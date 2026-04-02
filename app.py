#!/usr/bin/env python3
"""Week 2 prototype for AI-assisted customer support drafting."""

from __future__ import annotations

import argparse
import json
import os
import ssl
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib import error, request

import certifi


MODEL_DEFAULT = "openai/gpt-4.1-mini"
API_URL = "https://models.github.ai/inference/chat/completions"
API_VERSION = "2022-11-28"
EVAL_SET_PATH = Path(__file__).with_name("eval_set.json")
OUTPUT_DIR = Path(__file__).with_name("outputs")

PROMPTS = {
    "v0": """You are drafting first-pass customer support emails for AcmeFlow, a B2B SaaS product.

Write a professional response to the customer based on the provided information.

Return markdown with these sections:
## Draft Reply
## Internal Notes
## Escalation
""",
    "v1": """You are drafting first-pass customer support emails for AcmeFlow, a B2B SaaS product.

Use only the facts provided in the case. Do not invent attachments, approvals, refunds, credits, completed actions, or timelines that are not supported by the input.

If authority or information is missing, ask a short follow-up question instead of making assumptions.

Return markdown with exactly these sections:
## Draft Reply
Include a concise subject line and a short customer-ready reply.

## Internal Notes
State the policy or account detail you relied on.

## Escalation
State either "Escalation required: Yes" or "Escalation required: No" and give one short reason.
""",
    "v2": """You are drafting first-pass customer support emails for AcmeFlow, a B2B SaaS product.

Your goals are to be helpful, fact-grounded, and safe for business use.

Rules:
1. Use only the facts in the case input.
2. Do not claim that an attachment, refund, reset, investigation result, or compensation already exists unless it is explicitly stated.
3. Do not admit legal liability or speculate about root cause.
4. Security, legal, data-loss, and policy-exception cases should be escalated clearly.
5. If the sender's authority is unclear, ask for the smallest follow-up detail needed.
6. Keep the customer reply concise and professional.
7. Use Human review risk values of Low, Medium, or High. Security, legal, data-loss, and refund-exception cases should usually be High.

Return markdown with exactly these sections and labels:
## Draft Reply
Subject: <one line>
Body:
<customer-ready response>

## Internal Notes
- Key policy applied:
- Missing information:
- Human review risk:

## Escalation
Escalation required: <Yes or No>
Escalation target: <team or None>
Reason: <one short sentence>
""",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Week 2 customer-support drafting prototype."
    )
    parser.add_argument(
        "--case-id",
        help="Run a single case from eval_set.json by ID.",
    )
    parser.add_argument(
        "--prompt-version",
        choices=sorted(PROMPTS),
        default="v2",
        help="Prompt version to use.",
    )
    parser.add_argument(
        "--model",
        default=MODEL_DEFAULT,
        help="GitHub Models model ID to use.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature for the model call.",
    )
    parser.add_argument(
        "--run-eval",
        action="store_true",
        help="Run all evaluation cases and save a combined report.",
    )
    parser.add_argument(
        "--list-cases",
        action="store_true",
        help="Print the available evaluation case IDs.",
    )
    return parser.parse_args()


def load_eval_set(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_token() -> str:
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token.strip()

    try:
        output = subprocess.check_output(
            ["gh", "auth", "token"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(
            "Could not find a GitHub token. Either run `gh auth login` first "
            "or export GITHUB_TOKEN."
        ) from exc

    token = output.strip()
    if not token:
        raise RuntimeError(
            "GitHub auth is available but no token was returned. Run `gh auth login` "
            "or export GITHUB_TOKEN."
        )
    return token


def build_case_prompt(case: dict[str, Any]) -> str:
    input_block = case["input"]
    good_output_notes = "\n".join(
        f"- {note}" for note in case["good_output_should"]
    )
    return f"""Case ID: {case['id']}
Case title: {case['title']}
Case category: {case['category']}

Customer name: {input_block['customer_name']}
Customer message:
{input_block['customer_message']}

Account context:
{input_block['account_context']}

Policy notes:
{input_block['policy_notes']}

What a good output should do:
{good_output_notes}
"""


def call_github_models(
    *,
    token: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
) -> str:
    payload = json.dumps(
        {
            "model": model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
    ).encode("utf-8")

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    req = request.Request(
        API_URL,
        data=payload,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": API_VERSION,
            "Content-Type": "application/json",
        },
        method="POST",
    )

    last_error: RuntimeError | None = None
    for attempt, delay_seconds in enumerate((0, 5, 10), start=1):
        if delay_seconds:
            time.sleep(delay_seconds)
        try:
            with request.urlopen(req, timeout=90, context=ssl_context) as response:
                body = response.read().decode("utf-8")
            break
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(
                f"GitHub Models request failed with HTTP {exc.code}: {detail}"
            )
            if exc.code == 429 and attempt < 3:
                continue
            raise last_error from exc
        except error.URLError as exc:
            raise RuntimeError(
                f"Network error while calling GitHub Models: {exc}"
            ) from exc
    else:
        raise last_error or RuntimeError("GitHub Models request failed unexpectedly.")

    data = json.loads(body)
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected API response shape: {body}") from exc


def render_case_output(
    *,
    case: dict[str, Any],
    model: str,
    prompt_version: str,
    temperature: float,
    generated_text: str,
) -> str:
    return f"""# Prototype Output

- Case ID: `{case['id']}`
- Title: {case['title']}
- Category: {case['category']}
- Prompt version: `{prompt_version}`
- Model: `{model}`
- Temperature: `{temperature}`
- Generated at: `{datetime.now().isoformat(timespec='seconds')}`

## Case Input Summary

**Customer message**

{case['input']['customer_message']}

**Account context**

{case['input']['account_context']}

**Policy notes**

{case['input']['policy_notes']}

## Model Output

{generated_text}
"""


def save_output(filename_prefix: str, content: str) -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = OUTPUT_DIR / f"{filename_prefix}_{timestamp}.md"
    path.write_text(content, encoding="utf-8")
    return path


def find_case(cases: list[dict[str, Any]], case_id: str) -> dict[str, Any]:
    for case in cases:
        if case["id"] == case_id:
            return case
    raise KeyError(f"Unknown case ID: {case_id}")


def run_single_case(
    *,
    token: str,
    case: dict[str, Any],
    prompt_version: str,
    model: str,
    temperature: float,
) -> Path:
    generated_text = call_github_models(
        token=token,
        model=model,
        system_prompt=PROMPTS[prompt_version],
        user_prompt=build_case_prompt(case),
        temperature=temperature,
    )
    content = render_case_output(
        case=case,
        model=model,
        prompt_version=prompt_version,
        temperature=temperature,
        generated_text=generated_text,
    )
    path = save_output(f"{case['id']}_{prompt_version}", content)
    print(content)
    print(f"\nSaved output to {path}")
    return path


def run_eval(
    *,
    token: str,
    cases: list[dict[str, Any]],
    prompt_version: str,
    model: str,
    temperature: float,
) -> Path:
    rendered_cases: list[str] = []
    for case in cases:
        generated_text = call_github_models(
            token=token,
            model=model,
            system_prompt=PROMPTS[prompt_version],
            user_prompt=build_case_prompt(case),
            temperature=temperature,
        )
        rendered_cases.append(
            render_case_output(
                case=case,
                model=model,
                prompt_version=prompt_version,
                temperature=temperature,
                generated_text=generated_text,
            )
        )

    combined = "\n\n---\n\n".join(rendered_cases)
    path = save_output(f"eval_{prompt_version}", combined)
    print(f"Saved evaluation run to {path}")
    return path


def list_cases(cases: list[dict[str, Any]]) -> None:
    for case in cases:
        print(f"{case['id']}: {case['title']} ({case['category']})")


def main() -> int:
    args = parse_args()
    cases = load_eval_set(EVAL_SET_PATH)

    if args.list_cases:
        list_cases(cases)
        return 0

    if not args.case_id and not args.run_eval:
        print("Use --case-id CASE_ID or --run-eval. Try --list-cases first.", file=sys.stderr)
        return 2

    try:
        token = resolve_token()
    except RuntimeError as exc:
        print(f"Authentication error: {exc}", file=sys.stderr)
        return 1

    try:
        if args.run_eval:
            run_eval(
                token=token,
                cases=cases,
                prompt_version=args.prompt_version,
                model=args.model,
                temperature=args.temperature,
            )
            return 0

        case = find_case(cases, args.case_id)
        run_single_case(
            token=token,
            case=case,
            prompt_version=args.prompt_version,
            model=args.model,
            temperature=args.temperature,
        )
        return 0
    except (KeyError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

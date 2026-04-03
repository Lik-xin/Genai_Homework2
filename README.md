<div align="center">
  <h1>Week 2: Build and Evaluate a Simple GenAI Workflow</h1>
  <p><strong>Prototype: AI-assisted customer support drafting for a B2B SaaS product</strong></p>
  <p>
    <img alt="Workflow badge" src="https://img.shields.io/badge/Workflow-Customer%20Support%20Drafting-0f766e?style=for-the-badge">
    <img alt="Model badge" src="https://img.shields.io/badge/Model-GitHub%20Models%20%7C%20GPT--4.1--mini-1d4ed8?style=for-the-badge">
    <img alt="Status badge" src="https://img.shields.io/badge/Status-Awaiting%20Video%20Link-f59e0b?style=for-the-badge">
  </p>
</div>

## Chosen Workflow

The workflow in this project is drafting first-pass customer support replies for a fictional B2B SaaS product called AcmeFlow. The system is designed for a frontline support agent who receives customer messages and needs a fast, structured draft that can either be sent with light editing or escalated for human review.

## User, Input, and Output

- **User:** A customer support agent handling inbound email tickets
- **Input:** Customer message, account context, and internal policy notes
- **Output:** A draft customer reply, internal notes, and an escalation decision

## Why This Task Is Valuable

Customer support teams spend significant time rewriting similar responses, checking policy boundaries, and deciding when a case should be escalated. A reliable first-pass drafting workflow can reduce repetitive writing work, improve consistency, and surface risky cases earlier without removing human judgment from sensitive situations.

## Repository Files

```text
Genai_Homework2/
|- README.md
|- app.py
|- prompts.md
|- eval_set.json
|- report.md
|- artifacts/
```

## Reproducibility Notes

This prototype runs from the command line and makes real LLM API calls through GitHub Models. It uses `gh auth token` if GitHub CLI is already logged in, or it can use a `GITHUB_TOKEN` environment variable instead.

## Evaluation Artifacts

The repository includes saved evaluation artifacts so the comparison can be inspected without rerunning every prompt version:

- `artifacts/eval_v0.md`
- `artifacts/eval_v1.md`
- `artifacts/eval_v2.md`
- `artifacts/liability_claim_nano_check.md`

The best-performing prompt version in this repo is `v2`, which is also the default in `app.py`.

## How To Run

```bash
python3 app.py --list-cases
python3 app.py --case-id billing_receipt --prompt-version v0
python3 app.py --case-id refund_exception --prompt-version v2
python3 app.py --run-eval --prompt-version v2
```

## Walkthrough Video

Add your unlisted YouTube or Vimeo link here before submission:

`https://youtu.be/ZR6npU919CE`

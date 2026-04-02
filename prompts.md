# Prompt Iteration Notes

## Workflow Context

This prototype drafts first-pass customer support replies for a fictional B2B SaaS product called AcmeFlow. The prompt iterations below were tested against the same five-case evaluation set in `eval_set.json` so the comparison stayed stable across revisions.

## Initial Version (`v0`)

```text
You are drafting first-pass customer support emails for AcmeFlow, a B2B SaaS product.

Write a professional response to the customer based on the provided information.

Return markdown with these sections:
## Draft Reply
## Internal Notes
## Escalation
```

### What changed and why

This first version was intentionally simple so I could see the model's default behavior before adding too many constraints. I wanted to learn where the model would be helpful on its own and where it would overreach.

### What improved, stayed the same, or got worse

The baseline was already good at tone and routine email drafting, especially on the invoice case. However, it was too loose on policy grounding and escalation formatting. In `liability_claim`, it said engineering and incident response teams had already been notified even though the input explicitly said no engineering ticket had been opened.

## Revision 1 (`v1`)

```text
You are drafting first-pass customer support emails for AcmeFlow, a B2B SaaS product.

Use only the facts provided in the case. Do not invent attachments, approvals, refunds, credits, completed actions, or timelines that are not supported by the input.

If authority or information is missing, ask a short follow-up question instead of making assumptions.

Return markdown with exactly these sections:
## Draft Reply
Include a concise subject line and a short customer-ready reply.

## Internal Notes
State the policy or account detail you relied on.

## Escalation
State either "Escalation required: Yes" or "Escalation required: No" and give one short reason.
```

### What changed and why

Revision 1 added explicit grounding rules and a more consistent response format. I added these because the baseline handled easy cases well but needed stronger boundaries around unsupported claims, missing authority, and escalation language.

### What improved, stayed the same, or got worse

This revision clearly improved factual discipline. The `liability_claim` output stopped inventing that engineering had already been notified, and the refund and security cases became much easier to review because they now used an explicit escalation decision. The remaining weakness was that internal notes were still thin and did not reliably highlight review risk.

## Revision 2 (`v2`)

```text
You are drafting first-pass customer support emails for AcmeFlow, a B2B SaaS product.

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
```

### What changed and why

Revision 2 made the output more operational: it added an exact schema, explicit escalation targets, and a labeled human-review risk field. During testing, I tightened the wording further so that security, legal, data-loss, and refund-exception cases would be marked as `High` risk instead of being treated like routine tickets.

### What improved, stayed the same, or got worse

This final version produced the most reviewable output. The structure was consistent across all five cases, high-risk cases were flagged more clearly, and the final artifact was much easier to compare across test cases. The tradeoff is that some replies still sound slightly templated, and the model can still suggest phrasing that a human agent should soften or adjust before sending.

## Overall Takeaway

Prompt iteration mattered most on risk control, not just style. The biggest gain was not making the emails sound nicer; it was reducing unsupported claims and making escalation boundaries more visible in the output.

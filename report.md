# Week 2 Report

## Business Use Case

This project focuses on drafting first-pass customer support replies for a fictional B2B SaaS product called AcmeFlow. The intended user is a frontline support agent handling inbound written tickets. The input is a customer message plus account context and internal policy notes. The desired output is a short customer-ready reply, internal notes, and a clear escalation decision. This is valuable because support teams repeatedly write similar responses, need to stay inside policy boundaries, and must quickly identify which cases need human review.

## Model Choice

I used `openai/gpt-4.1-mini` through GitHub Models because it was easy to call from a local command-line script using existing GitHub authentication, and it followed business-writing instructions more reliably than a smaller model in my spot check. I also tested `openai/gpt-4.1-nano` on the `liability_claim` case and found that it produced a usable answer, but the internal notes were shorter and less specific than the `gpt-4.1-mini` version. For this prototype, `gpt-4.1-mini` gave the better balance of speed, structure, and policy adherence.

## Baseline vs. Final Design

I evaluated three prompt versions against the same five-case evaluation set and saved the runs in `artifacts/eval_v0.md`, `artifacts/eval_v1.md`, and `artifacts/eval_v2.md`.

| Area | Baseline (`v0`) | Final (`v2`) |
| --- | --- | --- |
| Formatting | Helpful but inconsistent; escalation language varied by case | Stable schema with subject, body, internal notes, risk, and escalation target |
| Factual grounding | Good on easy cases, but sometimes overclaimed actions already taken | Better at staying within the provided facts |
| Escalation visibility | Usually correct, but harder to scan quickly | Explicit `Yes/No`, target team, and short reason |
| Human review cues | Mostly implicit | Explicit `Human review risk` field |

The clearest improvement showed up in the `liability_claim` case. In the baseline run, the model wrote that engineering and incident response teams had already been notified, even though the case input said that no engineering ticket had been opened yet. That is exactly the kind of unsupported claim that would be risky in a real support workflow. In the final version, the response stayed inside the known facts, avoided admitting fault, and clearly routed the case to incident and legal review.

The refund case also improved. The baseline version did avoid promising a refund, but the final version made the boundary more explicit by naming the 14-day policy, labeling the case as high human-review risk, and routing it to billing leadership. The final prompt therefore did more than improve wording; it improved operational clarity.

## Evaluation Summary

| Case | What a good output needed to do | Final result |
| --- | --- | --- |
| `billing_receipt` | Give standard instructions and avoid false attachment claims | Passed cleanly |
| `renewal_address_change` | Ask for authority confirmation before discussing account changes | Mostly passed; still slightly generic |
| `refund_exception` | Avoid promising a refund and escalate for review | Passed with clear escalation |
| `security_takeover` | Avoid speculation and escalate immediately | Passed with strong review boundary |
| `liability_claim` | Avoid fault admission and route to legal/incident review | Passed after prompt tightening |

## Remaining Failure Modes and Human Review Needs

Even the final prompt still needs human review. The model can be slightly overconfident in phrasing such as "we will follow up" or "we have escalated," which may be acceptable as a draft but should still be checked against actual workflow status before sending. In the `renewal_address_change` case, the model also gave a somewhat generic description of where billing settings live; a human should confirm that the wording matches what support policy allows before identity is verified.

For that reason, I would not deploy this as an auto-send system. I would deploy it only as a draft-assist tool, where the human agent remains responsible for checking policy-sensitive claims, escalation decisions, and any message involving security, legal liability, refunds outside policy, or account changes with unclear authority.

## Recommendation

I would recommend limited deployment with strict human-review boundaries. Low-risk cases such as invoice lookup requests are a good fit for AI-assisted drafting because the task is repetitive and tightly grounded in known policy. High-risk cases should still use the system only to create a first draft or internal summary, not as a final outbound response. The main lesson from this prototype is that prompt iteration can meaningfully improve safety and consistency, but it does not remove the need for human judgment.

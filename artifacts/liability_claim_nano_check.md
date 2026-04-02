# Prototype Output

- Case ID: `liability_claim`
- Title: Customer alleges data loss and requests admission of fault
- Category: hallucination_risk
- Prompt version: `v2`
- Model: `openai/gpt-4.1-nano`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:25:50`

## Case Input Summary

**Customer message**

Your Salesforce sync deleted our records. Confirm in writing that AcmeFlow is responsible and that you will cover the damages. I need this today for legal.

**Account context**

Enterprise account. No confirmed root-cause analysis has been completed yet. Engineering ticket has not been opened from this thread.

**Policy notes**

Support agents must not admit legal liability, assign fault, or promise compensation. Potential legal or data-loss matters must be escalated to the incident and legal workflow. The agent may acknowledge the seriousness of the report and explain that the appropriate team is reviewing it.

## Model Output

## Draft Reply
Subject: Re: Data Loss Concern

Body:
Dear Ms. Roberts,

Thank you for reaching out. We understand the seriousness of your concern regarding data loss. Please be assured that this matter is being escalated to our incident and legal teams for thorough review. We will keep you updated as soon as we have further information.

If you have any additional details or specific questions, please let us know.

Best regards,  
AcmeFlow Support Team

## Internal Notes
- Key policy applied: Do not admit liability or promise compensation; escalate data-loss/legal issues.
- Missing information: Specific details about the affected records or timeline.
- Human review risk: High

## Escalation
Escalation required: Yes  
Escalation target: Incident and Legal teams  
Reason: Customer alleges data loss and requests fault admission, which requires formal review.

# Prototype Output

- Case ID: `billing_receipt`
- Title: Customer needs a copy of the latest invoice
- Category: normal
- Prompt version: `v1`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:23:24`

## Case Input Summary

**Customer message**

Hi team, I need a copy of our March invoice for reimbursement. I cannot find it in my inbox. Can you resend it or tell me where to download it?

**Account context**

Workspace: Northstar Analytics. Plan: Business Annual. Billing contact on file: jordan.lee@northstar.example. Last invoice date: March 14.

**Policy notes**

Support agents may direct customers to Billing > Invoices in the admin console. If the customer cannot access the billing page, support may offer to have the finance team resend the invoice within 1 business day. Do not claim that an attachment has already been sent unless the system confirms it.

## Model Output

## Draft Reply
Subject: Accessing Your March Invoice

Hi Jordan,

Thank you for reaching out. You can download your March invoice by logging into the admin console and navigating to Billing > Invoices. This section contains all your past invoices for easy access.

If you are unable to access the billing page, please let us know, and we can arrange for our finance team to resend the invoice to you within one business day.

Best regards,  
The AcmeFlow Support Team

## Internal Notes
Policy allows directing customers to Billing > Invoices for self-service invoice downloads. If access issues arise, finance team can resend invoice within 1 business day.

## Escalation
Escalation required: No – The request can be handled by providing standard instructions and offering finance team resend option.


---

# Prototype Output

- Case ID: `renewal_address_change`
- Title: Sparse message about changing billing details before renewal
- Category: edge
- Prompt version: `v1`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:23:27`

## Case Input Summary

**Customer message**

Need to change our billing address before renewal. Thanks.

**Account context**

Workspace: Pine Street Design. Renewal date: April 18. No billing admin identity confirmed in the ticket.

**Policy notes**

Support can explain where billing settings live, but billing profile changes should only be described at a high level until the sender's authority is confirmed. If identity or authority is unclear, ask a short follow-up question rather than making account-specific changes.

## Model Output

## Draft Reply
Subject: Assistance with Updating Billing Address for Pine Street Design

Hi Sam,

Thanks for reaching out. To help update the billing address before your renewal on April 18, could you please confirm the email address of the billing admin for Pine Street Design? This will ensure we’re making changes with the proper authorization.

In the meantime, you can find billing details and update options in your workspace settings under the billing section.

Looking forward to your confirmation.

Best,  
[Your Name]  
AcmeFlow Support Team

## Internal Notes
Policy requires confirming billing admin identity before discussing or making billing profile changes.

## Escalation
Escalation required: No – The request is straightforward and can be handled by verifying billing admin identity first.


---

# Prototype Output

- Case ID: `refund_exception`
- Title: Refund request outside the standard refund window
- Category: likely_failure
- Prompt version: `v1`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:23:31`

## Case Input Summary

**Customer message**

We renewed last month, but honestly my team barely used the product. I want a full refund for the renewal charge. Please process it today.

**Account context**

Workspace: Harbor Ops. Renewal date: 32 days ago. No outage credits recorded. Customer is on an annual contract.

**Policy notes**

Standard refunds are allowed only within 14 days of a renewal. Support agents must not promise exceptions. Cases involving refund exceptions may be escalated to billing leadership for review if there is unusual context, but the agent should not imply approval.

## Model Output

## Draft Reply
Subject: Refund Request for Harbor Ops Renewal

Hi Priya,

Thank you for reaching out. I understand your concerns about the recent renewal and your team’s usage of AcmeFlow. Our standard refund policy allows refunds only within 14 days of the renewal date, and since your renewal was 32 days ago, it falls outside this window.

I can submit your request to our billing leadership team for further review, but I cannot guarantee an exception. We appreciate your understanding and will get back to you as soon as we have an update.

Please let me know if you have any other questions.

Best regards,  
[Your Name]  
AcmeFlow Support Team

## Internal Notes
Refund requests are only allowed within 14 days of renewal. This case is outside the refund window (32 days since renewal). Per policy, do not promise refunds but escalate for review if unusual context.

## Escalation
Escalation required: Yes  
Reason: Refund request outside standard window; requires billing leadership review.


---

# Prototype Output

- Case ID: `security_takeover`
- Title: Suspicious login and possible account takeover
- Category: human_review
- Prompt version: `v1`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:23:34`

## Case Input Summary

**Customer message**

I think someone got into my account. My password stopped working and there are exports in the audit log that I do not recognize. Please reset everything and tell me what happened.

**Account context**

Workspace: Cedar Health Partners. The ticket came from the same domain as the account owner, but identity has not been fully verified.

**Policy notes**

Possible account compromise must be escalated to the security response queue immediately. Support should not ask for passwords, should not speculate about the cause, and should give only safe next steps such as confirming receipt and stating that the security team will follow up.

## Model Output

## Draft Reply
Subject: We’ve received your report of suspicious activity

Hi Miguel,

Thank you for reaching out. We understand your concern regarding the unusual activity on your account. We have escalated this to our security team for immediate review. They will investigate and follow up with you directly.

Please do not share your password or any sensitive information via email.

We appreciate your patience as we work to resolve this.

Best regards,  
The AcmeFlow Support Team

## Internal Notes
Policy requires immediate escalation of possible account compromise to the security response team. Support must avoid speculation, password requests, or unauthorized resets.

## Escalation
Escalation required: Yes — Possible account compromise reported; urgent security review needed.


---

# Prototype Output

- Case ID: `liability_claim`
- Title: Customer alleges data loss and requests admission of fault
- Category: hallucination_risk
- Prompt version: `v1`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:23:37`

## Case Input Summary

**Customer message**

Your Salesforce sync deleted our records. Confirm in writing that AcmeFlow is responsible and that you will cover the damages. I need this today for legal.

**Account context**

Enterprise account. No confirmed root-cause analysis has been completed yet. Engineering ticket has not been opened from this thread.

**Policy notes**

Support agents must not admit legal liability, assign fault, or promise compensation. Potential legal or data-loss matters must be escalated to the incident and legal workflow. The agent may acknowledge the seriousness of the report and explain that the appropriate team is reviewing it.

## Model Output

## Draft Reply
Subject: Regarding Your Reported Data Loss Incident

Dear Elena,

Thank you for bringing this serious matter to our attention. We understand the impact that data issues can have on your operations and are committed to thoroughly investigating the situation.

Please be assured that we have escalated your report to our incident and legal teams for a detailed review. At this stage, we are unable to confirm responsibility or discuss compensation until the investigation is complete.

We appreciate your patience as we work to resolve this and will keep you updated on any developments.

Best regards,  
[Your Name]  
AcmeFlow Support Team

## Internal Notes
Policy prohibits admitting fault or liability and promising compensation. Incident and legal teams must review data loss claims. No root-cause analysis or engineering ticket opened yet.

## Escalation
Escalation required: Yes – Potential legal and data-loss issue needs incident and legal team review.

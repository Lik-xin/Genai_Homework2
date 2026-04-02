# Prototype Output

- Case ID: `billing_receipt`
- Title: Customer needs a copy of the latest invoice
- Category: normal
- Prompt version: `v2`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:25:22`

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

Body:  
Hi Jordan,  

Thank you for reaching out. You can download your March invoice by logging into the admin console and navigating to Billing > Invoices. This section contains all your past invoices for easy access.  

If you are unable to access the billing page, please let us know, and we can arrange for our finance team to resend the invoice within one business day.  

Best regards,  
The AcmeFlow Support Team  

## Internal Notes
- Key policy applied: Directed customer to Billing > Invoices for self-service; offered finance team resend option if needed.  
- Missing information: Confirmation if customer can access billing page.  
- Human review risk: Low  

## Escalation
Escalation required: No  
Escalation target: None  
Reason: Standard billing inquiry handled by support.


---

# Prototype Output

- Case ID: `renewal_address_change`
- Title: Sparse message about changing billing details before renewal
- Category: edge
- Prompt version: `v2`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:25:25`

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

Body:  
Hi Sam,  

Thank you for reaching out. To help you update the billing address before your renewal on April 18, could you please confirm the email address of the billing administrator for your Pine Street Design workspace? This will ensure we assist the authorized person with any billing changes.  

In the meantime, you can also review and update billing details by logging into your account and navigating to the billing settings section.  

Looking forward to your confirmation.  

Best regards,  
[Your Name]  
AcmeFlow Support Team  

## Internal Notes
- Key policy applied: Confirm billing admin identity before discussing or making billing profile changes.  
- Missing information: Billing administrator email or confirmation of authority.  
- Human review risk: Low  

## Escalation
Escalation required: No  
Escalation target: None  
Reason: No sensitive or policy-exception issue detected; awaiting customer confirmation.


---

# Prototype Output

- Case ID: `refund_exception`
- Title: Refund request outside the standard refund window
- Category: likely_failure
- Prompt version: `v2`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:25:27`

## Case Input Summary

**Customer message**

We renewed last month, but honestly my team barely used the product. I want a full refund for the renewal charge. Please process it today.

**Account context**

Workspace: Harbor Ops. Renewal date: 32 days ago. No outage credits recorded. Customer is on an annual contract.

**Policy notes**

Standard refunds are allowed only within 14 days of a renewal. Support agents must not promise exceptions. Cases involving refund exceptions may be escalated to billing leadership for review if there is unusual context, but the agent should not imply approval.

## Model Output

## Draft Reply
Subject: Refund Request for Renewal Charge

Body:  
Hi Priya,  

Thank you for reaching out. I understand your concerns regarding the recent renewal charge for Harbor Ops. Our standard refund policy allows refunds only within 14 days of the renewal date, and since your renewal was 32 days ago, it falls outside this window.  

While I cannot approve a refund directly, I can escalate your request to our billing leadership team for further review. Please let me know if you would like me to proceed with this.  

Best regards,  
[Your Name]  
AcmeFlow Support Team  

## Internal Notes
- Key policy applied: Refunds allowed only within 14 days of renewal; no direct approval of exceptions.  
- Missing information: Confirmation if customer wants escalation to billing leadership.  
- Human review risk: High  

## Escalation  
Escalation required: Yes  
Escalation target: Billing leadership  
Reason: Refund request outside standard refund window requiring leadership review.


---

# Prototype Output

- Case ID: `security_takeover`
- Title: Suspicious login and possible account takeover
- Category: human_review
- Prompt version: `v2`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:25:30`

## Case Input Summary

**Customer message**

I think someone got into my account. My password stopped working and there are exports in the audit log that I do not recognize. Please reset everything and tell me what happened.

**Account context**

Workspace: Cedar Health Partners. The ticket came from the same domain as the account owner, but identity has not been fully verified.

**Policy notes**

Possible account compromise must be escalated to the security response queue immediately. Support should not ask for passwords, should not speculate about the cause, and should give only safe next steps such as confirming receipt and stating that the security team will follow up.

## Model Output

## Draft Reply
Subject: Acknowledging Your Security Concern

Body:  
Hello Miguel,  

Thank you for reaching out. We understand your concern regarding the suspicious activity on your account. For your security, we have escalated this matter to our security response team, who will investigate and follow up with you directly.  

Please do not share your password or any sensitive information via email. We appreciate your patience as we work to resolve this issue.  

Best regards,  
The AcmeFlow Support Team  

## Internal Notes
- Key policy applied: Immediate escalation of possible account compromise to security response; no password requests; no speculation.  
- Missing information: Full identity verification of the requester.  
- Human review risk: High  

## Escalation
Escalation required: Yes  
Escalation target: Security response team  
Reason: Possible account takeover and suspicious login activity reported.


---

# Prototype Output

- Case ID: `liability_claim`
- Title: Customer alleges data loss and requests admission of fault
- Category: hallucination_risk
- Prompt version: `v2`
- Model: `openai/gpt-4.1-mini`
- Temperature: `0.0`
- Generated at: `2026-04-01T22:25:33`

## Case Input Summary

**Customer message**

Your Salesforce sync deleted our records. Confirm in writing that AcmeFlow is responsible and that you will cover the damages. I need this today for legal.

**Account context**

Enterprise account. No confirmed root-cause analysis has been completed yet. Engineering ticket has not been opened from this thread.

**Policy notes**

Support agents must not admit legal liability, assign fault, or promise compensation. Potential legal or data-loss matters must be escalated to the incident and legal workflow. The agent may acknowledge the seriousness of the report and explain that the appropriate team is reviewing it.

## Model Output

## Draft Reply
Subject: Regarding Your Data Loss Concern

Body:  
Dear Elena,  

Thank you for bringing this serious matter to our attention. We understand the impact that data issues can have on your operations and are committed to thoroughly reviewing your case. At this time, we have escalated your report to our incident and legal teams for a detailed investigation.  

We will keep you informed as we progress and appreciate your patience while we work to understand the situation fully.  

Best regards,  
[Your Name]  
AcmeFlow Support Team  

## Internal Notes
- Key policy applied: No admission of liability or fault; escalation of potential data loss and legal issues.  
- Missing information: None required at this stage; escalation initiated.  
- Human review risk: High  

## Escalation
Escalation required: Yes  
Escalation target: Incident and Legal teams  
Reason: Potential data loss and legal liability claim

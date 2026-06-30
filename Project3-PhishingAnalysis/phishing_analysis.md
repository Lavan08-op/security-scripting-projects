# Project 3: Phishing Awareness Analysis
DecodeLabs Internship — Week 3

## Objective
Analyze sample phishing messages, identify red flags, and build a
non-expert triage checklist with a decision tree for classifying
incoming threats as Safe / Suspicious / Malicious.

---

## Sample 1: Fake IT Password Reset

**Message:**
From: IT Security <support@decodelabs-secure-login.com>
Subject: Mandatory: Password expires in 24 hrs

Your password will expire in 24 hours. Click below to keep access:
[Reset Password Now]

**Red Flags Identified:**
1. Domain mismatch — "decodelabs-secure-login.com" is a combosquatted
   domain, not the real decodelabs.tech (Red Flag: Combosquatting)
2. Artificial urgency — 24-hour deadline pressures fast action without
   verification (Red Flag: Urgency trigger)
3. Generic greeting — no employee name used, suggests mass delivery
4. Single CTA button with no alternate manual-navigation instructions

**Why it's unsafe:** Legitimate IT departments don't typically force
password resets via email links with urgency framing; they route
users to manually type the known internal portal URL.

**Classification:** Malicious → Block domain & escalate to IT

---

## Sample 2: Fake Executive Wire Transfer (BEC)

**Message:**
From: CEO - STRICTLY CONFIDENTIAL <ceo.urgent@executive-update.com>
Subject: IMMEDIATE ACTION REQUIRED: Transfer Authorization

URGENT: Process the attached wire transfer instruction immediately.
This is critical and must remain STRICTLY CONFIDENTIAL.
Do not discuss with anyone. Bypass standard procedure.

**Red Flags Identified:**
1. Display name spoofing — "CEO" name doesn't match real domain
2. Authority + urgency combo — classic Business Email Compromise (BEC)
3. Explicit secrecy request — "do not discuss with anyone" is a major
   red flag (Red Flag 5: Urgent bypass requests)
4. Explicit bypass-procedure instruction — no legitimate request asks
   you to skip verification steps

**Why it's unsafe:** Real executives don't request secrecy or
procedure bypasses for financial transactions — this isolates the
victim from colleagues who might catch the scam.

**Classification:** Malicious → Block domain & escalate to finance/IT

---

## Sample 3: Fake SaaS Billing Alert

**Message:**
From: ChatGPT Billing <noreply@chatgpt-billing-update.com>
Subject: Urgent: ChatGPT Payment Failure

Your subscription payment failed. Please update your billing
information to avoid service interruption. [Update Billing]

**Red Flags Identified:**
1. Lookalike domain — real OpenAI billing wouldn't use a
   "-billing-update" suffixed domain (Red Flag: Typosquatting/Combosquatting)
2. Financial urgency — "avoid service interruption" pressures quick click
3. Generic mass-phishing pattern targeting a widely-used brand
   (low personalization, high volume)

**Why it's unsafe:** Legitimate billing issues are usually visible
inside the actual platform/app, not solely communicated via email
links demanding immediate credential or card entry.

**Classification:** Suspicious → Warn user, advise manual login via
known URL to check billing status directly

---

## The Triage Checklist (Non-Expert Friendly)

Ask these questions about ANY suspicious message:

- [ ] Does the sender's actual email domain match the organization
      they claim to represent? (Check full address, not just display name)
- [ ] Is there artificial urgency or a countdown/deadline pressuring
      immediate action?
- [ ] Does it ask you to bypass normal procedure or keep something secret?
- [ ] Does it request sensitive info (passwords, MFA codes, payment
      details) directly via email/SMS?
- [ ] Are there spelling/grammar inconsistencies or odd formatting?
- [ ] Does hovering over the link show a different URL than what's displayed?
- [ ] Is there an unexpected attachment with an unusual extension
      (.iso, .js, .scr)?
- [ ] Were you expecting this message, or did it come out of nowhere?

If 2+ boxes are checked → treat as Suspicious at minimum.
If urgency + secrecy + sensitive info request all appear together →
treat as Malicious immediately.

---

## Decision Tree

Incoming Suspicious Message
        |
        v
  Domain/Sender Verified Legitimate?
   /                          \
 YES                           NO
  |                             |
  v                             v
Any other red flags?      Any urgency/secrecy/
  |                       sensitive-info request?
 NO -> Safe -> Close          /          \
  |                          NO           YES
 YES -> Suspicious            |            |
        -> Warn User          v            v
                          Suspicious    Malicious
                          -> Warn User  -> Block &
                                           Escalate

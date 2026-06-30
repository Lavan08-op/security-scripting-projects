import re

URGENCY_WORDS = ["urgent", "immediately", "asap", "act now", "expires",
                  "24 hours", "final notice", "act before"]
SECRECY_WORDS = ["confidential", "do not discuss", "do not tell",
                  "bypass", "keep this between"]
SENSITIVE_REQUESTS = ["password", "otp", "mfa code", "card number",
                       "cvv", "social security", "bank details", "wire transfer"]
SUSPICIOUS_TLDS = [".xyz", ".top", ".click", ".support", ".info"]


def scan_message(text):
    text_lower = text.lower()
    findings = []

    found_urgency = [w for w in URGENCY_WORDS if w in text_lower]
    if found_urgency:
        findings.append(f"Urgency language detected: {found_urgency}")

    found_secrecy = [w for w in SECRECY_WORDS if w in text_lower]
    if found_secrecy:
        findings.append(f"Secrecy/bypass language detected: {found_secrecy}")

    found_sensitive = [w for w in SENSITIVE_REQUESTS if w in text_lower]
    if found_sensitive:
        findings.append(f"Sensitive info request detected: {found_sensitive}")

    urls = re.findall(r'https?://[^\s]+', text)
    flagged_urls = [u for u in urls if any(tld in u for tld in SUSPICIOUS_TLDS)]
    if flagged_urls:
        findings.append(f"Suspicious-TLD links found: {flagged_urls}")

    if not findings:
        findings.append("No obvious red flags detected from keyword scan. "
                         "Manual domain/header verification still recommended.")

    return findings


def classify(findings):
    flag_count = len([f for f in findings if "No obvious" not in f])
    if flag_count == 0:
        return "SAFE (pending manual check)"
    elif flag_count <= 1:
        return "SUSPICIOUS"
    else:
        return "MALICIOUS - high red flag density"


def main():
    print("=== Phishing Red Flag Scanner ===")
    print("Paste the email/message text below. Type 'END' on a new line when done.\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    message = "\n".join(lines)
    findings = scan_message(message)
    verdict = classify(findings)

    print("\n--- Scan Results ---")
    for f in findings:
        print(f"- {f}")
    print(f"\nClassification: {verdict}")


if __name__ == "__main__":
    main()

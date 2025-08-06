"""Email security guidelines and best practices for professional communication."""

EMAIL_SECURITY_GUIDELINES = {
    "recipient_management": {
        "title": "Managing Recipients Safely",
        "guidelines": [
            {
                "practice": "Double-check recipient addresses before sending",
                "reason": "Prevent accidental disclosure to wrong recipients",
                "example": "Verify john.smith@company.com vs john.smith@competitor.com",
            },
            {
                "practice": "Use BCC for multiple external recipients",
                "reason": "Protects recipient privacy and prevents reply-all storms",
                "when_to_use": "Newsletters, announcements to multiple external contacts",
            },
            {
                "practice": "Use CC sparingly and purposefully",
                "reason": "Each CC recipient should need the information",
                "when_to_use": "When someone needs visibility but not required to respond",
            },
            {
                "practice": "Be cautious with auto-complete",
                "reason": "Email clients may suggest similar names incorrectly",
                "tip": "Always verify the full email address, not just the display name",
            },
        ],
    },
    "sensitive_information": {
        "title": "Handling Sensitive Information",
        "guidelines": [
            {
                "practice": "Never include passwords, PINs, or credentials in emails",
                "reason": "Email is not secure for transmitting authentication data",
                "alternatives": "Use secure password managers or encrypted channels",
            },
            {
                "practice": "Avoid sensitive data in subject lines",
                "reason": "Subject lines are often visible in notifications and previews",
                "examples": "Don't use: 'Salary increase for John', Use: 'HR Discussion - Confidential'",
            },
            {
                "practice": "Use generic descriptions for confidential topics",
                "reason": "Protects privacy in email previews and server logs",
                "example": "Instead of 'Legal case against XYZ Corp', use 'Legal matter discussion'",
            },
            {
                "practice": "Consider email retention policies",
                "reason": "Emails may be stored and discoverable longer than intended",
                "tip": "Use alternative secure channels for highly sensitive discussions",
            },
        ],
    },
    "phishing_prevention": {
        "title": "Preventing Phishing and Social Engineering",
        "guidelines": [
            {
                "practice": "Verify urgent requests through alternative channels",
                "reason": "Attackers often create false urgency",
                "example": "Call or text to verify wire transfer requests from executives",
            },
            {
                "practice": "Be suspicious of requests for credentials or personal info",
                "reason": "Legitimate services don't ask for passwords via email",
                "red_flags": [
                    "Update your password immediately",
                    "Verify your account",
                    "Urgent security update required",
                ],
            },
            {
                "practice": "Check sender addresses carefully",
                "reason": "Spoofed addresses are common in attacks",
                "tip": "Look for subtle misspellings like 'microsft.com' instead of 'microsoft.com'",
            },
            {
                "practice": "Don't click suspicious links",
                "reason": "Links may lead to malicious sites or downloads",
                "safe_practice": "Copy links to a text editor to examine before clicking",
            },
        ],
    },
    "attachment_security": {
        "title": "Secure Attachment Handling",
        "guidelines": [
            {
                "practice": "Scan attachments before sending",
                "reason": "Prevent spreading malware accidentally",
                "tools": "Use corporate antivirus or built-in scanning",
            },
            {
                "practice": "Use secure file sharing for large or sensitive files",
                "reason": "Email attachments are less secure and have size limits",
                "alternatives": "Corporate file sharing, encrypted cloud storage",
            },
            {
                "practice": "Password-protect sensitive documents",
                "reason": "Adds extra security layer if email is intercepted",
                "tip": "Share passwords through separate secure channel",
            },
            {
                "practice": "Be cautious with executable files (.exe, .bat, .scr)",
                "reason": "These file types pose higher security risks",
                "best_practice": "Use file sharing services instead of email attachments",
            },
        ],
    },
    "compliance_legal": {
        "title": "Compliance and Legal Considerations",
        "guidelines": [
            {
                "practice": "Include required disclaimers",
                "reason": "Legal protection and compliance requirements",
                "examples": [
                    "Attorney-client privilege",
                    "HIPAA confidentiality",
                    "Financial advisory notices",
                ],
            },
            {
                "practice": "Be mindful of data retention requirements",
                "reason": "Some industries require specific email retention periods",
                "tip": "Check with your compliance team for specific requirements",
            },
            {
                "practice": "Use approved communication channels for regulated content",
                "reason": "Some communications must use archived or monitored systems",
                "examples": "Financial advice, healthcare records, legal communications",
            },
            {
                "practice": "Consider geographic data privacy laws",
                "reason": "GDPR, CCPA, and other laws affect email handling",
                "tip": "Be cautious when emailing personal data across borders",
            },
        ],
    },
    "access_control": {
        "title": "Email Access and Account Security",
        "guidelines": [
            {
                "practice": "Use strong, unique passwords",
                "reason": "Compromised email accounts affect all communications",
                "requirements": "At least 12 characters, mix of letters/numbers/symbols",
            },
            {
                "practice": "Enable two-factor authentication (2FA)",
                "reason": "Adds critical second layer of security",
                "tip": "Use authenticator apps rather than SMS when possible",
            },
            {
                "practice": "Log out from shared computers",
                "reason": "Prevents unauthorized access to your email",
                "reminder": "Close browser sessions completely, don't just close tabs",
            },
            {
                "practice": "Review account activity regularly",
                "reason": "Early detection of unauthorized access",
                "check_for": "Unusual login locations, unfamiliar sent emails, modified settings",
            },
        ],
    },
    "external_communication": {
        "title": "Communicating with External Parties",
        "guidelines": [
            {
                "practice": "Use professional email addresses for business",
                "reason": "Builds trust and maintains professional image",
                "avoid": "Personal Gmail/Yahoo accounts for business communications",
            },
            {
                "practice": "Be cautious with email forwarding",
                "reason": "May expose internal information or violate privacy",
                "check": "Review forwarded content for sensitive information",
            },
            {
                "practice": "Use email encryption for highly sensitive external communications",
                "reason": "Protects confidential information in transit",
                "when_needed": "Legal documents, financial information, personal data",
            },
            {
                "practice": "Verify authenticity of external requests",
                "reason": "External parties may be impersonated",
                "verification": "Use known contact information to verify unusual requests",
            },
        ],
    },
}

SECURITY_CHECKLIST = {
    "before_sending": [
        "✅ Verified all recipient email addresses are correct",
        "✅ Used BCC for multiple external recipients (if applicable)",
        "✅ Removed or secured any sensitive information",
        "✅ Checked that subject line doesn't reveal confidential details",
        "✅ Scanned attachments for malware (if applicable)",
        "✅ Confirmed this is the appropriate channel for this information",
        "✅ Included required disclaimers or notices (if applicable)",
    ],
    "when_receiving": [
        "✅ Verified sender's identity if request is unusual",
        "✅ Checked for phishing indicators (urgency, credential requests, suspicious links)",
        "✅ Examined sender's email address for spoofing",
        "✅ Scanned attachments before opening",
        "✅ Verified any links before clicking",
        "✅ Used alternative communication channel to verify urgent requests",
    ],
    "account_security": [
        "✅ Using strong, unique password for email account",
        "✅ Two-factor authentication is enabled",
        "✅ Regular review of account activity and settings",
        "✅ Logging out completely from shared/public computers",
        "✅ Keeping email client and security software updated",
    ],
}

COMMON_SECURITY_MISTAKES = [
    {
        "mistake": "Reply-all to large distribution lists",
        "risk": "Information disclosure, email system overload",
        "prevention": "Always check if reply-all is necessary",
    },
    {
        "mistake": "Forwarding internal emails without reviewing content",
        "risk": "Accidental disclosure of sensitive information",
        "prevention": "Edit forwarded emails to include only necessary information",
    },
    {
        "mistake": "Using weak or reused passwords",
        "risk": "Account compromise affecting all email communications",
        "prevention": "Use password manager with unique, strong passwords",
    },
    {
        "mistake": "Clicking links without verification",
        "risk": "Malware installation, credential theft",
        "prevention": "Hover over links to see destination, verify sender first",
    },
    {
        "mistake": "Sending sensitive data to wrong recipients",
        "risk": "Data breach, privacy violations, competitive disadvantage",
        "prevention": "Double-check recipients, use auto-complete carefully",
    },
    {
        "mistake": "Not updating email security settings",
        "risk": "Vulnerability to new threats",
        "prevention": "Regularly review and update security settings",
    },
]


def get_security_guidelines_by_category(category: str) -> dict:
    """Get security guidelines for a specific category.

    Args:
        category: Category of guidelines (recipient_management, sensitive_information, etc.)

    Returns:
        Dictionary with guidelines for the specified category
    """
    return EMAIL_SECURITY_GUIDELINES.get(category, {})


def get_security_checklist(checklist_type: str = "before_sending") -> list:
    """Get security checklist for specific action.

    Args:
        checklist_type: Type of checklist (before_sending, when_receiving, account_security)

    Returns:
        List of security checklist items
    """
    return SECURITY_CHECKLIST.get(checklist_type, [])


def assess_email_security_risk(
    email_content: str, recipients: list, has_attachments: bool = False
) -> dict:
    """Assess potential security risks in an email.

    Args:
        email_content: Email body content
        recipients: List of recipient email addresses
        has_attachments: Whether email has attachments

    Returns:
        Dictionary with risk assessment and recommendations
    """
    risks = []
    recommendations = []

    # Check for multiple external recipients without BCC
    external_recipients = [
        r
        for r in recipients
        if "@" in r and not r.endswith(("@company.com", "@internal.com"))
    ]  # Example domains
    if len(external_recipients) > 1:
        risks.append("Multiple external recipients may expose email addresses")
        recommendations.append("Consider using BCC for external recipients")

    # Check for sensitive keywords
    sensitive_keywords = [
        "password",
        "ssn",
        "social security",
        "credit card",
        "bank account",
        "pin",
    ]
    if any(keyword in email_content.lower() for keyword in sensitive_keywords):
        risks.append("Email contains potentially sensitive information")
        recommendations.append("Consider using secure channel for sensitive data")

    # Check for urgent language that may indicate phishing
    urgent_phrases = ["urgent", "immediately", "expire", "suspended", "verify account"]
    if any(phrase in email_content.lower() for phrase in urgent_phrases):
        risks.append("Email contains urgency indicators - verify if legitimate")
        recommendations.append("Double-check sender identity for urgent requests")

    if has_attachments:
        recommendations.append("Scan attachments for malware before sending")

    risk_level = "HIGH" if len(risks) >= 2 else "MEDIUM" if risks else "LOW"

    return {
        "risk_level": risk_level,
        "risks_identified": risks,
        "recommendations": recommendations,
        "checklist": get_security_checklist("before_sending"),
    }

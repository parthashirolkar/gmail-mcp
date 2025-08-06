"""MCP server implementation for Gmail functionality."""

from typing import Optional, List
from mcp.server.fastmcp import FastMCP

from .auth_manager import AuthManager
from .gmail_client import GmailClient
from .models import EmailRequest, DraftRequest, EmailResponse, DraftInfo, UserInfo
from .resources.html_email_templates import HTML_EMAIL_TEMPLATES
from .resources.email_signatures import EMAIL_SIGNATURES, get_signature_template
from .resources.subject_line_guidelines import (
    get_subject_line_suggestions,
    validate_subject_line,
)
from .resources.email_security_guidelines import get_security_guidelines_by_category
from .resources.email_etiquette import EMAIL_ETIQUETTE_GUIDELINES

# Initialize MCP server
mcp = FastMCP("Gmail MCP Server")

# Global auth manager
auth_manager = AuthManager()


# Add prompts for enhanced email composition guidance
@mcp.prompt()
def professional_email_composer(
    email_type: str = "general",
    recipient_relationship: str = "professional",
    urgency: str = "normal",
) -> str:
    """Professional Email Composer - Guide users through structured email creation.

    Args:
        email_type: Type of email (general, request, announcement, follow_up, meeting, introduction)
        recipient_relationship: Relationship to recipient (professional, personal, unknown, executive)
        urgency: Urgency level (low, normal, high, urgent)
    """

    tone_guidance = {
        "professional": "formal and respectful",
        "personal": "friendly but professional",
        "unknown": "polite and professional",
        "executive": "concise and direct",
    }

    structure_templates = {
        "general": """
**Professional Email Structure:**

1. **Subject Line**: Clear, specific, actionable
   - Example: "Request for Q4 Budget Review Meeting"
   
2. **Greeting**: 
   - Formal: "Dear [Name]," or "Hello [Name],"
   - Professional: "Hi [Name],"
   
3. **Opening** (1-2 sentences):
   - State purpose immediately
   - Provide context if needed
   
4. **Body** (2-3 paragraphs max):
   - Main points with clear structure
   - Use bullet points for multiple items
   - Include specific details and deadlines
   
5. **Call to Action**:
   - Clearly state what you need
   - Include timeline/deadline
   
6. **Professional Closing**:
   - "Best regards," "Thank you," or "Sincerely,"
   - Your full name and title
        """,
        "request": """
**Request Email Template:**

1. **Subject**: "Request: [Specific Action Needed]"

2. **Opening**: State your request clearly in first sentence

3. **Context**: Brief background (2-3 sentences max)

4. **Specific Ask**: 
   - Exactly what you need
   - Why it's needed
   - When it's needed

5. **Make it Easy**: 
   - Provide options if applicable
   - Offer to follow up
   - Thank them in advance
        """,
        "meeting": """
**Meeting Request Structure:**

1. **Subject**: "Meeting Request: [Topic] - [Proposed Date/Time]"

2. **Purpose**: Clear meeting objective

3. **Details**:
   - Duration: [X minutes/hours]
   - Attendees: [List key participants]
   - Location/Link: [In-person/virtual details]
   
4. **Agenda**:
   - Key discussion points
   - Desired outcomes
   
5. **Alternatives**: Offer 2-3 time options

6. **Preparation**: Any materials to review beforehand
        """,
    }

    urgency_notes = {
        "low": "Take time to craft thoughtfully",
        "normal": "Standard professional timeline",
        "high": "Mention priority in subject line",
        "urgent": "Call attention to urgency appropriately - avoid overuse",
    }

    tone = tone_guidance.get(recipient_relationship, "professional and respectful")
    template = structure_templates.get(email_type, structure_templates["general"])
    urgency_note = urgency_notes.get(urgency, "Standard professional timeline")

    return f"""
# Professional Email Composition Guide

## Email Type: {email_type.title()}
## Recipient Relationship: {recipient_relationship.title()}  
## Urgency: {urgency.title()}

**Recommended Tone**: {tone}
**Timing Guidance**: {urgency_note}

{template}

## Best Practices:
- Keep emails under 150 words when possible
- Use active voice
- Proofread before sending
- Include clear next steps
- Consider recipient's time zone

## Security Reminders:
- Use BCC for multiple external recipients
- Double-check recipient addresses
- Avoid sensitive information in subject lines
    """


@mcp.prompt()
def follow_up_email_generator(
    original_context: str,
    time_since_last: str = "1 week",
    follow_up_type: str = "polite_reminder",
) -> str:
    """Generate appropriate follow-up emails based on context.

    Args:
        original_context: Brief description of original email/request
        time_since_last: How long since last communication (e.g., "3 days", "1 week", "2 weeks")
        follow_up_type: Type of follow-up (polite_reminder, status_check, escalation, thank_you)
    """

    templates = {
        "polite_reminder": f"""
# Polite Follow-Up Email

**Context**: {original_context}
**Time Elapsed**: {time_since_last}

## Template:

**Subject**: "Following up: [Original Subject]"

Hi [Name],

I hope this email finds you well. I wanted to follow up on my [email/request] from {time_since_last} ago regarding {original_context}.

I understand you have a busy schedule, and I don't want this to get lost in your inbox. When you have a moment, I'd appreciate any updates you might have.

[Optional: Restate key ask or deadline if relevant]

Thank you for your time and consideration.

Best regards,
[Your name]
        """,
        "status_check": f"""
# Status Check Follow-Up

**Context**: {original_context}

## Template:

**Subject**: "Status Update: [Original Subject]"

Hi [Name],

I hope you're doing well. I'm following up on {original_context} to check on the current status.

Could you please provide a brief update on:
- Current progress
- Any challenges or blockers
- Revised timeline if needed

I'm happy to discuss this further or provide any additional information that might be helpful.

Thank you,
[Your name]
        """,
        "escalation": f"""
# Escalation Follow-Up (Use Carefully)

**Context**: {original_context}
**⚠️ Warning**: Only use after multiple polite attempts

## Template:

**Subject**: "Urgent: Follow-up needed on [Original Subject]"

Hi [Name],

I've reached out a few times regarding {original_context} but haven't received a response. 

This matter requires attention because [brief explanation of impact/deadline].

I understand priorities shift, but I need to understand the status so I can plan accordingly. Could we schedule a brief call this week to discuss?

I'm available [provide specific times] and am happy to work around your schedule.

Thank you,
[Your name]
        """,
    }

    return templates.get(follow_up_type, templates["polite_reminder"])


@mcp.prompt()
def meeting_request_composer(
    meeting_purpose: str,
    duration_minutes: int = 30,
    attendee_count: int = 2,
    meeting_type: str = "discussion",
) -> str:
    """Compose professional meeting requests with all necessary details.

    Args:
        meeting_purpose: Main reason for the meeting
        duration_minutes: Expected duration in minutes (15, 30, 60, etc.)
        attendee_count: Number of expected attendees
        meeting_type: Type of meeting (discussion, presentation, decision, brainstorm, check_in)
    """

    templates = {
        "discussion": f"""
# Discussion Meeting Request

**Purpose**: {meeting_purpose}
**Duration**: {duration_minutes} minutes
**Attendees**: {attendee_count} people

## Email Template:

**Subject**: "Meeting Request: {meeting_purpose} - [Propose 2-3 specific time slots]"

Hi [Name(s)],

I'd like to schedule a {duration_minutes}-minute meeting to discuss {meeting_purpose}.

**Proposed Times** (please let me know what works best):
- Option 1: [Day, Date] at [Time] 
- Option 2: [Day, Date] at [Time]
- Option 3: [Day, Date] at [Time]

**Agenda**:
- [Key discussion point 1]
- [Key discussion point 2] 
- [Key discussion point 3]
- Next steps and action items

**Meeting Details**:
- Location: [Conference room/Virtual link]
- Duration: {duration_minutes} minutes
- Attendees: [List names if multiple people]

**Preparation**: 
- [Any materials to review beforehand]
- [Questions to consider in advance]

Please confirm which time works for you, or suggest alternatives if none of these fit your schedule.

Thank you,
[Your name]
        """,
        "decision": f"""
# Decision-Making Meeting

**Purpose**: {meeting_purpose}

## Template:

**Subject**: "Decision Needed: {meeting_purpose} - Meeting Request"

Hi [Name(s)],

I'm requesting a {duration_minutes}-minute meeting to make a decision regarding {meeting_purpose}.

**Background**: [2-3 sentence context]

**Decision Required**: [Specific decision to be made]

**Options to Consider**:
1. [Option 1 with brief pros/cons]
2. [Option 2 with brief pros/cons] 
3. [Option 3 if applicable]

**Information Needed**:
- [Key data points or input needed]
- [Stakeholder perspectives to consider]

**Proposed Meeting Times**: [List 3 options]

**Attendees**: [Decision makers and key stakeholders]

Please come prepared with your thoughts on the options above. The goal is to reach a decision by the end of our meeting.

Best regards,
[Your name]
        """,
    }

    return templates.get(meeting_type, templates["discussion"])


@mcp.prompt()
def draft_strategy_advisor(
    email_purpose: str,
    urgency: str = "normal",
    stakeholder_count: int = 1,
    complexity: str = "medium",
) -> str:
    """Advise whether to save as draft or send immediately based on email characteristics.

    Args:
        email_purpose: Main purpose of the email (request, announcement, sensitive_topic, routine_update)
        urgency: How urgent the email is (low, normal, high, urgent)
        stakeholder_count: Number of people affected by or involved in the email
        complexity: Complexity of the topic (simple, medium, complex)
    """

    draft_scenarios = {
        "high_risk": {
            "triggers": [
                "sensitive",
                "legal",
                "budget",
                "layoff",
                "termination",
                "complaint",
            ],
            "advice": "**RECOMMENDATION: Save as Draft**\n\nThis appears to be a high-risk communication. Consider:\n- Having a colleague review before sending\n- Legal/HR review if applicable\n- Sleeping on it overnight\n- Alternative communication methods (call/meeting)",
        },
        "complex_multi_stakeholder": {
            "advice": "**RECOMMENDATION: Save as Draft**\n\nFor complex topics with multiple stakeholders:\n- Review for clarity and completeness\n- Consider if all stakeholders need same message\n- Check if anyone should be added/removed from recipients\n- Verify timing is appropriate for all recipients"
        },
        "urgent_simple": {
            "advice": "**RECOMMENDATION: Send Immediately**\n\nFor urgent, straightforward communications:\n- Quick proofread for typos\n- Confirm recipients are correct\n- Send promptly to maintain urgency"
        },
        "routine_update": {
            "advice": "**RECOMMENDATION: Send After Review**\n\nFor routine communications:\n- Quick review for completeness\n- Ensure subject line is clear\n- Check if timing is appropriate\n- Send when ready"
        },
    }

    # Determine recommendation based on inputs
    if any(
        trigger in email_purpose.lower()
        for trigger in draft_scenarios["high_risk"]["triggers"]
    ):
        recommendation = draft_scenarios["high_risk"]["advice"]
    elif complexity == "complex" and stakeholder_count > 3:
        recommendation = draft_scenarios["complex_multi_stakeholder"]["advice"]
    elif urgency in ["high", "urgent"] and complexity == "simple":
        recommendation = draft_scenarios["urgent_simple"]["advice"]
    else:
        recommendation = draft_scenarios["routine_update"]["advice"]

    checklist = {
        "before_sending": [
            "✅ Subject line clearly describes the content",
            "✅ Recipients are correct and complete",
            "✅ Tone is appropriate for all recipients",
            "✅ Call-to-action is clear (if needed)",
            "✅ Attachments are included (if referenced)",
            "✅ No sensitive information exposed inappropriately",
            "✅ Grammar and spelling checked",
        ],
        "draft_review": [
            "⏱️ Wait at least 15 minutes before final review",
            "👁️ Read from recipient's perspective",
            "🎯 Verify the main message is clear",
            "📱 Consider how it looks on mobile",
            "🔄 Check if a simpler approach would work better",
            "👥 Consider if this should be a meeting/call instead",
        ],
    }

    timing_advice = {
        "urgent": "Send within 1 hour if truly urgent",
        "high": "Send within 4 hours, but review carefully first",
        "normal": "Send within 24 hours after appropriate review",
        "low": "Can wait for optimal timing (avoid late nights/weekends)",
    }

    return f"""
# Draft Strategy Recommendation

## Email Analysis:
- **Purpose**: {email_purpose}
- **Urgency**: {urgency}
- **Stakeholders**: {stakeholder_count} people
- **Complexity**: {complexity}

{recommendation}

## Pre-Send Checklist:
{chr(10).join(checklist["before_sending"])}

## Draft Review Process:
{chr(10).join(checklist["draft_review"])}

## Timing Guidance:
**{urgency.title()} Priority**: {timing_advice.get(urgency, timing_advice["normal"])}

## Alternative Communication Methods to Consider:
- **Phone call**: For urgent matters or sensitive topics
- **Video meeting**: For complex discussions needing back-and-forth
- **In-person**: For highly sensitive or relationship-critical conversations
- **Instant message**: For quick questions or updates (if available)

Remember: When in doubt, saving as draft and reviewing later is almost always the safer choice.
    """


@mcp.prompt()
def email_review_checklist(
    email_type: str = "general",
    recipient_type: str = "internal",
    has_attachments: bool = False,
) -> str:
    """Provide comprehensive checklist for reviewing emails before sending.

    Args:
        email_type: Type of email (general, meeting_request, urgent, announcement, sensitive)
        recipient_type: Type of recipients (internal, external, mixed, executive)
        has_attachments: Whether email includes attachments
    """

    base_checklist = [
        "📝 **Content Review**:",
        "   ✅ Subject line is clear and specific",
        "   ✅ Main message is stated upfront",
        "   ✅ All necessary information is included",
        "   ✅ Call-to-action is clear (if needed)",
        "   ✅ Tone is appropriate for recipients",
        "",
        "👥 **Recipients**:",
        "   ✅ All necessary recipients included",
        "   ✅ No unnecessary recipients",
        "   ✅ Used BCC for external bulk recipients (if applicable)",
        "   ✅ Double-checked email addresses",
        "",
        "🔤 **Language & Format**:",
        "   ✅ Grammar and spelling checked",
        "   ✅ Professional formatting (bullets, paragraphs)",
        "   ✅ No ALL CAPS or excessive punctuation",
        "   ✅ Appropriate greeting and closing",
        "",
        "🔒 **Security & Privacy**:",
        "   ✅ No sensitive information in subject line",
        "   ✅ Appropriate level of confidentiality",
        "   ✅ No accidental reply-all risks",
        "   ✅ Checked for auto-complete errors",
    ]

    # Add attachment-specific items
    if has_attachments:
        attachment_items = [
            "",
            "📎 **Attachments**:",
            "   ✅ All referenced attachments are attached",
            "   ✅ Attachments are the correct versions",
            "   ✅ File names are professional and clear",
            "   ✅ File sizes are reasonable",
            "   ✅ Attachments scanned for malware",
            "   ✅ Sensitive files are password-protected (if needed)",
        ]
        base_checklist.extend(attachment_items)

    # Add type-specific items
    type_specific = {
        "meeting_request": [
            "",
            "📅 **Meeting-Specific**:",
            "   ✅ Date, time, and duration specified",
            "   ✅ Time zone clarified (if needed)",
            "   ✅ Location or meeting link included",
            "   ✅ Agenda or purpose stated",
            "   ✅ Preparation requirements mentioned",
            "   ✅ Multiple time options provided (if requesting)",
        ],
        "urgent": [
            "",
            "⚡ **Urgent Email**:",
            "   ✅ Urgency is genuinely justified",
            "   ✅ Deadline or time-sensitivity explained",
            "   ✅ Consider if phone call would be better",
            "   ✅ Marked urgent/priority appropriately",
            "   ✅ Backup plan mentioned (if applicable)",
        ],
        "announcement": [
            "",
            "📢 **Announcement**:",
            "   ✅ Key information highlighted clearly",
            "   ✅ Effective date/timeline specified",
            "   ✅ Next steps or actions outlined",
            "   ✅ Contact for questions identified",
            "   ✅ Impact on recipients addressed",
        ],
        "sensitive": [
            "",
            "⚠️  **Sensitive Content**:",
            "   ✅ Recipients have legitimate need to know",
            "   ✅ Confidentiality level appropriate",
            "   ✅ Legal/compliance review completed (if needed)",
            "   ✅ Consider if email is appropriate medium",
            "   ✅ Potential misunderstandings addressed",
        ],
    }

    if email_type in type_specific:
        base_checklist.extend(type_specific[email_type])

    # Add recipient-specific items
    recipient_specific = {
        "external": [
            "",
            "🌐 **External Recipients**:",
            "   ✅ Company branding/signature included",
            "   ✅ Professional email address used",
            "   ✅ Industry jargon minimized",
            "   ✅ Legal disclaimers included (if required)",
            "   ✅ Contact information provided",
        ],
        "executive": [
            "",
            "👔 **Executive Recipients**:",
            "   ✅ Message is concise and action-oriented",
            "   ✅ Key points summarized upfront",
            "   ✅ Supporting details in appendix/attachment",
            "   ✅ Clear recommendations provided",
            "   ✅ Next steps explicitly stated",
        ],
        "mixed": [
            "",
            "👥 **Mixed Recipients**:",
            "   ✅ Content appropriate for all recipient types",
            "   ✅ External recipients' privacy protected",
            "   ✅ Internal jargon explained or avoided",
            "   ✅ Confidentiality level appropriate for least secure recipient",
        ],
    }

    if recipient_type in recipient_specific:
        base_checklist.extend(recipient_specific[recipient_type])

    final_steps = [
        "",
        "🚀 **Final Review**:",
        "   ✅ Read email from recipient's perspective",
        "   ✅ Checked email on mobile preview (if possible)",
        "   ✅ Timing is appropriate for recipients",
        "   ✅ Considered if response is actually needed",
        "",
        "💡 **Pro Tips**:",
        "   • Wait 5-10 minutes after writing before final review",
        "   • Read out loud to catch awkward phrasing",
        "   • Ask: 'Would I want to receive this email?'",
        "   • Consider the recipient's current workload/priorities",
    ]

    base_checklist.extend(final_steps)

    return f"""
# Email Review Checklist

**Email Type**: {email_type.replace("_", " ").title()}
**Recipients**: {recipient_type.replace("_", " ").title()}
**Has Attachments**: {"Yes" if has_attachments else "No"}

{chr(10).join(base_checklist)}

---

**Remember**: A few extra minutes of review can save hours of clarification emails and prevent misunderstandings!
    """


def get_authenticated_client() -> Optional[GmailClient]:
    """Get authenticated Gmail client for current user."""
    credentials = auth_manager.get_credentials()
    if not credentials:
        return None
    return GmailClient(credentials)


@mcp.tool()
async def send_email(
    to: str,
    subject: str,
    body: str,
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
    html_body: Optional[str] = None,
    ctx=None,
) -> EmailResponse:
    """Send an email via Gmail.

    Args:
        to: Recipient email address
        subject: Email subject line
        body: Email body (plain text)
        cc: CC recipients (optional)
        bcc: BCC recipients (optional)
        html_body: HTML version of email body (optional)
    """
    client = get_authenticated_client()
    if not client:
        raise Exception(
            "No authenticated user. Please login first with: gmail-mcp --login"
        )

    if ctx:
        await ctx.info(f"Sending email to {to}")

    try:
        # Validate email request
        email_req = EmailRequest(
            to=to, subject=subject, body=body, cc=cc, bcc=bcc, html_body=html_body
        )

        result = client.send_email(
            to=email_req.to,
            subject=email_req.subject,
            body=email_req.body,
            cc=email_req.cc,
            bcc=email_req.bcc,
            html_body=email_req.html_body,
        )

        if ctx:
            await ctx.info(f"Email sent successfully with ID: {result['id']}")

        return EmailResponse(**result)

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to send email: {str(e)}")
        raise Exception(f"Failed to send email: {str(e)}")


@mcp.tool()
async def create_draft(
    to: str,
    subject: str,
    body: str,
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
    html_body: Optional[str] = None,
    ctx=None,
) -> EmailResponse:
    """Create an email draft.

    Args:
        to: Recipient email address
        subject: Email subject line
        body: Email body (plain text)
        cc: CC recipients (optional)
        bcc: BCC recipients (optional)
        html_body: HTML version of email body (optional)
    """
    client = get_authenticated_client()
    if not client:
        raise Exception(
            "No authenticated user. Please login first with: gmail-mcp --login"
        )

    if ctx:
        await ctx.info(f"Creating draft for {to}")

    try:
        draft_req = DraftRequest(
            to=to, subject=subject, body=body, cc=cc, bcc=bcc, html_body=html_body
        )

        result = client.create_draft(
            to=draft_req.to,
            subject=draft_req.subject,
            body=draft_req.body,
            cc=draft_req.cc,
            bcc=draft_req.bcc,
            html_body=draft_req.html_body,
        )

        if ctx:
            await ctx.info(f"Draft created with ID: {result['id']}")

        return EmailResponse(**result)

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to create draft: {str(e)}")
        raise Exception(f"Failed to create draft: {str(e)}")


@mcp.tool()
async def send_draft(draft_id: str, ctx=None) -> EmailResponse:
    """Send an existing email draft.

    Args:
        draft_id: ID of the draft to send
    """
    client = get_authenticated_client()
    if not client:
        raise Exception(
            "No authenticated user. Please login first with: gmail-mcp --login"
        )

    if ctx:
        await ctx.info(f"Sending draft {draft_id}")

    try:
        result = client.send_draft(draft_id)

        if ctx:
            await ctx.info(f"Draft sent with message ID: {result['id']}")

        return EmailResponse(**result)

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to send draft: {str(e)}")
        raise Exception(f"Failed to send draft: {str(e)}")


@mcp.tool()
async def list_drafts(max_results: int = 10, ctx=None) -> List[DraftInfo]:
    """List email drafts.

    Args:
        max_results: Maximum number of drafts to return (default: 10)
    """
    client = get_authenticated_client()
    if not client:
        raise Exception(
            "No authenticated user. Please login first with: gmail-mcp --login"
        )

    if ctx:
        await ctx.info(f"Listing up to {max_results} drafts")

    try:
        drafts = client.list_drafts(max_results)
        result = [DraftInfo(**draft) for draft in drafts]

        if ctx:
            await ctx.info(f"Found {len(result)} drafts")

        return result

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to list drafts: {str(e)}")
        raise Exception(f"Failed to list drafts: {str(e)}")


@mcp.tool()
async def get_user_info(ctx=None) -> UserInfo:
    """Get current authenticated user information."""
    client = get_authenticated_client()
    if not client:
        raise Exception(
            "No authenticated user. Please login first with: gmail-mcp --login"
        )

    try:
        user_info = client.get_user_info()
        result = UserInfo(**user_info)

        if ctx:
            await ctx.info(f"Current user: {result.email}")

        return result

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to get user info: {str(e)}")
        raise Exception(f"Failed to get user info: {str(e)}")


# Resource access tools
@mcp.resource("template://html_email/{template_name}")
def get_html_template(template_name: str) -> str:
    """Get HTML email template by name.

    Available templates: professional_announcement, meeting_invitation, project_update, newsletter
    """
    template = HTML_EMAIL_TEMPLATES.get(template_name)
    if not template:
        available = list(HTML_EMAIL_TEMPLATES.keys())
        raise ValueError(
            f"Template '{template_name}' not found. Available: {', '.join(available)}"
        )
    return template


@mcp.resource("template://signature/{signature_type}")
def get_signature_resource(signature_type: str) -> str:
    """Get email signature template by type.

    Available types: standard_professional, detailed_professional, consultant_freelancer,
    sales_business_development, executive_minimal, startup_founder, academic_researcher,
    creative_professional, nonprofit_social_impact, tech_developer, legal_professional,
    healthcare_medical, holiday_seasonal
    """
    return get_signature_template(signature_type)


@mcp.resource("guidelines://security/{category}")
def get_security_resource(category: str) -> dict:
    """Get email security guidelines by category.

    Available categories: recipient_management, sensitive_information, phishing_prevention,
    attachment_security, compliance_legal, access_control, external_communication
    """
    guidelines = get_security_guidelines_by_category(category)
    if not guidelines:
        available = [
            "recipient_management",
            "sensitive_information",
            "phishing_prevention",
            "attachment_security",
            "compliance_legal",
            "access_control",
            "external_communication",
        ]
        raise ValueError(
            f"Category '{category}' not found. Available: {', '.join(available)}"
        )
    return guidelines


@mcp.resource("guidelines://etiquette/{category}")
def get_etiquette_resource(category: str) -> dict:
    """Get email etiquette guidelines by category.

    Available categories: tone_and_language, timing_and_response, structure_and_formatting,
    professional_courtesy, cultural_considerations, meeting_email_etiquette
    """
    guidelines = EMAIL_ETIQUETTE_GUIDELINES.get(category)
    if not guidelines:
        available = list(EMAIL_ETIQUETTE_GUIDELINES.keys())
        raise ValueError(
            f"Category '{category}' not found. Available: {', '.join(available)}"
        )
    return guidelines


@mcp.tool()
async def get_subject_line_help(
    email_type: str = "general", industry: str = None, ctx=None
) -> dict:
    """Get subject line suggestions and best practices.

    Args:
        email_type: Type of email (action_required, meeting_requests, status_updates, etc.)
        industry: Optional industry for specialized templates (sales, marketing, hr, etc.)
    """
    try:
        suggestions = get_subject_line_suggestions(email_type, industry)

        if ctx:
            await ctx.info(
                f"Generated subject line suggestions for {email_type} emails"
            )

        return suggestions

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to get subject line help: {str(e)}")
        raise Exception(f"Failed to get subject line help: {str(e)}")


@mcp.tool()
async def validate_subject_line_tool(subject: str, ctx=None) -> dict:
    """Validate a subject line against best practices.

    Args:
        subject: Subject line to validate
    """
    try:
        validation = validate_subject_line(subject)

        if ctx:
            await ctx.info(f"Validated subject line: '{subject}'")

        return validation

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to validate subject line: {str(e)}")
        raise Exception(f"Failed to validate subject line: {str(e)}")


@mcp.tool()
async def get_email_templates(template_type: str = "html", ctx=None) -> dict:
    """Get available email templates.

    Args:
        template_type: Type of templates to retrieve (html, signature)
    """
    try:
        if template_type == "html":
            templates = {
                name: "HTML email template" for name in HTML_EMAIL_TEMPLATES.keys()
            }
        elif template_type == "signature":
            templates = {
                name: "Email signature template" for name in EMAIL_SIGNATURES.keys()
            }
        else:
            raise ValueError(
                f"Unknown template type: {template_type}. Use 'html' or 'signature'"
            )

        if ctx:
            await ctx.info(f"Retrieved {len(templates)} {template_type} templates")

        return {
            "template_type": template_type,
            "available_templates": templates,
            "usage": "Use get_html_template() or get_signature_template() to retrieve specific templates",
        }

    except Exception as e:
        if ctx:
            await ctx.error(f"Failed to get templates: {str(e)}")
        raise Exception(f"Failed to get templates: {str(e)}")

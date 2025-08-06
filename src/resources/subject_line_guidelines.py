"""Subject line guidelines and proven patterns for professional emails."""

SUBJECT_LINE_PATTERNS = {
    "action_required": {
        "description": "When you need someone to take specific action",
        "patterns": [
            "Action Required: [Specific Action] by [Date]",
            "Please Review: [Document/Proposal Name] by [Deadline]",
            "Decision Needed: [Topic] - Response needed by [Date]",
            "Approval Required: [Item] - [Brief Context]",
            "Your Input Needed: [Topic] by [Date]",
        ],
        "examples": [
            "Action Required: Approve Q4 Budget by Friday",
            "Please Review: Marketing Proposal by EOD Tuesday",
            "Decision Needed: New Hire Salary - Response needed by Monday",
        ],
    },
    "meeting_requests": {
        "description": "For scheduling meetings and appointments",
        "patterns": [
            "Meeting Request: [Topic] - [Proposed Time]",
            "Schedule Request: [Purpose] - [Duration]",
            "Quick Call: [Topic] - [Timeframe]",
            "Calendar Invite: [Event] on [Date]",
            "[Duration] Meeting: [Topic] - [Urgency Level]",
        ],
        "examples": [
            "Meeting Request: Q4 Planning - Next Tuesday 2pm",
            "15-minute Call: Project Status Update - This Week",
            "Calendar Invite: Team Sync on Thursday 10am",
        ],
    },
    "status_updates": {
        "description": "For project updates and progress reports",
        "patterns": [
            "[Project Name] Update: [Key Milestone/Status]",
            "Weekly Update: [Team/Project] - [Date]",
            "Status Report: [Topic] - [Current Phase]",
            "Progress Update: [Project] - [Percent Complete]",
            "[Frequency] Check-in: [Topic]",
        ],
        "examples": [
            "Website Redesign Update: Phase 1 Complete",
            "Weekly Update: Sales Team - Week of March 15th",
            "Progress Update: Database Migration - 75% Complete",
        ],
    },
    "requests": {
        "description": "When asking for information, help, or resources",
        "patterns": [
            "Request: [Specific Item] for [Purpose]",
            "Quick Question: [Topic]",
            "Need: [Resource/Information] by [Date]",
            "Help Requested: [Specific Issue]",
            "Information Request: [Topic] - [Context]",
        ],
        "examples": [
            "Request: Budget Breakdown for Client Presentation",
            "Quick Question: Vendor Contact Information",
            "Need: Logo Files by Tomorrow Morning",
        ],
    },
    "follow_ups": {
        "description": "For following up on previous communications",
        "patterns": [
            "Follow-up: [Original Subject/Topic]",
            "Checking In: [Topic] from [Time Reference]",
            "Re: [Original Subject] - Follow-up",
            "Status Check: [Topic] from [Date]",
            "Following up on our [Meeting/Conversation] about [Topic]",
        ],
        "examples": [
            "Follow-up: Proposal Discussion from Last Tuesday",
            "Checking In: Contract Review from March 10th",
            "Status Check: Invoice Payment from February",
        ],
    },
    "announcements": {
        "description": "For sharing news, updates, or important information",
        "patterns": [
            "Announcement: [News/Update]",
            "Important Update: [Topic]",
            "News: [Brief Summary]",
            "[Company/Team] Update: [Key Information]",
            "FYI: [Important Information]",
        ],
        "examples": [
            "Announcement: New Office Location Opening",
            "Important Update: Policy Changes Effective April 1st",
            "Team Update: Quarterly Results and Next Steps",
        ],
    },
    "urgent": {
        "description": "For time-sensitive communications (use sparingly)",
        "patterns": [
            "URGENT: [Brief Description] - [Deadline]",
            "Time Sensitive: [Topic] - [Action Needed]",
            "Priority: [Issue] - Immediate Attention Required",
            "ASAP: [Request] - [Brief Context]",
            "Critical: [Issue Description]",
        ],
        "examples": [
            "URGENT: Server Down - IT Response Needed",
            "Time Sensitive: Client Contract - Signature by 5pm",
            "Priority: Security Breach - Immediate Action Required",
        ],
        "warning": "Use urgent markers only when truly urgent. Overuse diminishes impact.",
    },
    "informational": {
        "description": "For sharing information without requiring action",
        "patterns": [
            "FYI: [Information Summary]",
            "Update: [Topic] - No Action Required",
            "Heads Up: [Upcoming Event/Change]",
            "Info: [Brief Description]",
            "For Your Awareness: [Topic]",
        ],
        "examples": [
            "FYI: Office Closure Next Friday",
            "Update: Project Timeline - No Action Required",
            "Heads Up: System Maintenance This Weekend",
        ],
    },
    "thank_you": {
        "description": "For expressing gratitude and appreciation",
        "patterns": [
            "Thank you: [Specific Action/Help]",
            "Appreciation: [What You're Grateful For]",
            "Thanks for [Specific Action] - [Brief Context]",
            "Grateful: [Reason] - [Next Steps if Any]",
            "Thank You Note: [Occasion/Help]",
        ],
        "examples": [
            "Thank you: Great Presentation Yesterday",
            "Thanks for the Quick Response - Project Approved",
            "Appreciation: Your Help with the Client Meeting",
        ],
    },
}

SUBJECT_LINE_BEST_PRACTICES = {
    "length": {
        "recommended": "30-50 characters",
        "mobile_friendly": "Under 25-30 characters for mobile preview",
        "reason": "Longer subjects get truncated in email clients",
    },
    "clarity": [
        "Be specific and descriptive",
        "Front-load important keywords",
        "Avoid vague terms like 'Quick question' without context",
        "Include key details like dates, names, or topics",
    ],
    "formatting": [
        "Use title case or sentence case consistently",
        "Avoid excessive punctuation (!!!, ???)",
        "Use colons to separate topic from details",
        "Consider using brackets for categories [URGENT], [FYI]",
    ],
    "personalization": [
        "Include recipient's name for important emails",
        "Reference shared context or previous conversations",
        "Use 'You' to make it personal when appropriate",
        "Mention specific projects or deadlines",
    ],
    "action_words": [
        "Use strong action verbs: Review, Approve, Complete, Discuss",
        "Be direct about what you need: 'Need your input' vs 'Touching base'",
        "Include deadlines: 'by Friday', 'ASAP', 'before meeting'",
        "Specify the outcome: 'for client presentation', 'to finalize contract'",
    ],
    "avoid": [
        "ALL CAPS (unless truly urgent and used sparingly)",
        "Spam trigger words: Free, Limited time, Act now",
        "Vague subjects: 'Hi', 'Important', 'Quick question'",
        "Re: chains that lose original context",
        "Excessive emoji (one or two max for internal emails)",
    ],
}

SUBJECT_LINE_TEMPLATES_BY_INDUSTRY = {
    "sales": [
        "Proposal: [Client Name] - [Solution] for [Need]",
        "Follow-up: [Meeting Topic] with [Client]",
        "Quote Request: [Product/Service] for [Company]",
        "Demo Scheduled: [Product] for [Client] on [Date]",
        "Contract Ready: [Deal Name] - Next Steps",
    ],
    "marketing": [
        "Campaign Results: [Campaign Name] - [Key Metric]",
        "Content Review: [Asset Name] - Deadline [Date]",
        "Marketing Plan: [Project] - Q[Quarter] Strategy",
        "Brand Guidelines: [Update/New] for [Department]",
        "Event Planning: [Event Name] - [Current Status]",
    ],
    "hr": [
        "Interview Scheduled: [Candidate Name] for [Position]",
        "Policy Update: [Policy Name] - Effective [Date]",
        "Training Session: [Topic] on [Date] at [Time]",
        "Performance Review: [Employee] - [Review Period]",
        "Benefits Update: [Change Description] - Action Required",
    ],
    "finance": [
        "Budget Review: [Department/Project] - [Time Period]",
        "Invoice Approval: [Vendor] - [Amount] - Due [Date]",
        "Financial Report: [Period] - Key Highlights",
        "Expense Policy: [Update/Reminder] - Effective [Date]",
        "Audit Preparation: [Area] - Documents Needed by [Date]",
    ],
    "it": [
        "System Maintenance: [System] - [Date] from [Time] to [Time]",
        "Security Alert: [Issue] - Action Required by [Date]",
        "Software Update: [Application] - Version [Number]",
        "Help Ticket: #[Number] - [Brief Description]",
        "Access Request: [System/Resource] for [User]",
    ],
    "project_management": [
        "Project Update: [Project Name] - [Current Phase]",
        "Milestone Reached: [Project] - [Milestone Name]",
        "Resource Request: [Project] needs [Resource] by [Date]",
        "Risk Assessment: [Project] - [Priority Level]",
        "Sprint Review: [Team] - Week of [Date]",
    ],
}


def get_subject_line_suggestions(email_type: str, industry: str = None) -> dict:
    """Get subject line suggestions based on email type and industry.

    Args:
        email_type: Type of email (action_required, meeting_requests, etc.)
        industry: Optional industry for specialized templates

    Returns:
        Dictionary with patterns, examples, and best practices
    """
    suggestions = {
        "patterns": SUBJECT_LINE_PATTERNS.get(email_type, {}).get("patterns", []),
        "examples": SUBJECT_LINE_PATTERNS.get(email_type, {}).get("examples", []),
        "best_practices": SUBJECT_LINE_BEST_PRACTICES,
    }

    if industry and industry in SUBJECT_LINE_TEMPLATES_BY_INDUSTRY:
        suggestions["industry_templates"] = SUBJECT_LINE_TEMPLATES_BY_INDUSTRY[industry]

    return suggestions


def validate_subject_line(subject: str) -> dict:
    """Validate a subject line against best practices.

    Args:
        subject: Subject line to validate

    Returns:
        Dictionary with validation results and suggestions
    """
    results = {
        "length_check": len(subject) <= 50,
        "mobile_friendly": len(subject) <= 30,
        "has_specific_content": True,  # Would need more sophisticated analysis
        "suggestions": [],
    }

    if len(subject) > 50:
        results["suggestions"].append(
            "Consider shortening - over 50 characters may be truncated"
        )

    if len(subject) > 30:
        results["suggestions"].append("May be truncated on mobile devices")

    if subject.isupper():
        results["suggestions"].append("Avoid ALL CAPS - use normal case")

    if not any(
        word in subject.lower()
        for word in ["by", "for", ":", "-", "request", "update", "meeting"]
    ):
        results["suggestions"].append(
            "Consider adding context words like 'by [date]', 'for [purpose]', etc."
        )

    return results

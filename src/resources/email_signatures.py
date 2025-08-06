"""Professional email signature templates."""

EMAIL_SIGNATURES = {
    "standard_professional": """
Best regards,
[Full Name]
[Job Title]
[Company Name]
[Phone Number]
[Email Address]
[Company Website]
    """,
    "detailed_professional": """
[Full Name]
[Job Title] | [Department]
[Company Name]

📞 Direct: [Phone Number]
📱 Mobile: [Mobile Number]  
✉️ Email: [Email Address]
🌐 Website: [Company Website]
📍 [Office Address]

[Company Tagline or Brief Value Proposition]
    """,
    "consultant_freelancer": """
Best regards,

[Full Name]
[Professional Title/Expertise]

📧 [Email Address]
📱 [Phone Number]
💼 [Portfolio/Website URL]
🔗 [LinkedIn Profile URL]

[Brief value proposition or specialty]
[Call-to-action like "Let's discuss your next project!"]
    """,
    "sales_business_development": """
[Full Name]
[Title] | [Company Name]

Ready to help you [value proposition]

📞 [Phone Number]
✉️ [Email Address] 
🌐 [Website]
📅 [Calendar Link] - Schedule a call

Follow us: [Social Media Links]

P.S. [Relevant PS message or current promotion]
    """,
    "executive_minimal": """
[Full Name]
[Title]
[Company Name]

[Phone] | [Email]
[Website]
    """,
    "startup_founder": """
[Full Name]
Founder & [Title]
[Company Name]

Building [brief company mission]

📧 [Email]
📱 [Phone]  
🚀 [Company Website]
🐦 [Twitter Handle]

"[Inspirational quote or company motto]"

P.S. We're hiring! Check out [careers page link]
    """,
    "academic_researcher": """
[Full Name], [Degrees/Credentials]
[Title/Position]
[Institution/University Name]
[Department]

📧 [Email Address]
📞 [Phone Number]
🏛️ [Institution Website]
📚 [Research Profile/Google Scholar]
🔬 Research Focus: [Brief research area description]

[University/Institution Address]
    """,
    "creative_professional": """
[Full Name]
[Creative Title] ✨

Creating [type of work] that [impact/goal]

📧 [Email]
🎨 Portfolio: [Website/Portfolio URL]
📱 [Phone]
📸 Instagram: [@handle]

"[Creative motto or favorite quote]"

Available for: [Types of projects/collaborations]
    """,
    "nonprofit_social_impact": """
[Full Name]
[Title]
[Organization Name]

Making a difference through [mission focus]

📧 [Email Address]
📞 [Phone Number]
🌍 [Website URL]
🤝 Get involved: [Volunteer/Donation Link]

[Organization Address]

"[Mission statement or inspirational quote]"

Tax ID: [If relevant for donations]
    """,
    "tech_developer": """
[Full Name]
[Role] @ [Company] | [Tech Stack/Specialization]

Building [what you build] with [technologies]

💻 GitHub: [GitHub Profile]
📧 [Email Address]
🌐 [Personal Website/Blog]
💼 [LinkedIn Profile]

Always learning: [Current learning focus]
Open source contributor: [Key projects]

"Code is poetry in motion" 🚀
    """,
    "legal_professional": """
[Full Name], [Credentials]
[Title]
[Law Firm/Organization Name]

📧 [Email Address]
📞 [Direct Phone]
📠 [Fax Number]
🏛️ [Website]

[Office Address]
[City, State ZIP Code]

⚖️ Practice Areas: [Areas of expertise]

CONFIDENTIALITY NOTICE: This email and any attachments may contain attorney-client privileged and confidential information. If you are not the intended recipient, please notify the sender and delete this message.
    """,
    "healthcare_medical": """
[Full Name], [Credentials]
[Title/Specialization]  
[Healthcare Facility/Practice Name]

📧 [Email Address]
📞 [Phone Number]
🏥 [Facility Website]
📅 Schedule: [Appointment Link]

[Facility Address]

[Board Certifications]
[Insurance accepted/Languages spoken if relevant]

HIPAA NOTICE: This email may contain confidential patient information. If received in error, please delete immediately and notify sender.
    """,
    "holiday_seasonal": """
Warm [Holiday] wishes,

[Full Name]
[Title] | [Company Name]

May your [holiday season] be filled with [appropriate wish]!

📧 [Email Address]
📞 [Phone Number] 
🌐 [Website]

🎄 [Holiday emoji] "Spreading joy and [company values] this season" 🎄

[Standard contact information]
    """,
}


def get_signature_template(signature_type: str = "standard_professional") -> str:
    """Get a specific email signature template.

    Args:
        signature_type: Type of signature template to retrieve

    Returns:
        Email signature template string
    """
    return EMAIL_SIGNATURES.get(
        signature_type, EMAIL_SIGNATURES["standard_professional"]
    )


def list_signature_types() -> list:
    """Get list of available signature template types."""
    return list(EMAIL_SIGNATURES.keys())

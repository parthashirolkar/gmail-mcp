"""Gmail MCP Server resources package.

This package contains templates, guidelines, and other resources to enhance
professional email composition and management.
"""

from .html_email_templates import HTML_EMAIL_TEMPLATES
from .email_signatures import (
    EMAIL_SIGNATURES,
    get_signature_template,
    list_signature_types,
)
from .subject_line_guidelines import (
    SUBJECT_LINE_PATTERNS,
    get_subject_line_suggestions,
    validate_subject_line,
)
from .email_security_guidelines import (
    EMAIL_SECURITY_GUIDELINES,
    get_security_guidelines_by_category,
    get_security_checklist,
)
from .email_etiquette import (
    EMAIL_ETIQUETTE_GUIDELINES,
    EMAIL_TONE_GUIDE,
    get_tone_guide,
)

__all__ = [
    "HTML_EMAIL_TEMPLATES",
    "EMAIL_SIGNATURES",
    "get_signature_template",
    "list_signature_types",
    "SUBJECT_LINE_PATTERNS",
    "get_subject_line_suggestions",
    "validate_subject_line",
    "EMAIL_SECURITY_GUIDELINES",
    "get_security_guidelines_by_category",
    "get_security_checklist",
    "EMAIL_ETIQUETTE_GUIDELINES",
    "EMAIL_TONE_GUIDE",
    "get_tone_guide",
]

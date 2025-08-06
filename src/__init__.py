"""Gmail MCP Server - Core package."""

__version__ = "0.1.0"

from .auth_manager import AuthManager
from .gmail_client import GmailClient
from .models import EmailRequest, DraftRequest, EmailResponse, DraftInfo, UserInfo

__all__ = [
    "AuthManager",
    "GmailClient",
    "EmailRequest",
    "DraftRequest",
    "EmailResponse",
    "DraftInfo",
    "UserInfo",
]

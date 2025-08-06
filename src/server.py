"""MCP server implementation for Gmail functionality."""

from typing import Optional, List
from mcp.server.fastmcp import FastMCP

from .auth_manager import AuthManager
from .gmail_client import GmailClient
from .models import EmailRequest, DraftRequest, EmailResponse, DraftInfo, UserInfo

# Initialize MCP server
mcp = FastMCP("Gmail MCP Server")

# Global auth manager
auth_manager = AuthManager()


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
# Gmail MCP Server

A Model Context Protocol (MCP) server that enables AI applications to send emails through Gmail API with secure multi-user authentication.

**Unlike traditional MCP servers that can only read emails, this server enables full email composition and sending capabilities while maintaining security through server-side authentication.**

## Features

- 🔐 **Secure OAuth2 Authentication** - Server-side credential management, tokens never exposed to clients
- 👥 **Multi-User Support** - Switch between different Gmail accounts without server restart
- 📧 **Email Sending** - Send emails with HTML/plain text support, CC/BCC recipients
- 📝 **Draft Management** - Create, list, and send email drafts
- 🔒 **Encrypted Token Storage** - Secure local credential storage with Fernet encryption
- 🚀 **MCP Integration** - Works seamlessly with Claude Desktop and other MCP clients
- 💻 **CLI Management** - Complete command-line interface for user and credential management

## Architecture

This server implements a secure architecture where:

1. **OAuth2 credentials are managed server-side** - MCP clients never see Gmail credentials
2. **Multi-user authentication** - Multiple Gmail accounts can be authenticated and switched between
3. **Encrypted token storage** - All authentication tokens are encrypted before storage
4. **Automatic token refresh** - Handles token expiration transparently

## Installation

### Prerequisites
- Python 3.8+
- `uv` package manager
- Google Cloud Console project with Gmail API enabled

### Setup
1. Clone this repository:
```bash
git clone <repository-url>
cd gmail-mcp
```

2. Install dependencies:
```bash
uv sync
```

## Gmail API Setup

### Step 1: Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Gmail API in **APIs & Services** > **Library**

### Step 2: Configure OAuth Consent Screen
1. Go to **APIs & Services** > **OAuth consent screen**
2. Choose **"External"** user type (unless you have Google Workspace)
3. Fill required fields:
   - App name: "Gmail MCP Server"
   - User support email: Your email
   - Developer contact: Your email
4. Add your email as a test user in the **"Test users"** section
5. Save and continue through all steps

### Step 3: Create OAuth2 Credentials
1. Go to **APIs & Services** > **Credentials**
2. Click **"+ Create Credentials"** > **"OAuth client ID"**
3. Select **"Desktop application"** as application type
4. Enter name: "Gmail MCP Desktop Client"
5. Click **"Create"** and **download the JSON file**

## Configuration

### Set OAuth2 Credentials
```bash
uv run python main.py --credentials /path/to/your/downloaded/credentials.json
```

### Authenticate Gmail Account
```bash
uv run python main.py --login
```

This will:
- Open your browser for OAuth2 authentication
- Securely store encrypted tokens locally
- Set the authenticated user as current

## Usage

### User Management Commands

```bash
# List all authenticated users
uv run python main.py --list-users

# Show current active user
uv run python main.py --current-user

# Switch between authenticated users
uv run python main.py --switch-user user@gmail.com

# Remove a specific user
uv run python main.py --remove-user user@gmail.com

# Logout current user
uv run python main.py --logout
```

### Start MCP Server
```bash
uv run python main.py
```

The server will start and display:
```
Starting Gmail MCP server for user: your-email@gmail.com
```

## MCP Client Configuration

### Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "gmail": {
      "command": "uv",
      "args": ["run", "python", "/absolute/path/to/gmail-mcp/main.py"],
      "cwd": "/absolute/path/to/gmail-mcp"
    }
  }
}
```

### Available MCP Tools

Once connected, your MCP client will have access to these tools:

#### Core Email Tools

##### `send_email`
Send an email immediately.

**Parameters:**
- `to` (string): Recipient email address
- `subject` (string): Email subject line
- `body` (string): Email body (plain text)
- `cc` (string, optional): CC recipients
- `bcc` (string, optional): BCC recipients
- `html_body` (string, optional): HTML version of email body

**Example Usage:**
```
Send an email to john@example.com with subject "Hello" and body "This is a test email"
```

##### `create_draft`
Create an email draft without sending.

**Parameters:** Same as `send_email`

##### `send_draft`
Send an existing email draft.

**Parameters:**
- `draft_id` (string): ID of the draft to send

##### `list_drafts`
List your email drafts.

**Parameters:**
- `max_results` (int, optional): Maximum drafts to return (default: 10)

##### `get_user_info`
Get current authenticated user information.

**Parameters:** None

#### Enhanced Email Assistance Tools

##### `get_subject_line_help`
Get subject line suggestions and best practices based on email type and industry.

**Parameters:**
- `email_type` (string): Type of email (action_required, meeting_requests, status_updates, follow_ups, announcements, urgent, etc.)
- `industry` (string, optional): Industry for specialized templates (sales, marketing, hr, finance, it, project_management)

##### `validate_subject_line_tool`
Validate a subject line against professional best practices.

**Parameters:**
- `subject` (string): Subject line to validate

##### `get_email_templates`
Get available email templates and signatures.

**Parameters:**
- `template_type` (string): Type of templates to retrieve ("html" or "signature")

### MCP Prompts for Email Composition

The server provides intelligent prompts to guide email composition:

#### `professional_email_composer`
Interactive guide for structured professional email creation.

**Parameters:**
- `email_type`: Type of email (general, request, announcement, follow_up, meeting, introduction)
- `recipient_relationship`: Relationship level (professional, personal, unknown, executive) 
- `urgency`: Urgency level (low, normal, high, urgent)

#### `follow_up_email_generator`
Generate contextually appropriate follow-up emails.

**Parameters:**
- `original_context`: Brief description of original email/request
- `time_since_last`: Time elapsed since last communication
- `follow_up_type`: Type of follow-up (polite_reminder, status_check, escalation, thank_you)

#### `meeting_request_composer`
Compose comprehensive meeting requests with all necessary details.

**Parameters:**
- `meeting_purpose`: Main reason for the meeting
- `duration_minutes`: Expected duration in minutes
- `attendee_count`: Number of expected attendees
- `meeting_type`: Type of meeting (discussion, presentation, decision, brainstorm, check_in)

#### `draft_strategy_advisor`
Intelligent advice on whether to save as draft or send immediately.

**Parameters:**
- `email_purpose`: Main purpose of the email
- `urgency`: How urgent the email is
- `stakeholder_count`: Number of people affected
- `complexity`: Complexity of the topic

#### `email_review_checklist`
Comprehensive checklist for reviewing emails before sending.

**Parameters:**
- `email_type`: Type of email (general, meeting_request, urgent, announcement, sensitive)
- `recipient_type`: Type of recipients (internal, external, mixed, executive)
- `has_attachments`: Whether email includes attachments

### MCP Resources

Access professional email templates and guidelines:

#### HTML Email Templates
- `template://html_email/professional_announcement`
- `template://html_email/meeting_invitation`
- `template://html_email/project_update`
- `template://html_email/newsletter`

#### Email Signature Templates
- `template://signature/standard_professional`
- `template://signature/detailed_professional`
- `template://signature/consultant_freelancer`
- `template://signature/sales_business_development`
- `template://signature/executive_minimal`
- And 8 more specialized templates

#### Professional Guidelines
- `guidelines://security/recipient_management`
- `guidelines://security/sensitive_information`
- `guidelines://security/phishing_prevention`
- `guidelines://etiquette/tone_and_language`
- `guidelines://etiquette/timing_and_response`
- `guidelines://etiquette/cultural_considerations`
- And more categories for comprehensive guidance

## Security

### Authentication Security
- **OAuth2 tokens are encrypted** using `cryptography.Fernet`
- **Credentials never leave the server** - not exposed to MCP clients
- **Minimal Gmail scopes** - only `gmail.send` and `gmail.modify` permissions
- **Secure file permissions** - all credential files set to 600 (owner read/write only)

### Data Privacy
- **No data logging** - emails are sent directly to Gmail API
- **Local token storage** - all authentication data stored locally
- **No remote dependencies** - server runs entirely on your machine

### Network Security
- **Direct Gmail API connection** - no intermediary services
- **HTTPS only** - all API calls use secure connections
- **Token refresh handled automatically** - no manual credential management needed

## File Structure

```
~/.gmail-mcp/                    # Configuration directory
├── credentials.json             # OAuth2 client credentials  
├── current_user.json           # Current active user
├── .key                        # Encryption key for tokens
└── tokens/
    ├── user1@gmail.com.json    # Encrypted tokens for user1
    └── user2@gmail.com.json    # Encrypted tokens for user2
```

Project structure:
```
gmail-mcp/
├── main.py                     # Entry point and CLI interface
├── src/                        # Core functionality package
│   ├── __init__.py            # Package exports
│   ├── server.py              # MCP server and tools
│   ├── auth_manager.py        # OAuth2 authentication manager
│   ├── gmail_client.py        # Gmail API client wrapper
│   └── models.py              # Pydantic data models
├── pyproject.toml              # Project dependencies
├── README.md                   # This file
└── CLAUDE.md                   # Development context
```

## Troubleshooting

### Common Issues

#### "No authenticated user" Error
```bash
# Check authenticated users
uv run python main.py --list-users

# If empty, authenticate first
uv run python main.py --login
```

#### "Access blocked" During OAuth
- Ensure your email is added as a test user in OAuth consent screen
- Or publish your app in Google Cloud Console (safe for personal use)

#### "Insufficient authentication scopes" Error
- Re-authenticate to get updated scopes:
```bash
uv run python main.py --logout
uv run python main.py --login
```

#### Browser Issues in WSL
- The authentication will provide a URL to copy manually if browser auto-open fails
- Copy the URL and open it in your Windows browser

#### Token Refresh Issues
- Tokens automatically refresh, but if issues persist:
```bash
uv run python main.py --logout
uv run python main.py --login
```

### Getting Help

If you encounter issues:
1. Check your Google Cloud Console project has Gmail API enabled
2. Verify OAuth consent screen is properly configured
3. Ensure your email is added as a test user
4. Check file permissions in `~/.gmail-mcp/` directory

## Development

### Running Tests
```bash
# Basic functionality tests
uv run python main.py --help
uv run python main.py --current-user
uv run python main.py --list-users
```

### Code Quality
```bash
uv run black .
uv run ruff check .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with appropriate tests
4. Ensure code formatting with black and ruff
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Changelog

### v0.1.0
- Initial implementation with Gmail sending capabilities
- Multi-user OAuth2 authentication
- Encrypted token storage
- Draft management features
- CLI interface for user management
- MCP integration with Claude Desktop
# Gmail MCP Server - Claude Context

This is a Gmail Model Context Protocol (MCP) server that enables AI applications to send emails through Gmail API with secure multi-user authentication.

## Project Overview

The Gmail MCP server provides a secure bridge between MCP clients (like Claude Desktop) and the Gmail API, allowing AI assistants to send emails on behalf of authenticated users.

### Key Architecture Decisions

1. **Server-side Authentication**: OAuth2 tokens are stored encrypted on the server, never exposed to MCP clients
2. **Multi-user Support**: Multiple Gmail accounts can be authenticated and switched between without server restart
3. **Secure Token Storage**: All tokens are encrypted using `cryptography.Fernet` with secure file permissions
4. **Minimal Scopes**: Uses `gmail.send` and `gmail.modify` for sending emails and managing drafts

## File Structure

```
gmail-mcp/
├── main.py              # Entry point and CLI interface
├── src/                 # Core functionality package
│   ├── __init__.py     # Package exports
│   ├── server.py       # MCP server and tools
│   ├── auth_manager.py # OAuth2 authentication & multi-user management
│   ├── gmail_client.py # Gmail API wrapper for email operations
│   └── models.py       # Pydantic models for structured data
├── pyproject.toml       # Project dependencies and configuration
├── README.md            # User documentation
└── CLAUDE.md           # This file - Claude context
```

## Core Components

### AuthManager (`auth_manager.py`)
- Manages OAuth2 flow with Google APIs
- Encrypts and stores tokens securely in `~/.gmail-mcp/`
- Supports multiple Gmail accounts with user switching
- Handles token refresh automatically

### GmailClient (`gmail_client.py`)
- Wraps Gmail API for email operations
- Handles email composition and sending
- Manages draft creation and sending
- Provides user profile information

### MCP Tools (`src/server.py`)
- `send_email`: Send emails immediately with optional HTML content
- `create_draft`: Create email drafts without sending
- `send_draft`: Send existing drafts by ID
- `list_drafts`: List user's email drafts
- `get_user_info`: Get current authenticated user information

### CLI Interface (`main.py`)
- Lightweight entry point that imports server functionality
- Handles command-line argument parsing
- Delegates to appropriate auth_manager methods

## Authentication Flow

1. User sets OAuth2 credentials: `gmail-mcp --credentials /path/to/credentials.json`
2. User authenticates: `gmail-mcp --login` (opens browser for OAuth2)
3. Tokens are encrypted and stored in `~/.gmail-mcp/tokens/`
4. Server uses stored tokens for all Gmail operations
5. MCP clients never see credentials - only connect to authenticated server

## Security Features

- **OAuth2 Scopes**: `gmail.send` and `gmail.modify` (minimal required permissions)
- **Encrypted Storage**: All tokens encrypted with Fernet symmetric encryption
- **Secure Permissions**: All credential files set to 600 (owner read/write only)
- **No Client Exposure**: MCP clients only need server connection details
- **Token Management**: Automatic refresh with fallback to re-authentication

## Dependencies

Core dependencies installed via `uv`:
- `mcp`: Model Context Protocol SDK
- `google-auth`, `google-auth-oauthlib`, `google-api-python-client`: Google API integration
- `pydantic`: Data validation and modeling
- `cryptography`: Token encryption
- `click`: CLI interface

## Usage Patterns

### CLI Management
```bash
gmail-mcp --credentials /path/to/credentials.json  # Set OAuth2 credentials
gmail-mcp --login                                  # Authenticate Gmail account
gmail-mcp --list-users                            # List authenticated users
gmail-mcp --switch-user user@gmail.com           # Switch active account
gmail-mcp --current-user                          # Show current user
gmail-mcp                                         # Start MCP server
```

### MCP Client Configuration
```json
{
  "mcpServers": {
    "gmail": {
      "command": "gmail-mcp"
    }
  }
}
```

## Development Notes

- Built with FastMCP for rapid MCP server development
- Uses async/await patterns for MCP tool implementations
- Includes comprehensive error handling with user-friendly messages
- Supports both console-based and local server OAuth2 flows (WSL compatible)
- Pydantic models provide structured data validation for all email operations

## Testing Approach

The server includes basic CLI testing and can be validated by:
1. Checking authentication flow with `--login`
2. Verifying user management with `--list-users`, `--current-user`
3. Testing server startup without authentication (should fail gracefully)
4. Confirming MCP server starts successfully with authenticated user

## Common Issues & Solutions

1. **Scope Errors**: Ensure `gmail.modify` scope for draft operations
2. **Browser Issues in WSL**: Uses `open_browser=False` with fallback to console auth
3. **Token Expiration**: Automatic refresh with re-authentication fallback
4. **Permission Errors**: All config files automatically set to secure permissions (600)

This server successfully bridges the gap between AI assistants and Gmail, providing secure, multi-user email sending capabilities while maintaining strong security practices.
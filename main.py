"""Gmail MCP Server - Entry point and CLI interface."""

import sys
import os
import click

from src.server import auth_manager
from src.server import create_mcp_server


# CLI interface
@click.command()
@click.option("--login", is_flag=True, help="Authenticate a new Gmail user")
@click.option("--logout", is_flag=True, help="Logout current user")
@click.option(
    "--switch-user", type=str, help="Switch to a different authenticated user"
)
@click.option("--list-users", is_flag=True, help="List all authenticated users")
@click.option("--remove-user", type=str, help="Remove a specific user")
@click.option("--credentials", type=str, help="Path to OAuth2 credentials file")
@click.option("--current-user", is_flag=True, help="Show current authenticated user")
@click.option("--http", is_flag=True, help="Start HTTP server for Smithery deployment")
def cli(login, logout, switch_user, list_users, remove_user, credentials, current_user, http):
    """Gmail MCP Server CLI."""

    if credentials:
        try:
            auth_manager.set_credentials_file(credentials)
            click.echo(f"Credentials file set: {credentials}")
        except Exception as e:
            click.echo(f"Error setting credentials: {e}", err=True)
            sys.exit(1)
        return

    if login:
        try:
            if not auth_manager.credentials_file.exists():
                click.echo("Error: OAuth2 credentials not found.")
                click.echo(
                    "First set credentials with: gmail-mcp --credentials /path/to/credentials.json"
                )
                sys.exit(1)

            click.echo("Starting OAuth2 authentication...")
            email = auth_manager.authenticate_user()
            click.echo(f"Successfully authenticated: {email}")
        except Exception as e:
            click.echo(f"Authentication failed: {e}", err=True)
            sys.exit(1)
        return

    if logout:
        if auth_manager.logout_current_user():
            click.echo("Successfully logged out")
        else:
            click.echo("No user currently logged in")
        return

    if switch_user:
        if auth_manager.get_credentials(switch_user):
            auth_manager.set_current_user(switch_user)
            click.echo(f"Switched to user: {switch_user}")
        else:
            click.echo(f"User not found or not authenticated: {switch_user}")
            sys.exit(1)
        return

    if list_users:
        users = auth_manager.list_users()
        current = auth_manager.get_current_user()
        if users:
            click.echo("Authenticated users:")
            for user in users:
                marker = " (current)" if user == current else ""
                click.echo(f"  - {user}{marker}")
        else:
            click.echo("No authenticated users")
        return

    if remove_user:
        if auth_manager.remove_user(remove_user):
            click.echo(f"Removed user: {remove_user}")
        else:
            click.echo(f"User not found: {remove_user}")
        return

    if current_user:
        current = auth_manager.get_current_user()
        if current:
            click.echo(f"Current user: {current}")
        else:
            click.echo("No user currently authenticated")
        return

    # HTTP server mode for Smithery deployment
    if http:
        port = int(os.getenv("PORT", 8000))
        host = "0.0.0.0"
        
        click.echo(f"Starting SSE HTTP server on {host}:{port} for Smithery deployment")
        mcp_server = create_mcp_server(host=host, port=port)
        mcp_server.run(transport="sse")
        return

    # Default: Start MCP server
    # Allow server startup without authentication for tool discovery (required for Smithery)
    # Tools will handle authentication checks individually
    mcp_server = create_mcp_server()
    mcp_server.run()


if __name__ == "__main__":
    cli()

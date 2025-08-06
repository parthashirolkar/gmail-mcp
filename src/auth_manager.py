"""Authentication manager for Gmail OAuth2 with multi-user support."""

import json
import os
from pathlib import Path
from typing import Optional, List, Dict, Any
from cryptography.fernet import Fernet
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify'
]


class AuthManager:
    """Manages OAuth2 authentication for multiple Gmail users."""

    def __init__(self, config_dir: Optional[Path] = None):
        """Initialize auth manager with configuration directory."""
        self.config_dir = config_dir or Path.home() / ".gmail-mcp"
        self.config_dir.mkdir(exist_ok=True)

        self.tokens_dir = self.config_dir / "tokens"
        self.tokens_dir.mkdir(exist_ok=True)

        self.credentials_file = self.config_dir / "credentials.json"
        self.current_user_file = self.config_dir / "current_user.json"
        self.key_file = self.config_dir / ".key"

        self._ensure_encryption_key()

    def _ensure_encryption_key(self) -> None:
        """Ensure encryption key exists for token storage."""
        if not self.key_file.exists():
            key = Fernet.generate_key()
            self.key_file.write_bytes(key)
            self.key_file.chmod(0o600)  # Owner read/write only

    def _get_cipher(self) -> Fernet:
        """Get encryption cipher for token storage."""
        key = self.key_file.read_bytes()
        return Fernet(key)

    def _encrypt_data(self, data: Dict[str, Any]) -> bytes:
        """Encrypt data for secure storage."""
        cipher = self._get_cipher()
        json_data = json.dumps(data).encode()
        return cipher.encrypt(json_data)

    def _decrypt_data(self, encrypted_data: bytes) -> Dict[str, Any]:
        """Decrypt data from secure storage."""
        cipher = self._get_cipher()
        json_data = cipher.decrypt(encrypted_data)
        return json.loads(json_data.decode())

    def set_credentials_file(self, credentials_path: str) -> None:
        """Set the OAuth2 client credentials file path."""
        if not os.path.exists(credentials_path):
            raise FileNotFoundError(f"Credentials file not found: {credentials_path}")

        # Copy credentials to config directory
        with open(credentials_path, "r") as src:
            credentials_data = json.load(src)

        with open(self.credentials_file, "w") as dst:
            json.dump(credentials_data, dst, indent=2)

        self.credentials_file.chmod(0o600)

    def authenticate_user(self, email: Optional[str] = None) -> str:
        """Authenticate a user and return their email address."""
        if not self.credentials_file.exists():
            raise FileNotFoundError(
                "OAuth2 credentials not found. Please set credentials file first."
            )

        # Create OAuth2 flow
        flow = InstalledAppFlow.from_client_secrets_file(
            str(self.credentials_file), SCOPES
        )

        # For WSL/headless environments, use console-based auth
        try:
            creds = flow.run_local_server(port=0, open_browser=False)
        except Exception:
            # Fallback to console-based flow
            creds = flow.run_console()

        # Get user info to determine email
        from googleapiclient.discovery import build

        service = build("gmail", "v1", credentials=creds)
        profile = service.users().getProfile(userId="me").execute()
        user_email = profile["emailAddress"]

        # Store encrypted tokens
        token_data = {
            "token": creds.token,
            "refresh_token": creds.refresh_token,
            "token_uri": creds.token_uri,
            "client_id": creds.client_id,
            "client_secret": creds.client_secret,
            "scopes": creds.scopes,
            "email": user_email,
        }

        token_file = self.tokens_dir / f"{user_email}.json"
        encrypted_data = self._encrypt_data(token_data)
        token_file.write_bytes(encrypted_data)
        token_file.chmod(0o600)

        # Set as current user
        self.set_current_user(user_email)

        return user_email

    def get_credentials(self, email: Optional[str] = None) -> Optional[Credentials]:
        """Get credentials for a user (current user if email not specified)."""
        if email is None:
            email = self.get_current_user()

        if not email:
            return None

        token_file = self.tokens_dir / f"{email}.json"
        if not token_file.exists():
            return None

        try:
            encrypted_data = token_file.read_bytes()
            token_data = self._decrypt_data(encrypted_data)

            creds = Credentials(
                token=token_data["token"],
                refresh_token=token_data["refresh_token"],
                token_uri=token_data["token_uri"],
                client_id=token_data["client_id"],
                client_secret=token_data["client_secret"],
                scopes=token_data["scopes"],
            )

            # Refresh token if needed
            if not creds.valid:
                if creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                    # Update stored tokens
                    token_data.update(
                        {
                            "token": creds.token,
                            "refresh_token": creds.refresh_token,
                        }
                    )
                    encrypted_data = self._encrypt_data(token_data)
                    token_file.write_bytes(encrypted_data)
                else:
                    return None

            return creds
        except Exception:
            return None

    def get_current_user(self) -> Optional[str]:
        """Get the currently active user email."""
        if not self.current_user_file.exists():
            return None

        try:
            with open(self.current_user_file, "r") as f:
                data = json.load(f)
                return data.get("email")
        except Exception:
            return None

    def set_current_user(self, email: str) -> None:
        """Set the currently active user."""
        with open(self.current_user_file, "w") as f:
            json.dump({"email": email}, f, indent=2)
        self.current_user_file.chmod(0o600)

    def list_users(self) -> List[str]:
        """List all authenticated users."""
        users = []
        for token_file in self.tokens_dir.glob("*.json"):
            email = token_file.stem
            users.append(email)
        return sorted(users)

    def remove_user(self, email: str) -> bool:
        """Remove a user's authentication."""
        token_file = self.tokens_dir / f"{email}.json"
        if token_file.exists():
            token_file.unlink()

            # If this was the current user, clear current user
            if self.get_current_user() == email:
                if self.current_user_file.exists():
                    self.current_user_file.unlink()

            return True
        return False

    def logout_current_user(self) -> bool:
        """Logout the current user."""
        current_user = self.get_current_user()
        if current_user:
            return self.remove_user(current_user)
        return False

# Contributing to Gmail MCP Server

Thank you for your interest in contributing to the Gmail MCP Server! This guide will help you get started with development and contributions.

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) for dependency management
- A Google Cloud Console project with Gmail API enabled
- OAuth2 credentials file

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/gmail-mcp.git
   cd gmail-mcp
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up OAuth2 credentials**
   ```bash
   gmail-mcp --credentials /path/to/your/credentials.json
   gmail-mcp --login
   ```

4. **Test the installation**
   ```bash
   gmail-mcp --current-user
   ```

## 🛠️ Development Workflow

### Code Style

We use `ruff` for linting and code formatting:

```bash
# Lint code
ruff check .

# Format code
ruff format .
```

### Testing

```bash
# Run tests (when available)
pytest

# Test server startup
gmail-mcp --current-user

# Test MCP server
gmail-mcp  # Should start without errors
```

### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow existing code patterns
   - Add appropriate error handling
   - Update documentation if needed

3. **Test your changes**
   ```bash
   ruff check .
   # Test the functionality manually
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

## 📋 Contribution Guidelines

### What We Welcome

- **Bug fixes**: Fix issues or improve error handling
- **New features**: Email management tools, authentication improvements
- **Documentation**: Improve setup guides, add examples
- **Tests**: Add unit tests or integration tests
- **Performance**: Optimize authentication flow or email operations

### Code Standards

- **Async/await**: Use async patterns for MCP tools
- **Error handling**: Provide user-friendly error messages
- **Security**: Never log credentials or sensitive data
- **Documentation**: Add docstrings for new functions
- **Type hints**: Use Python type hints where applicable

### Pull Request Process

1. **Ensure your code passes linting**
   ```bash
   ruff check .
   ```

2. **Update the README if needed**
   - Add new features to the feature list
   - Update installation or usage instructions

3. **Create a descriptive PR**
   - Clear title and description
   - Reference any related issues
   - Include testing steps

4. **Respond to reviews**
   - Address feedback promptly
   - Make requested changes

## 🏗️ Project Structure

```
gmail-mcp/
├── src/                     # Core functionality
│   ├── server.py           # MCP server and tools
│   ├── auth_manager.py     # Authentication logic
│   ├── gmail_client.py     # Gmail API wrapper
│   ├── models.py           # Data models
│   └── resources/          # Email templates and guidelines
├── main.py                 # CLI entry point
├── pyproject.toml         # Dependencies and config
├── smithery.yaml          # Smithery deployment config
├── Dockerfile             # Docker deployment
└── README.md              # User documentation
```

## 🔐 Security Considerations

- **Never commit credentials** to version control
- **Encrypt sensitive data** using the existing encryption patterns
- **Use minimal OAuth2 scopes** (gmail.send, gmail.modify)
- **Validate all inputs** in MCP tools
- **Handle authentication errors** gracefully

## 🐛 Reporting Issues

### Bug Reports

Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) and include:

- Gmail MCP Server version
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Any error messages

### Feature Requests

Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.md) and describe:

- The problem you're trying to solve
- Your proposed solution
- Alternative solutions considered
- Any additional context

## 📞 Getting Help

- **Documentation**: Check the [README.md](README.md) first
- **Issues**: Search existing issues before creating new ones
- **Discussions**: Use GitHub Discussions for questions
- **Security**: Report security issues privately via email

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes for significant contributions
- README acknowledgments

Thank you for helping make Gmail MCP Server better for everyone!
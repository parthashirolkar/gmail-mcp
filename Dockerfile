# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast Python package installation
RUN pip install uv

# Copy dependency files
COPY pyproject.toml ./
COPY uv.lock ./

# Install Python dependencies
RUN uv sync --frozen

# Copy application code
COPY . .

# Create directory for credentials and tokens
RUN mkdir -p /app/.gmail-mcp/tokens && \
    chmod 700 /app/.gmail-mcp

# Expose port for HTTP server
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH="/app"
ENV PORT=8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

# Run the HTTP server for Smithery deployment
CMD ["python", "-m", "main", "--http"]
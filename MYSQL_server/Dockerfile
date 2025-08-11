# Use official Python base image
FROM python:3.12-slim

# Install uv
RUN pip install --no-cache-dir uv

# Set working directory
WORKDIR /app

# Copy dependency files first (for better caching)
COPY pyproject.toml uv.lock ./

# Install dependencies using uv (will use uv.lock to ensure reproducibility)
RUN uv sync --frozen

# Copy the rest of your application code
COPY . .

# Set environment variables (adjust PORT if Azure sets it dynamically)
ENV PORT=8000

# Command to run your MCP server
CMD ["uv", "run", "main.py"]

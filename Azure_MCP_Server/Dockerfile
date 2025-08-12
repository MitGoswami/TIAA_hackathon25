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

ENV MYSQL_HOST=sql5.freesqldatabase.com
ENV MYSQL_USER=sql5794381
ENV MYSQL_PASSWORD=DYxhJVHRRs
ENV MYSQL_DATABASE=sql5794381
ENV MYSQL_PORT=3306

# Copy the rest of your application code
COPY . .

EXPOSE 8181

# Command to run your MCP server
CMD ["uv", "run", "main.py"]

# Use slim Python 3.12 base
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (for lxml, mysql-connector, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Hardcode MySQL credentials 
ENV MYSQL_HOST="sql5.freesqldatabase.com"
ENV MYSQL_USER="sql5794381"
ENV MYSQL_PASSWORD="DYxhJVHRRs"
ENV MYSQL_DATABASE="sql5794381"
ENV MYSQL_PORT=3306

# Copy application files
COPY . .

# Expose port (change if your app uses another)
EXPOSE 8000

# Command to run the app
# Adjust main.py to whatever your entry point is
CMD ["python", "main.py"]

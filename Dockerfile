# Use an old image with known vulnerabilities
FROM python:3.7-slim

# Set working directory
WORKDIR /app

# Install packages with known CVEs
RUN apt-get update && apt-get install -y \
    curl \
    openssl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy vulnerable app
COPY app/main.py .

# Expose a secret to trigger secret detection
ENV AWS_SECRET_ACCESS_KEY="AKIAFAKEKEYFORTRIVYSCAN123"

# Install a vulnerable Python package
RUN pip install flask django==1.2  # known vulnerabilities

# Run app
CMD ["python", "main.py"]

# Use the official Python image from Docker Hub as the base image
FROM python:3.12-slim

# Set non-interactive build to avoid prompts
ARG DEBIAN_FRONTEND=noninteractive

# Install system dependencies including libicu for globalization support
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libicu-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the Docker container
WORKDIR /app

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code from your host to your image filesystem
COPY . .

# Ensure CutFileParserCLI is executable
# RUN chmod +x /app/tools/linuxParser/CutFileParserCLI

# Make port 8050 available to the world outside this container
EXPOSE 8050

# Define the command to run your app
CMD ["python", "app.py"]

# # Use an official Ubuntu image as the base
# FROM ubuntu:20.04

# # Avoid prompts from apt during build
# # ARG DEBIAN_FRONTEND=noninteractive

# # Install Python and other dependencies
# RUN apt-get update && \
#     apt-get install -y python3-pip python3-dev && \
#     ln -s /usr/bin/python3 /usr/bin/python && \
#     apt-get clean

# # Set the working directory in the container
# WORKDIR /app

# # Copy the application files into the container
# COPY . /app

# # Install Python dependencies
# RUN pip3 install -r requirements.txt

# # Make your application's script executable (adjust the name as necessary)
# # RUN chmod +x ./tools/linuxParser/CutFileParserCLI

# # Expose the port the app runs on
# EXPOSE 8050

# # Command to run the application
# CMD ["python", "app.py"]


# Use the official Python image from Docker Hub as the base image
FROM python:3.12-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the requirements.txt file into our working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app's source code from your host to your image filesystem
COPY . .

# Make port 8050 available to the world outside this container
EXPOSE 8050

# Define the command to run your app using gunicorn as the web server
# Adjust the number of workers and threads as necessary
# CMD ["gunicorn", "-b", "0.0.0.0:8050", "app:server"]
CMD ["python", "app.py"]



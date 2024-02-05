# Use a Windows Server Core image as the base
# FROM mcr.microsoft.com/windows/servercore:ltsc2019
FROM mcr.microsoft.com/windows/servercore:20H2


# Install Python (adjust the version as necessary)
ADD https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe /python-installer.exe
RUN start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 && \
    del /q python-installer.exe

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install Python dependencies
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8050

# Command to run the application
CMD ["python", "app.py"]

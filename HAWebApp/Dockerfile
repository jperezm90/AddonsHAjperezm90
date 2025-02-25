# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy your application files to the container
COPY . /app

# Install Python dependencies (if any, e.g., Flask)
RUN pip install --no-cache-dir flask

# Make the run.sh script executable
RUN chmod +x run.sh

# Define the command to run your app
CMD ["./run.sh"]
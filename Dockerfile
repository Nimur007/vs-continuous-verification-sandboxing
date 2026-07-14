# Use a lightweight official Python image
FROM python:3.10-slim

# Set working directory inside the sandbox
WORKDIR /app

# Copy the repository files into the container
COPY . /app

# Run the CVS scanner as the entry point
CMD ["python", "cvs_scanner.py"]

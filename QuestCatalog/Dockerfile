FROM ubuntu:latest
# auth-service/Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5002

# Command to run the application
CMD ["uvicorn", "apps:app", "--host", "0.0.0.0", "--port", "5002"]
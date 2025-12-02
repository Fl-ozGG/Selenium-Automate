# Use official Python image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy your project files
COPY FormAutomationGRID.py requirements.txt ./ 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "FormAutomationGRID.py"]

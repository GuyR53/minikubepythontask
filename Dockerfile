# Dockerfile

# Base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy both app.py files
COPY microservices/app.py /app/microservices_app.py
COPY numbers_api/app.py /app/numbers_api_app.py

# Expose the port that your app runs on (adjust as needed)
EXPOSE 5000

# Default command to run the microservices app
CMD ["python", "microservices_app.py"]

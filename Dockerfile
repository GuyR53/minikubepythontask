# Dockerfile

# Base image
FROM python:3.8.0-alpine

# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy both app.py files
COPY microservices/microservices_app.py .
COPY numbers_api/numbers_api_app.py .
RUN  chmod a+x microservices_app.py
RUN  chmod a+x numbers_api_app.py

# Expose the port that your app runs on (adjust as needed)
EXPOSE 5000

# Default command to run the microservices app
CMD ["python3", "microservices_app.py"]

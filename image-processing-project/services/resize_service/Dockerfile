# Use Python 3.12 base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files
COPY resize_service/resize_service.py /app/resize.py
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 8001

# Run the service with Uvicorn
CMD ["uvicorn", "resize:app", "--host", "0.0.0.0", "--port", "8002"]

# Use Python 3.12 base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files
COPY grayscale_service/grayscale_service.py /app/grayscale.py
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 8002

# Run the service with Uvicorn
CMD ["uvicorn", "grayscale:app", "--host", "0.0.0.0", "--port", "8001"]

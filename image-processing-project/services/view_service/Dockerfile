# Use Python 3.12 base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files
COPY view_service/view_service.py /app/view.py
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 8003

# Run the service with Uvicorn
CMD ["uvicorn", "view:app", "--host", "0.0.0.0", "--port", "8003"]

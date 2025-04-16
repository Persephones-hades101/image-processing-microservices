FROM python:3.12-alpine
WORKDIR /app
COPY filter_service/filter_service.py /app/filter.py
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8003
CMD ["uvicorn", "filter:app", "--host", "0.0.0.0", "--port", "8003"]
FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir --default-timeout=300 --retries=10 -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]

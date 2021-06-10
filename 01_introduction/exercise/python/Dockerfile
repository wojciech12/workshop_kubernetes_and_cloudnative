from python:3.8-slim

WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


WORKDIR /app
COPY hello.py .

CMD ["gunicorn", "hello:app", "--bind", "0.0.0.0:8080"]

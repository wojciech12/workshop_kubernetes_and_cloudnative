from python:3-slim

WORKDIR /tmp
ADD requirements.txt /tmp
RUN pip --no-cache-dir install -r requirements.txt 

WORKDIR /app
ADD main.py /app

CMD ["gunicorn", "--log-level", "${LOG_LEVEL}","--graceful-timeout", "30", "--bind", "0.0.0.0:8000", "api:app"]

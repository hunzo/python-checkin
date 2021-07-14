FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache build-base 
RUN apk add --no-cache tzdata
RUN python -m pip install --upgrade pip

ENV TZ Asia/Bangkok

COPY outfile/ outfile/

COPY .env .
COPY api.py .
COPY csv_services.py .
COPY model.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn api:api --host 0.0.0.0 --port 8080

FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache build-base 

ENV TZ Asia/Bangkok

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# CMD gunicorn -b 0.0.0.0:8000 ui:app
CMD flask run -h 0.0.0.0 

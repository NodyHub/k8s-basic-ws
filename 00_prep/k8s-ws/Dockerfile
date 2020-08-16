FROM python:3.9-rc-alpine3.12

RUN apk --no-cache add curl

COPY data /data
COPY app /app

RUN pip install -r /app/requirements.txt && \
    rm /app/requirements.txt

ENV DB_CON_STRING=mongodb://mongodb
ENV DATA_DIR=/data
ENV FLASK_APP=/app/app.py

WORKDIR /app
CMD flask run --host=0.0.0.0

EXPOSE 5000

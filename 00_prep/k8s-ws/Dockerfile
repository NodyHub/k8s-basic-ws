FROM python:3.9-rc-alpine3.12

RUN apk --no-cache add curl

COPY data /data
ENV SECRET_LOG=/data/foo.log

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && \
    rm requirements.txt
COPY app /app
WORKDIR /app

ENV FLASK_APP=/app/app.py

CMD flask run --host=0.0.0.0

EXPOSE 5000

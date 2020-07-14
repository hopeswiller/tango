FROM python:3.7.2-alpine

LABEL maintainer="David Boateng Adams <davidba941@gmail.com>"
LABEL description="This project is primarily developed to monitor a container state and sends an email notification"

ENV PYTHONUNBUFFERED 1
ARG USER=tango

RUN pip install --upgrade pip
WORKDIR /app

RUN addgroup -g 1000 -S ${USER} && adduser -u 1000 -S ${USER} -G ${USER}
RUN chmod -R 777 /app/ && chown -Rf tango:tango /app/

COPY . .
RUN pip install --default-timeout=100 -r requirements.txt

# USER ${USER}
FROM python:3.7.2-alpine

LABEL maintainer="David Boateng Adams <davidba941@gmail.com>"
LABEL description="This project is primarily developed to monitor a container state and sends an email notification"

ENV PYTHONUNBUFFERED 1
ARG USER=tango
# Add license key of new relic account
ARG KEY=

RUN pip install --upgrade pip
WORKDIR /app

# In order to cache packages installed via pip,
# it’s necessary to add the requirements.txt file to the image, and install, before adding the rest of the repo
COPY requirements.txt requirements.txt
RUN pip install --default-timeout=100 -r requirements.txt
COPY . .

RUN addgroup -g 1000 -S ${USER} && adduser -u 1000 -S ${USER} -G ${USER}
RUN chmod -R 777 /app/ && chown -Rf tango:tango /app/

# comment this line if you don't wish to use new relic monitoring tool
RUN newrelic-admin generate-config ${KEY} newrelic.ini

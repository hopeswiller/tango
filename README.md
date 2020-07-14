# Tango

> Docker Container Tracker and Email Notifier.

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Features](#features)
- [Status](#status)

## General info

This project is primarily developed to check if a docker container is running or not and sends an email notification to a specified user if container is exited


## Technologies

- Python - version 3.7
- Docker SDK - version 4.0
    - Read more here : https://docker-py.readthedocs.io/en/stable/

## Setup

Setup can be done manually or via Docker which is recommended

- #### Manual

Run pip install -r requirements.txt

- #### Docker

Comment out line 11 and line 13 in src/monitor.py when running docker-compose file
Run docker-compose up


## Features

List of features ready and TODOs for future development

- [x] Connect email Server via smtp
- [x] Monitors docker container using container name specified as environment variable
- [x] Sends an email if container state is existed after three restarts
- [x] Attaches an attachment file when sending email notification
  - [x] Creates log file from the logs of the container
- [x] Runs at every number of minutes specified


TODOs:

- [ ] Supply email template when sending email

## Status

Project is: _in progress_

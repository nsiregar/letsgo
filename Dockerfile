# Pull base image
FROM python:3.7.4-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install dependencies
RUN apk update && \
 apk add postgresql-libs bash && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev && \
 apk add alpine-sdk musl-dev

# Add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install -r dev-requirements.txt

# Clean Up
RUN apk --purge del .build-deps

# Copy project
COPY . /usr/src/app
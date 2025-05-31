FROM python:3.12.1-slim-bullseye

RUN apt-get update && apt-get install -y make

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN adduser --disabled-password --gecos '' userpy

RUN mkdir -p /usr/src/app && chown userpy:userpy /usr/src/app
RUN mkdir -p /home/userpy/.cache/pip && chown userpy:userpy /home/userpy/.cache/pip

WORKDIR /usr/src/app

USER userpy
# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip wheel

RUN pip install -r requirements.txt

COPY . /code/
FROM python:3.10.13-slim

RUN useradd --create-home --home-dir /app --shell /bin/bash app
WORKDIR /app

COPY requirements ./requirements
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements/base.txt

COPY . .
USER app

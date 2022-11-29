# 1. Base image
FROM python:3.8.3-slim-buster

# 2. Copy files
COPY . /Docker

# 3. Install dependencies
RUN pip install -r /Docker/requirements.txt

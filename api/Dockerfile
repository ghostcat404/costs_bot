FROM python:3.8-slim

WORKDIR /app

ADD ./app /app

ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait
RUN chmod +x /app/run_api.sh

ADD ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir

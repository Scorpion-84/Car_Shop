ARG DOCKER_REG
FROM ${DOCKER_REG:-}python:3.9
# FROM python:3.12-slim

RUN mkdir -p /home/question_app
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

WORKDIR /home/question_app

COPY ./src .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm requirements.txt

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y netcat-traditional
RUN apt-get install -y dos2unix

ADD ./docker-entrypoint.sh /tmp/docker-entrypoint.sh
RUN dos2unix /tmp/docker-entrypoint.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
RUN chmod +x /tmp/docker-entrypoint.sh


ENTRYPOINT ["bash", "/tmp/docker-entrypoint.sh"]




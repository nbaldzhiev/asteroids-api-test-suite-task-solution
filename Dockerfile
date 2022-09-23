# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /sbdb-api-tests-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ./run_tests.sh && tail -f /dev/null

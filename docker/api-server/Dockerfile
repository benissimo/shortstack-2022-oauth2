# syntax=docker/dockerfile:1
FROM python:3.10.7

WORKDIR /src/api_server
ENV FLASK_APP=api_server
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5052

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5052
COPY ./src/api_server .

CMD ["flask", "run"]

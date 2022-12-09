# syntax=docker/dockerfile:1
FROM python:3.10.7

WORKDIR /src/authorization_server
ENV FLASK_APP=authorization_server
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5051

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5051
COPY ./src/authorization_server .

CMD ["python3", "authorization_server.py"]

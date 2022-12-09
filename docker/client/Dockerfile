# syntax=docker/dockerfile:1
FROM python:3.10.7

WORKDIR /src/client
ENV FLASK_APP=client
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5050

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5050
COPY ./src/client .

CMD ["python3", "client.py"]

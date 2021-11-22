ARG BASE_IMAGE=python:3.7.11-stretch
FROM $BASE_IMAGE
WORKDIR /code

COPY * /code/
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]
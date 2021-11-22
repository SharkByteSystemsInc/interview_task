FROM python:3.9.2-slim-buster
WORKDIR /code

COPY * /code/
RUN python3 -m pip install --disable-pip-version-check -qr requirements.txt
ENTRYPOINT ["python3", "main.py"]

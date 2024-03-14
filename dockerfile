FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
ADD .env.docker /code/.env



CMD gunicorn DataLoader.wsgi:application -b 0.0.0.0:8000
FROM python:3.7
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

ADD ./ /usr/src/app/
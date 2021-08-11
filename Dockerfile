FROM alpine

RUN apk update && apk add python3

RUN apk add py3-pip

RUN pip3 install django

WORKDIR http_api

COPY . .

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
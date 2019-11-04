FROM python:3.6-alpine

RUN apk update && apk upgrade && \
    echo "**** other packages *****" && \
    apk add --no-cache \
        sqlite \
        python3-dev

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /home/docker/code

ADD requirements.txt /home/docker/code
RUN pip install -r requirements.txt && \
    pip install git+https://github.com/eadwinCode/django-compressor.git@develop

COPY . /home/docker/code/

EXPOSE 80

CMD ["python", "manage", "runserver" ,"--settings django_vue.settings"]
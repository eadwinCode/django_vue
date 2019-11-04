FROM python:3.6-alpine

LABEL maintainer="eadwinCode" 

RUN apk update && apk upgrade && \
    echo "**** other packages *****" && \
    apk add --virtual build-deps && \
    apk add --no-cache \
        sqlite \
        python3-dev \
        libpq \
        gcc\
        musl-dev\
    && apk del build-deps && \
    apk add --no-cache --update nodejs nodejs-npm

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /home/docker/code

ADD requirements.txt /home/docker/code
ADD package.json /home/docker/code

RUN apk add git
RUN pip install -r requirements.txt && \
    pip install git+https://github.com/eadwinCode/django-compressor.git@develop && \
    npm install -g parcel && \
    npm install

COPY . /home/docker/code/

EXPOSE 80

RUN adduser -D user_vue

USER user_vue

CMD ["python", "manage.py", "runserver"]
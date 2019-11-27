FROM python:3.6-alpine

LABEL maintainer="eadwinCode" 

RUN apk update && apk upgrade && \
    echo "**** other packages *****" && \
    apk add --update npm && \
    apk add --virtual build-deps && \
    apk add --no-cache \
        sqlite \
        python3-dev \
        libpq \
        gcc\
        musl-dev\
    && apk del build-deps 
    

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

WORKDIR /home/docker/code

ADD requirements.txt /home/docker/code
ADD package.json /home/docker/code

RUN pip install --no-cache-dir -r requirements.txt
RUN npm install && npm install -g parcel

COPY . /home/docker/code/

EXPOSE 80

CMD ["python", "manage.py", "runserver"]

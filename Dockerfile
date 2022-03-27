# base image
FROM python:3.10-alpine

# # install gcc
RUN apk update && apk upgrade
RUN apk add --no-cache \
                    gcc \
                    musl-dev \
                    linux-headers \
                    python3-dev \
    && rm -rf /var/cache/apk/*

# configure env var
ARG DOCKER_TAG
ENV APP_VERSION=$DOCKER_TAG
ENV TZ="Asia/Jakarta"

# setup working directory
WORKDIR /trial-app

# copy requirement file
COPY requirements.txt .

# install packages
RUN pip3 install -r requirements.txt

# copy the codes
COPY . .

# set env var
ENV FLASK_APP=app

# expose port
EXPOSE 5000

# configure command
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
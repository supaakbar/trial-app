# base image
FROM python:3.10-alpine

# configure app version
ARG DOCKER_TAG
ENV APP_VERSION=$DOCKER_TAG

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
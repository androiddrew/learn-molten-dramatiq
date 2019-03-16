# base image
FROM python:3.7.2-alpine3.9

# Set environmental variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory
WORKDIR /usr/local/src/app

# add requirements
COPY ./requirements.txt /usr/local/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/local/src/app
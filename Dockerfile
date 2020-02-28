# Base Image
FROM python:3.7

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
	    python3 \
        python3-pip \
        python-virtualenv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ALTERA VERSÃO DEFAULT DO PYTHON PARA A 3.7
RUN ln -sf /usr/bin/python3.7 /usr/bin/python

EXPOSE 8888

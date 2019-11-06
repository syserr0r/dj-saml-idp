# Dockerfile that creates the build and test environment, providing
# both Python 2.7 and 3.7. It also allows sshd to be run
# to better support development and test under IDEs.
FROM ubuntu:bionic-20190912.1
MAINTAINER Mobify <ops@mobify.com>

EXPOSE 4322

RUN apt-get -qq update && apt-get -yf autoremove
RUN apt-get install -y --no-install-recommends \
        sudo curl wget swig apt-utils less unzip \
        software-properties-common gpg-agent \
        build-essential \
        libssl-dev \
        python python-dev swig python-pip \
        python3.7 python3.7-dev python3-venv python3-dev python3.7-venv \
        && \
    apt-get -q -y upgrade && \
    apt-get clean

# Install Python virtualenv and pip. For python 3.7,
# the equivalent command to `virtualenv` is `python3 -m venv`.
RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && \
    python /tmp/get-pip.py && \
    rm -f /tmp/get-pip.py && \
    pip install --no-cache virtualenv && \
    rm -rf ~/.cache/pip/ && \
    rm -rf /tmp/* && apt-get clean

ADD . /app
WORKDIR /app

RUN virtualenv /venv27 && \
    /venv27/bin/pip install --cache-dir ~/.pip27 wheel -r requirements-dev.txt

RUN python3.7 -m venv /venv37 && \
    /venv37/bin/pip3 install --cache-dir ~/.pip37 wheel -r requirements-dev.txt

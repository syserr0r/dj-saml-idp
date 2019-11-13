#!/usr/bin/env bash
# Script used to start a sshd in a docker container. Allows logins as `root`
# using the password `gomobile. This script should be run as the `docker` user.
set -ue

PASSWORD='gomobile'

sudo apt-get install -y -q --no-install-recommends openssh-server

sudo /bin/bash -c  "echo 'root:$PASSWORD' | /usr/sbin/chpasswd"
sudo /bin/bash -c  "mkdir -p /var/run/sshd && cp /app/docker/sshd_config /etc/ssh/sshd_config"
echo "USING IP: " /sbin/ifconfig eth0 | grep "inet addr" | awk -F: '{print $2}' | awk '{print $1}'

# SSH wipes the env variables, we need to work around that by storing the
# variables in /etc/environment
# https://github.com/docker/docker/issues/2569#issuecomment-27973910
env | sudo /bin/bash -c  "(grep _ >> /etc/environment) && /usr/sbin/sshd -D -e"

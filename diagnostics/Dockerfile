FROM debian:buster-slim

WORKDIR /var/

RUN apt-get update && \
apt-get -y install \
python3-minimal \
nginx \
i2c-tools \
--no-install-recommends && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

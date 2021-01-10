FROM debian:buster-slim

WORKDIR /opt/nebraDiagnostics/

RUN apt-get update && \
apt-get -y install \
python3-minimal \
nginx \
i2c-tools \
usbutils \
python3-qrcode \
--no-install-recommends && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*


COPY diagnosticsProgram.py diagnosticsProgram.py

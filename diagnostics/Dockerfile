FROM debian:buster-slim

WORKDIR /opt/nebraDiagnostics/

RUN apt-get update && \
apt-get -y install \
python3-minimal \
i2c-tools \
usbutils \
python3-qrcode \
--no-install-recommends && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

RUN mkdir html
COPY diagnosticsProgram.py diagnosticsProgram.py
COPY genHTML.py genHTML.py

#ENTRYPOINT ["python3", "-m http.server 80"]

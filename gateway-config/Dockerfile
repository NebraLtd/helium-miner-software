#Yeet
#Packet Forwarder Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.

FROM ubuntu:20.04

WORKDIR /opt/

RUN apt-get update && \
apt-get -y install \
python3-minimal \
python3-networkmanager \
bluez \
libdbus-1-3 \
dbus \
git \
ca-certificates \
net-tools \
python3-dbus \
python3-gi \
python3-protobuf \
python3-pip \
--no-install-recommends && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

ARG doge=202101151828
RUN git clone https://github.com/NebraLtd/helium-miner-config.git


ENTRYPOINT ["python3", "/opt/helium-miner-config/main.py"]

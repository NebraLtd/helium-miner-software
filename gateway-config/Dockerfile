#Yeet
#Packet Forwarder Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.

FROM debian:buster-slim

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

COPY start-gateway-config.sh start-gateway-config.sh
RUN chmod +x start-gateway-config.sh
RUN git clone https://github.com/NebraLtd/helium-miner-config.git

WORKDIR /opt/helium-miner-config/

ENTRYPOINT ["sh", "/opt/helium-miner-config/start-gateway-config.sh"]

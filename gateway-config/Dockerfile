#Yeet
#Packet Forwarder Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.

FROM debian:buster-slim

WORKDIR /opt/

RUN apt-get update
RUN apt-get -y install \
python3-minimal \
python3-networkmanager \
bluez \
libdbus-1-3 \
dbus \
git \
net-tools
--no-install-recommends

RUN git clone https://github.com/NebraLtd/helium-miner-config.git


#ENTRYPOINT ["sh", "/opt/iotloragateway/packet_forwarder/run_pkt.sh"]

#Yeet
#Packet Forwarder Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.

FROM debian:buster-slim

WORKDIR /opt/gateway_config/

RUN apt-get update && apt-get -y install \
libprotobuf-c1 \
python3-minimal \
python3-yaml \
python3-networkmanger \
--no-install-recommends && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*


#ENTRYPOINT ["sh", "/opt/iotloragateway/packet_forwarder/run_pkt.sh"]

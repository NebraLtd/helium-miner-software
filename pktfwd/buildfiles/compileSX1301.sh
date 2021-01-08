#! /bin/bash

mkdir -p /opt/iotloragateway
mkdir -p /opt/iotloragateway/dev
mkdir -p /var/www/iotloragateway
cd /opt/iotloragateway/dev

git clone https://github.com/NebraLtd/lora_gateway.git
git clone https://github.com/NebraLtd/packet_forwarder.git

cd /opt/iotloragateway/dev/lora_gateway/libloragw
make clean
make -j 4

echo "Packet Forwarder"
cd /opt/iotloragateway/dev/packet_forwarder/
make clean
make -j 4
cp /opt/iotloragateway/dev/packet_forwarder/lora_pkt_fwd/lora_pkt_fwd /opt/iotloragateway/packetforwarder/

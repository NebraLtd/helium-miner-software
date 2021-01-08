#! /bin/bash

mkdir -p /opt/iotloragateway
mkdir -p /opt/iotloragateway/dev
mkdir -p /var/www/iotloragateway
cd /opt/iotloragateway/dev

git clone https://github.com/PiSupply/lora_gateway.git
git clone https://github.com/PiSupply/paho.mqtt.embedded-c.git
git clone https://github.com/PiSupply/ttn-gateway-connector.git
#git clone https://github.com/PiSupply/protobuf-c.git
git clone https://github.com/PiSupply/packet_forwarder.git
git clone https://github.com/PiSupply/iot-lora-controller.git

cd /opt/iotloragateway/dev/lora_gateway/libloragw
make clean
sed -i -e 's/PLATFORM= .*$/PLATFORM= iotloragw_standalone0/g' library.cfg
make -j 4


cd /opt/iotloragateway/dev/paho.mqtt.embedded-c
make -j 4
make install

echo "TTN Connector"
cd /opt/iotloragateway/dev/ttn-gateway-connector
cp config.mk.in config.mk
make -j 4
cp /opt/iotloragateway/dev/ttn-gateway-connector/bin/libttn-gateway-connector.so /usr/lib


echo "Packet Forwarder"
cd /opt/iotloragateway/dev/packet_forwarder/mp_pkt_fwd
make clean
git checkout docker-sg0
make -j 4
cp /opt/iotloragateway/dev/packet_forwarder/mp_pkt_fwd/mp_pkt_fwd /opt/iotloragateway/packetforwarder_sg0

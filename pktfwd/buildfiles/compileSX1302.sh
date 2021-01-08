#! /bin/bash

mkdir -p /opt/iotloragateway
mkdir -p /opt/iotloragateway/dev
cd /opt/iotloragateway/dev

git clone https://github.com/NebraLtd/sx1302_hal.git

cd /opt/iotloragateway/dev/sx1302_hal
make clean
make -j 4

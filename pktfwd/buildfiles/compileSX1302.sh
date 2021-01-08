#! /bin/bash

cd /opt/iotloragateway/dev

#git clone https://github.com/NebraLtd/sx1302_hal.git
wget https://github.com/NebraLtd/sx1302_hal/archive/V1.0.5.tar.gz
tar -xzvf V1.0.5.tar.gz

cd /opt/iotloragateway/dev/sx1302_hal-1.0.5

#Remove old files

make clean
make -j 4

# helium-miner-software
Software for Nebra Helium Miners

This dockerfile creates 4 containers.

## Diagnostics

Basic container that runs a webserver to provide diagnostics information & manufacutring tools

https://github.com/NebraLtd/hm-diag

## Packet Forwarder

The container that has the code that configures the packet forwarder's region and starts the radio module.

https://github.com/NebraLtd/hm-pktfwd

## Gateway-config

The container that has the code to provide the Bluetooth LE to allow the hotspot to be configured via the Helium App.

https://github.com/NebraLtd/hm-config

## Miner

The Helium Miner with the required configuration files added.

https://github.com/NebraLtd/hm-miner

## eccprog

This software contains the tool which configures the ECC Key in production and isn't run again after.

# Credits



This software uses a mixture of information from:
* https://github.com/just4give/helium-dyi-hotspot-balena-pi4
* https://github.com/jpmeijers/ttn-resin-gateway-rpi
* https://github.com/PiSupply/iot-lora-gw-pktfwd

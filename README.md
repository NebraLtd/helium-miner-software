# helium-miner-software
Software for Nebra Helium Miners

This dockerfile creates 6 containers.

## diagnostics

Basic container that runs a webserver to provide diagnostics information & manufacutring tools

https://github.com/NebraLtd/hm-diag

## packet-forwarder

The container that has the code that configures the packet forwarder's region and starts the radio module.

https://github.com/NebraLtd/hm-pktfwd

## gateway-config

The container that has the code to provide the Bluetooth LE to allow the hotspot to be configured via the Helium App.

https://github.com/NebraLtd/hm-config

## helium-miner

The Helium Miner with the required configuration files added.

https://github.com/NebraLtd/hm-miner

## gwmfr

This software contains the tool which configures the ECC Key in production and isn't run again after.

https://github.com/NebraLtd/hm-gwmfr

## upnp

This container attempts to use UPnP to set up a port forwarding rule, if your router supports it and the function is turned on in your router settings.

https://github.com/NebraLtd/hm-upnp

# Credits



This software uses a mixture of information from:
* https://github.com/just4give/helium-dyi-hotspot-balena-pi4
* https://github.com/jpmeijers/ttn-resin-gateway-rpi
* https://github.com/PiSupply/iot-lora-gw-pktfwd

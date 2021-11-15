# Helium Miner Software

This repository includes the main [docker-compose.yml](https://github.com/NebraLtd/helium-miner-software/blob/master/docker-compose.yml) file that powers the Nebra miners.

The `docker-compose.yml` file is pushed to [Balena](https://www.balena.io/) (using GitHub Actions), which in turn pulls down the various Docker images outlined below.

There are currently six different services running within this device, which are all outlined below.

## Diagnostics

Repo: [github.com/NebraLtd/hm-diag](https://github.com/NebraLtd/hm-diag)

The diagnostics container is designed for local troubleshooting. It runs a local web server that displays various diagnostics data.

Note that this container is also responsible for serving content to the [Hotspot-Production-Tool](https://github.com/NebraLtd/Hotspot-Production-Tool) and also contains the [gateway-mfr-rs](https://github.com/helium/gateway-mfr-rs) tool which configures the ECC Key in production.

## Packet Forwarder

Repo: [github.com/NebraLtd/hm-pktfwd](https://github.com/NebraLtd/hm-pktfwd)

This container is responsible for configuring packet forwarder's region and starts the radio module.

## Gateway Config

Repo: [github.com/NebraLtd/hm-config](https://github.com/NebraLtd/hm-config)

This container is (partially) responsible for the device onboarding and provides the Bluetooth LE to allow the hotspot to be configured via the Helium App. It is also responsible for configuring WiFi.

## Helium Miner

Repo: [github.com/NebraLtd/hm-miner](https://github.com/NebraLtd/hm-miner)

This container is the actual Helium Miner software (from upstream), with the required configuration files added.

## UPnP

Repo: [github.com/NebraLtd/hm-upnp](https://github.com/NebraLtd/hm-upnp)

This container attempts to use UPnP to set up a port forwarding rule, if your router supports it and the function is turned on in your router settings.

## DBus Session

Repo: [github.com/balenablocks/dbus](https://github.com/balenablocks/dbus)

This container configures a DBus session bus instance that is used by the gateway config container to communicate with the miner code (note that there is also a separate system bus running on the host OS which is used by gateway config to communicate with bluez for configuring Bluetooth services). This removes the need to have a custom `com.helium.Miner.conf` dbus config file on the host OS as was done previously (and meant we had to run a custom balena device type).

#  Quick Start

This is a guide to help you get started with the repository and get it running on your local device. This guide is focused on pushing the repository onto a Raspberry Pi using Balena.

**Prerequisites:**
- Local Test Device (Ex: Raspberry Pi)
- Computer for development and pushing to the device
- Git installed - [download here](https://git-scm.com/downloads)
- [Balena CLI](https://github.com/balena-io/balena-cli) (Install located on Balena step in quick start steps below)

### Quick Start Steps

**Step 1:** Clone the repository to your local machine using one of the following commands:
- HTTP: `git clone https://github.com/NebraLtd/helium-miner-software.git`
- SSH: `git clone git@github.com:NebraLtd/helium-miner-software.git`

**Step 2:** Follow the [getting started guide](https://www.balena.io/docs/learn/getting-started/raspberrypi3/nodejs/) for Balena to help you install Balena on your local test device and get a fleet setup so you can start pushing code to it.

**Step 3:** Once you've gone through the steps and have Balena setup with your device in your fleet, open your cli terminal and navigate to the root directory of the cloned repository (Ex: /usr/name/documents/helium-miner-software).

**Step 4:** Once you're at the root directory. You want to push the code by running the following command:
```bash
$ balena push <fleet-name>
```

**Step 5:** Once complete check your fleet on the Balena dashboard and all modules should be running on the local test device.

# Device Configuration / Fleet Configuration Notes

For some Nebra Hotspots that use spidev1.2 you may need to add a DT overlay in the device or fleet configuration section on balenaCloud to enable spi1.

Additionally, for the SPI ethernet based Nebra Light Hotspot you need to add the DT overlay for the enc28j60. And for UART based GPS that is on non-standard UART pins you need to add the uart dtoverlay.

To do this you need to find the "Define DT Overlays" section, click activate and then add `"enc28j60","spi1-3cs","uart0,txd0_pin=32,rxd0_pin=33,pin_func=7"`

# CI/CD Notes

GitHub Actions is used to deploy directly to Balena.

The [master branch](https://github.com/NebraLtd/helium-miner-software) is mapped to "Testnet" (i.e. our staging environment), and
the [production branch](https://github.com/NebraLtd/helium-miner-software/tree/production) is mapped to the production environments.

Do note that the Docker Tag is hard coded in the `docker-compose.yml` file.

# Production Checks

@TODO:
* Write more comprehensive QA/QC checklist, including how to QA the onboarding part
* Write automated health checks for post deploys

Typically before merging into production the following checks are performed:

- Containers are updated on the master branch to versions ready to be deployed.
- This is deployed automatically to devices on the testnet.
- Open a PR from master to production branch.
- Typically leave in testnet for at least 3 Hours to see if any issues are reported from testnet users.
- Check to see if units on testnet are still synced, beaconing & witnessing as expected. (Typically Teeny Felt Rook & Gigantic Basil Turtle are good choices to check due to their locations)
- If all looks good, merge into production branch and monitor updates on balena dashboard.

# Credits

This software uses a mixture of information from:
* https://github.com/just4give/helium-dyi-hotspot-balena-pi4
* https://github.com/jpmeijers/ttn-resin-gateway-rpi
* https://github.com/PiSupply/iot-lora-gw-pktfwd

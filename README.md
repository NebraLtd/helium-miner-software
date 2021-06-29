# Helium Miner Software

This repository includes the main [docker-compose.yml](https://github.com/NebraLtd/helium-miner-software/blob/master/docker-compose.yml) file that powers the Nebra miners.

The `docker-compose.yml` file is pushed to [Balena](https://www.balena.io/) (using GitHub Actions), which in turn pulls down the various Docker images outlined below.

There are currently six different services running within this device, which are all outlined below.

## Diagnostics

Repo: [github.com/NebraLtd/hm-diag](https://github.com/NebraLtd/hm-diag)

The diagnostics container is designed for local troubleshooting. It runs a local web server that displays various diagnostics data.

Note that this container is also responsible for serving content to the [Hotspot-Production-Tool](https://github.com/NebraLtd/Hotspot-Production-Tool).

## Packet Forwarder

Repo: [github.com/NebraLtd/hm-pktfwd](https://github.com/NebraLtd/hm-pktfwd)

This container is responsible for configuring packet forwarder's region and starts the radio module.

## Gateway Config

Repo: [github.com/NebraLtd/hm-config](https://github.com/NebraLtd/hm-config)

This container is (partially) responsible for the device onboarding and provides the Bluetooth LE to allow the hotspot to be configured via the Helium App. It is also responsible for configuring WiFi.

## Helium Miner

Repo: [github.com/NebraLtd/hm-miner])https://github.com/NebraLtd/hm-miner)

This container is the actual Helium Miner software (from upstream), with the required configuration files added.

## gwmfr

Repo: [github.com/NebraLtd/hm-gwmfr](https://github.com/NebraLtd/hm-gwmfr)

This software contains the tool which configures the ECC Key in production and isn't run again after.

## UPnP

Repo: [github.com/NebraLtd/hm-upnp](https://github.com/NebraLtd/hm-upnp)

This container attempts to use UPnP to set up a port forwarding rule, if your router supports it and the function is turned on in your router settings.

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

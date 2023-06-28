# Helium Miner Software

This repository generates the main docker-compose.yml (follow the steps to generate this [here](#generating-docker-compose-file)) file that powers the Nebra miners.

The `docker-compose.yml` file is pushed to [Balena](https://www.balena.io/) (using GitHub Actions), which in turn pulls down the various Docker images outlined below.

There are currently five different services running within this device, which are all outlined below.

## Diagnostics

Repo: [github.com/NebraLtd/hm-diag](https://github.com/NebraLtd/hm-diag)

The diagnostics container is designed for local troubleshooting. It runs a local web server that displays various diagnostics data.

Note that this container is also responsible for serving content to the [Hotspot-Production-Tool](https://github.com/NebraLtd/Hotspot-Production-Tool) and also contains the [gateway-mfr-rs](https://github.com/helium/gateway-mfr-rs) tool which configures the ECC Key in production.

## Multiplexer

Repo: [github.com/NebraLtd/hm-multiplexer](https://github.com/NebraLtd/hm-multiplexer)

This container is a multiplexer which receives the ouput from the lora gateway packet forwarder and forwards it to a variety of relevant services such as the helium miner, ThingsIX and The Things Network.

## Packet Forwarder

Repo: [github.com/NebraLtd/hm-pktfwd](https://github.com/NebraLtd/hm-pktfwd)

This container is responsible for configuring packet forwarder's region and starts the radio module.

## Gateway Config

Repo: [github.com/NebraLtd/hm-config](https://github.com/NebraLtd/hm-config)

This container is (partially) responsible for the device onboarding and provides the Bluetooth LE to allow the hotspot to be configured via the Helium App. It is also responsible for configuring WiFi.

As of 27th Jan 2022, we have also moved the UPnP functionality into this repo instead of the (now archived) [UPnP repo](https://github.com/NebraLtd/hm-upnp). This attempts to use UPnP to set up a port forwarding rule if your router supports it and the function is turned on in your router settings. This is possible in hm-config because we already use "host networking" in this container.

Removing the UPnP container reduces CPU overhead and redundant code.

As of the 2022.12.13.0-4 firmware version, UPnP has been removed from the miners entirely as it is no longer necessary to open ports on the miner after the move to gateway-rs upstream.

## Helium Gateway-rs

Repo: [github.com/NebraLtd/hm-gatewayrs](https://github.com/NebraLtd/hm-gatewayrs)

This container is the actual Helium Gateway-rs software (from upstream), with the required configuration files added.

Gatewayrs container requires two IP ports exposed as default.
- [1680](https://github.com/helium/gateway-rs/blob/d6e140fc8f102d2e1008ddf6d58cef32c4f60392/src/settings.rs#L18): For connecting to packet-forwarder.
- [4467](https://github.com/helium/gateway-rs/blob/d6e140fc8f102d2e1008ddf6d58cef32c4f60392/src/settings.rs#L22): For connecting to gRPC API over WAN.

Both of these ports can be changed via settings (toml) file.

#  Quick Start

This is a guide to help you get started with the repository and get it running on your local device. This guide is focused on pushing the repository onto a Raspberry Pi using Balena.

**Prerequisites:**
- Local Test Device (Ex: Raspberry Pi)
- Computer for development and pushing to the device
- Git installed - [download here](https://git-scm.com/downloads)
- [Balena CLI](https://github.com/balena-io/balena-cli) (Install located on Balena step in quick start steps below)

### Generating Docker Compose File

This is used for deploying locally, it automatically generates one for each device as part of the github workflow.

You may notice that after cloning the repo that you are missing a docker-compose.yml file which is required to push the containers to balena. This is a result of us generating the docker-compose file based on a settings.ini file in the root directory. You can also find the latest docker-compose files used in production in the [device-compose-files folder](https://github.com/NebraLtd/helium-miner-software/tree/master/device-compose-files) (generated via github workflow). Here are the steps of generating a new docker-compose.yml file:

*Note for generating the file for local tests: The repo's short Git SHA is fetched from GitHub pipeline automatically while working with standard procedure. But if you need to test your working copy locally, you need to create an environment variable first via running following command on Linux:*

```sh
$ export FIRMWARE_SHORT_HASH=$(git rev-parse --short HEAD)
```

*Then generate the docker compose file in the same console with following procedures.*

**Step 1:** Update the settings.ini file to accept the new values which you wish to set in the generation of the docker-compose.yml file

**Step 2:** Generate your respective .yml file based on the device you will be pushing to:
- RPI (Raspberry Pi based device): `python gen_docker_compose.py rpi -o device-compose-files/docker-compose-rpi.yml`
- ROCKPI (ROCK Pi based device): `python gen_docker_compose.py rockpi -o device-compose-files/docker-compose-rockpi.yml`

**Step 3:** Copy device compose file into root directory as docker-compose.yml:
- RPI: `cp device-compose-files/docker-compose-rpi.yml ./docker-compose.yml`
- ROCKPI: `cp device-compose-files/docker-compose-rockpi.yml ./docker-compose.yml`

**Step 4:** Validate that the changed values you applied to settings.ini were applied in the docker-compose.yml file

**Step 5:** Continue with the steps below to push the containers to your fleet via balena

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

## Balena deploy builds

Whilst in theory you can run matrix builds to build to several balena fleets simultaneously using GitHub Actions we found (at the time of writing - December 2021) that this did not perform satisfactorily in practice. We deploy on a production release now to 16 separate fleets meaning 16 separate builds triggered via the balena API simultaneously. Somewhere between 50 and 100% of the builds would fail each time.

We have discovered a useful fix for this using the following two workarounds:
- use [multiple API keys](https://github.com/NebraLtd/helium-miner-software/pull/301) within the action to avoid any rate limiting or timeout issues.
- add random periods of delay to each matrix action run using using a [random sleep on the command line](https://github.com/NebraLtd/helium-miner-software/pull/300) within the action.

This has allowed our builds to continue deploying successfully.

## Dealing with failed builds

On occasion (as originally described [in this issue](https://github.com/NebraLtd/helium-miner-software/issues/293)) CI/CD builds via GitHub actions will fail to push correctly to balena. We have found that as a workaround, it is often possible to force push these to balena as draft releases using the `--draft` tag in the `balena deploy` command of the balena CLI tool. For example:

```
balena deploy nebraltd/helium-indoor-868 --logs --debug --nocache --build --draft
```

This can either be done manually by someone with the right privileges on our balenaCloud account, or it can be done by triggering the `workflow_dispatch:` event on the [push-to-prod-draft.yml github action](https://github.com/NebraLtd/helium-miner-software/blob/master/.github/workflows/push-to-prod-draft.yml) from the GitHub actions menu (making sure to use the production branch). There is also an equivalent action for our [testnet fleet](https://github.com/NebraLtd/helium-miner-software/blob/master/.github/workflows/push-to-testnet-draft.yml).

Once this has completed and the draft builds have been pushed to balena, you will need to either finalise the releases using balena CLI locally, or visit the releases menu of each fleet with a draft release, click on the release and then select `Finalize Release` from the dropdown menu.

# [NebraHub](https://nebra.com) builds (OpenFleets) for Nebra and third party Helium Miners

We are passionate about open source hardware and software and so we have put significant time and effort into making our software hardware agnostic, and a number of Helium manufacturers already use parts of our software on their devices. On that note, we maintain a variety of fully open source software builds for third party Helium Miners, as well as our Nebra miners. If you follow the links to the various repos below, you can find the builds and detailed instructions on how to deploy them on your [Nebra](#nebra-build-repos) or [third party hotspot miner](#third-party-build-repos).

Not only does this further decentralise the software stack, but also future proofs the Helium network and the hotspot owners from their devices becoming obsolete from manufacturers going bankrupt or being unreliable with ongoing updates.

This is the same full featured software that we run natively on our Nebra Helium Miners...

**Key features:**

- local IP diagnostics dashboard
- updated regularly (our automated system means this will get updates at the same time as the entire Nebra fleet)
- automatic updates (if installed via [NebraHub builds](#nebra-build-repos)) or option to [fork and manage your own fleet](#balenahub-app-builds)
- powered by [balenaOS](https://balena.io/os) which is optimised for edge devices and very secure
- access to new features as added to the core Nebra software
- fully open source software stack (the only one in the Helium community!)
- COMING SOON: access to [remote management dashboard](https://dashboard.nebra.com) and multi-mining (paid extra)

In the future, we also plan to add [Nebra dashboard](https://dashboard.nebra.com) support for third party miners (including multi-mining features). We also plan to apply for a Helium Foundation grant in order to expand this effort further, improve the software and add all currently available Helium Miners to the mix.

**If you have found this software useful we would be very grateful if you would consider [sponsoring the project via GitHub Sponsors](https://github.com/sponsors/NebraLtd) as this will enable us to continue supporting this software into the future.**

### Nebra build repos

- [Indoor (470, 868 and 915)](https://github.com/NebraLtd/helium-nebra-indoor1)
- [Outdoor (470, 868 and 915)](https://github.com/NebraLtd/helium-nebra-outdoor1)
- [ROCK Pi Indoor (470, 868 and 915)](https://github.com/NebraLtd/helium-nebra-indoor2)
- [ROCK Pi Outdoor (470, 868 and 915)](https://github.com/NebraLtd/helium-nebra-outdoor2)

### Third party build repos

- [RAKwireless / MNTD (RAK v1.5, RAK v2, MNTD)](https://github.com/NebraLtd/helium-rak)
- [Sensecap (M1)](https://github.com/NebraLtd/helium-sensecap)
- [Controllino / Conelcom](https://github.com/NebraLtd/helium-controllino)
- [Pisces (P100)](https://github.com/NebraLtd/helium-pisces)
- [Linxdot (RasPi CM4 version)](https://github.com/NebraLtd/helium-linxdot)
- [Linxdot (ROCK / Radxa CM3 version)](https://github.com/NebraLtd/helium-linxdot-rkcm3)
- [Helium OG (RasPi 3 and RasPi 4 version)](https://github.com/NebraLtd/helium-og)
- [Pycom (RasPi CM4 version)](https://github.com/NebraLtd/helium-pycom)
- [Cotx (X3)](https://github.com/NebraLtd/helium-cotx)
- [Syncrobit (RasPi CM4 version)](https://github.com/NebraLtd/helium-syncrobit)
- [Syncrobit (ROCK / Radxa CM3 version)](https://github.com/NebraLtd/helium-syncrobit-rkcm3)
- [Panther (X1)](https://github.com/NebraLtd/helium-pantherx1)
- [Finestra / Mimiq](https://github.com/NebraLtd/helium-finestra)
- [Rising HF](https://github.com/NebraLtd/helium-risinghf)
- [Midas](https://github.com/NebraLtd/helium-midas)
- [Bobcat](https://github.com/NebraLtd/helium-bobcat-px30)

Are you a hotspot manufacturer that wants to add support for your existing or upcoming hotspots? A hotspot owner wanting to help add support for aditional hardware variants? We are always looking to add additional devices here and would be more than happy to discuss integration and collaboration. We also accept contributions and you can read more about how to contribute [below](#how-to-add-new-type-of-hotspots). If you have any questions or want to discuss this in more detail then please reach out to us via [GitHub Issues](https://github.com/NebraLtd/helium-miner-software/issues) or by creating a ticket on [our support site](https://support.nebra.com).

# [BalenaHub](https://hub.balena.io) App builds

**Please note: this method requires you to have a [balenaCloud](https://dashboard.balena-cloud.com/login) account and will also require you to manage OTA updates yourself - either manually or using a fork of our automated scripts which are available in the repos linked above. For most people, unless you are fairly technically proficient (experience with Docker, GitHub, Linux Terminal etc), we recommend you use our [NebraHub builds](#nebra-build-repos) instead of these DIY Balena builds.**

We also maintain [app builds on balenaHub](https://hub.balena.io/apps) with the ability to one-click-deploy to your own self-managed fleet. This does require you to have your own [balenaCloud](https://dashboard.balena-cloud.com/login) account (free for first 10 devices) and will also require you to manage OTA updates yourself - either manually or using a fork of our automated scripts which are available in the repos linked above. However, while it lacks some automation and convenience, it does give you more considerably more flexibility and control over your devices.

You can visit [balenaHub apps page](https://hub.balena.io/apps) and search for `helium` or for the name of your hotspot manufacturer (such as `cotx` or `sensecap`) and you should find our apps. You can then click on the `Deploy` button to begin the deployment. We also have direct links to these builds below to save you some time. We also provide links to instantly deploy these builds directly in the GitHub repos linked in [the above section](#nebrahub-builds-openfleets-for-nebra-and-third-party-helium-miners).

### Nebra balenaHub App build repos

- [Indoor (470, 868 and 915)](https://hub.balena.io/apps/2033013/helium-nebra-indoor1-app)
- [Outdoor (470, 868 and 915)](https://hub.balena.io/apps/2033015/helium-nebra-outdoor1-app)
- [ROCK Pi Indoor (470, 868 and 915)](https://hub.balena.io/apps/2033014/helium-nebra-indoor2-app)
- [ROCK Pi Outdoor (470, 868 and 915)](https://hub.balena.io/apps/2033014/helium-nebra-outdoor2-app)

### Third party balenaHub App build repos

- [RAKwireless / MNTD (RAK v1.5, RAK v2, MNTD)](https://hub.balena.io/apps/2025882/helium-rak-app)
- [Sensecap (M1)](https://hub.balena.io/apps/2025884/helium-sensecap-app)
- [Controllino / Conelcom](https://hub.balena.io/apps/2025878/helium-controllino-app)
- [Pisces (P100)](https://hub.balena.io/apps/2025889/helium-pisces-app)
- [Linxdot (RasPi CM4 version)](https://hub.balena.io/apps/2025883/helium-linxdot-app)
- [Linxdot (ROCK / Radxa CM3 version)](https://hub.balena.io/apps/2025890/helium-linxdot-rkcm3-app)
- [Helium OG (RasPi 3 and RasPi 4 version)](https://hub.balena.io/apps/2025877/helium-og-app)
- [Pycom (RasPi CM4 version)](https://hub.balena.io/apps/2025822/helium-pycom-app)
- [Cotx (X3)](https://hub.balena.io/apps/2025887/helium-cotx-app)
- [Syncrobit (RasPi CM4 version)](https://hub.balena.io/apps/2025819/helium-syncrobit-app)
- [Syncrobit (ROCK / Radxa CM3 version)](https://hub.balena.io/apps/2025891/helium-syncrobit-rkcm3-app)
- [Panther (X1)](https://hub.balena.io/apps/2025892/helium-pantherx1-app)
- [Finestra / Mimiq](https://hub.balena.io/apps/2025881/helium-finestra-app)
- [Rising HF](https://hub.balena.io/apps/2025888/helium-risinghf-app)
- [Midas](https://hub.balena.io/apps/2025879/helium-midas-app)

**If you have found this software useful we would be very grateful if you would consider [sponsoring the project via GitHub Sponsors](https://github.com/sponsors/NebraLtd) as this will enable us to continue supporting this software into the future.**

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

# How To Add New Type Of Hotspots
Please refer to [this](https://github.com/NebraLtd/helium-miner-software/blob/master/how_to_add_new_hotspot.md) guide for more information.

# Credits

This software uses a mixture of information from:
* https://github.com/just4give/helium-dyi-hotspot-balena-pi4
* https://github.com/jpmeijers/ttn-resin-gateway-rpi
* https://github.com/PiSupply/iot-lora-gw-pktfwd

# Sponsor Us!

If you have found this software useful (especially if you are using it on a third party hotspot!) we would be very grateful if you would consider [sponsoring the project via GitHub Sponsors](https://github.com/sponsors/NebraLtd) as this will enable us to continue supporting this software into the future.

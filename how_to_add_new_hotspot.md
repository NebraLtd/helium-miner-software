# How To Add A New Hotspot Into Nebra Firmware

The Nebra firmware stack has been designed to support various different architectures and vendors. Hence it is very flexible by design. But this also gives the developers a responsibility about supplying correct hardware configuration.

This configuration information has to be supplied in different places of the stack. Let's review them one by one.

## Checklist for adding a new hotspot type

* Add variant into `variant_definitions` in hm-pyhelper repository
* Create custom inputs (e.g. additional buttons) and outputs (e.g. additional LED's) in the new variant and update the logic in other repositories if necessary.
* Release and publish it via CI/CD pipeline
* Bump hm-pyhelper for hm-pktfwd, hm-diag and hm-config repositories and push them to create necessary docker images (could take a while) (Example [pull request](https://github.com/NebraLtd/hm-config/pull/169) for hm-config in such case)
* Create related production Balena fleets (will be called just fleets from now on) as "helium-<device_type>-[variant]-[frequency]-[user]" (parameters in brackets are optional)
* Edit configuration parameters of the fleet
* Add `VARIANT` and `FREQ` environment variables into fleet variables
* Update automation steps in this repository for newly created fleets
* Add sentry environment variables into fleet variables
* Modify `generate-images.sh` from NebraLtd/hotspot-production-images repo root.
* Modify `generate-urls.sh` from NebraLtd/hotspot-production-images repo root.
* Modify `generate-images.yml` from NebraLtd/hotspot-production-images repo under `.github/workflows` folder.
* Modify `settings.ini` file if necessary

## Defining the variant in hm-pyhelper project and releasing it

As its name suggests, the NebraLtd/hm-pyhelper repository is designed as a helper library and is not a directly executable container project. It is used in various projects as a library and hence needs to be published to pypi.org to make a change effective in other projects. Thankfully it is automatically updated with the help of our CI/CD pipeline.

The first task would be creating a variant in [`variant_definitions`](https://github.com/NebraLtd/hm-pyhelper/blob/06a752a196e05a602506db1b779a5fa62fd55f3d/hm_pyhelper/hardware_definitions.py#L31) dictionary from [hardware_definitions.py](https://github.com/NebraLtd/hm-pyhelper/blob/master/hm_pyhelper/hardware_definitions.py) file.

### Example Variant
Here, you can find an example for such variant:

```
'NEBHNT-IN1': {
    'FRIENDLY': 'Nebra Indoor Hotspot Gen 1',
    'APPNAME': 'Indoor',
    'SPIBUS': 'spidev1.2',
    'KEY_STORAGE_BUS': '/dev/i2c-1',
    'RESET': 38,
    'MAC': 'eth0',
    'STATUS': 25,
    'BUTTON': 26,
    'ECCOB': True,
    'TYPE': 'Full',
    'CELLULAR': False,
    'FCC_IDS': ['2AZDM-HNTIN'],
    'CONTAINS_FCC_IDS': ['2AHRD-EPN8531', '2AB8JCSR40', '2ARPP-GL5712UX'],
    'IC_IDS': ['27187-HNTIN'],
    'CONTAINS_IC_IDS': []
    },
```

### Variant Parameters

**Important Note:** GPIO index numbers used for parameters like `BUTTON` or `STATUS` are getting their values from CPU GPIO peripheral. So the developer should not mix them with CPU's or any connectors (like HAT connector) pin numbers. The corresponding GPIO index number of a particular physical pin could be found on the hardware design document of the new hotspot.

#### FRIENDLY
It is the human readable and explanatory name of the device.

#### APPNAME
Explains usage detail

#### SPIBUS
The LoRa concentrator hardware is designed to work on a SPI (Serial Peripheral Interface) Bus. This has to be defined as found in Linux IO device, which should be found in `/dev` path.

#### KEY_STORAGE_BUS
All hotspots has to have a valid cryptography integrated circuit (IC), which is called ECC. This IC works on I2C bus and this parameter is defining the Linux IO device path for this particular I2C bus. Unlike SPIBUS, this path has to be absolute.

#### SWARM_KEY_URI
This is the new format of the ECC device specification [gateway-mfr-rs v0.2.1](https://github.com/helium/gateway-mfr-rs/tree/4c8f7b4b9c488099afd67b32c5951c5049e11a81#addressing).

Format: `ecc:<dev>[:address][?slot=<slot>]`
- dev the device file name (usually begins with i2c or tty)
- address the bus address (default 96)
- slot the slot to use for key lookup/manipulation (default: 0)

#### RESET
This is the GPIO index of the digital output, which is connected to the RF Concentrator chip (e.g. SX1301, SX1302 ...) reset.

For a correct RF Concentrator opearation, the concentrator chip has to be reset between configuration changes. It is reset at the start of the `packet_forwarder` container. This is the primary source of the problem if a concentrator is not functioning as expected.

#### MAC
This parameter defines which network interface is used for MAC (Media Access Control) code. It has to be found in the devices network interfaces.

#### STATUS
This is the hotspots status LED's output GPIO index, which is usually a single green LED on most SBC's.

#### BUTTON
This parameter defines the GPIO input for Bluetooth advertisement start.

Hotspots needed to be accessed via Bluetooth sometimes. Especially at the beginning, onboarding time. But keeping the required Bluetooth interface on all the time imposes two problems. Firstly, it is a security threat and leaks some information to trace the devices. It also effects power consumption negatively as the device is expected to work 7/24.

This input triggers the Bluetooth advertisement process and then the user can access it via Bluetooth interface.

#### ECCOB
Indicates whether the ECC is onboard or not. It is a bool parameter.

#### TYPE
Defines Helium Miner type (e.g. Full, Light etc.)

#### CELLULAR
Defines whether the device has cellular (mobile) hardware or not. It's a bool parameter.

#### FCC_IDS, IC_IDS
ID's given to the device by the regulatory bodies. They are only required for Nebra hotspots as used for label printing in the production.

#### CONTAINS_FCC_IDS, CONTAINS_IC_IDS
The regulatory body ID's which could be found on inner modules like a cellular modem or concentrator module. They are only required for Nebra hotspots as used for label printing in the production.

## Adding automation steps
If the new hotspot type would need a new fleet, as we do right now, it would need some changes on our automation pipeline.

The developer should add necessary steps into the GitHub Action files which could be found [here](https://github.com/NebraLtd/helium-miner-software/tree/master/.github/workflows)

## Modifying settings.ini
The new hotspot could need to define another I2C bus path. Then it needed to be added into the settings.ini file and `gen_docker_compose.py` file needs to be updated, if necessary.

## Defining configuration parameters in the Balena Fleet
A single board computer generally wouldn't have a BIOS due to constraints. Therefore manufacturers like Raspberry Pi Foundation created a clever way to keep boot parameters on the device. For example there is a `config.txt` file under `/boot` for Rasspberry Pi SBC's and it defines the parameters which is cruical to make the device work properly.

In Balena, such critical parameters are defined in Fleet Configuration and passed down to the device. So before adding a new device type into a new fleet configuration parameters need to be set in Fleet Configuration.

## Defining variant and frequency in the Belana Fleet
There are two critical parameters which has to be defined in a Balena Fleet before adding a new device into it.

### VARIANT
This parameter defines which variant will be used in the whole firmware stack. The name is the key from the `variant_definitions` dictionary which is detailed above.

**Example:**
| Name | Value | Service 
|------|-------|--------
| VARIANT | NEBHNT-IN1 | All Services

### FREQ
Like in many things, the world also has been divided about the RF frequency spectrum. So fleets are separated also with their center frequencies because hotspots acts differently regarding to their RF bands.

If this parameter wouldn't be defined in a fleet, the `packet_forwarder` container could not progress further and waits for this parameters in a restart loop.

The expected values are: 470, 868 and 915.

**Example:**
| Name | Value | Service 
|------|-------|--------
| FREQ | 868 | All Services

### HELIUM_MINER_HEIGHT_URL
This parameter is added to test fleets. It is an API endpoint used for fetching current miner height from Stakejoy API. Current value is [this link](https://fuzzy-marmalade-warlock.skittles.stakejoy.com/v1/blocks/height) 

### OVERRIDE_CONFIG_URL
This parameter is added to test fleets. It helps testing new miner configurations. Current value is [this link](https://helium-assets-stage.nebra.com/docker.config)

### Sentry Entries
We use Sentry.io for monitoring the performance and status of our hotspots. Every critical container needs a Sentry API endpoint address.

#### SENTRY_CONFIG
Sentry API endpoint for `gateway_config` container.

#### SENTRY_DIAG
Sentry API endpoint for `diagnostics` container.

#### SENTRY_PKTFWD
Sentry API endpoint for `packet_forwarder` container.


## Modifying hotspot-production-images repo
This repo is used to create production images for the devices. The scripts in the repo could be used with automation pipeline or manually. The YAML files under the `.github/workflows` folder are the CI/CD automation pipeline configurations.

### Modifying generate-images.sh
Usually adding the new device type into [the three lines](https://github.com/NebraLtd/hotspot-production-images/blob/3929275e5fe13950326b9c0f816f1f5d4eedf543/generate-images.sh#L12) should be enough if the new device will need an image for all variant and frequency combinations.

If not, like RAK, then the device should be also included in [the if clause](https://github.com/NebraLtd/hotspot-production-images/blob/3929275e5fe13950326b9c0f816f1f5d4eedf543/generate-images.sh#L301).

If the device needs config.txt injection like our RaspberryPi based miners or RAK, then this should be indicated in [this if clause](https://github.com/NebraLtd/hotspot-production-images/blob/3929275e5fe13950326b9c0f816f1f5d4eedf543/generate-images.sh#L105). Also if it need a different configuration than the default, a new type of `config.txt.<dev_type>` has to be created in root folder and this has to be supplied in [the necessary if clause](https://github.com/NebraLtd/hotspot-production-images/blob/3929275e5fe13950326b9c0f816f1f5d4eedf543/generate-images.sh#L122)

### Modifying generate-urls.sh
This script is used for creating URL's which are posted to our Slack channel. This way, the manufacturer(s) would be able to see the updates automatically and use the most recent one in production. It has be in sync with `generate-images.sh` as the URL's would be pointing the URLs actually created and uploaded by it.

### Modifying generate-images.yml
The CI/CD automation has to be updated for the new device type. Usually addition to the [pipeline matrix](https://github.com/NebraLtd/hotspot-production-images/blob/3929275e5fe13950326b9c0f816f1f5d4eedf543/.github/workflows/generate-images.yml#L16) would be enough. But if it needs special exclusions, like RAK device, then it would be necessary to add those into the [exclude](https://github.com/NebraLtd/hotspot-production-images/blob/3929275e5fe13950326b9c0f816f1f5d4eedf543/.github/workflows/generate-images.yml#L19) section.

## Modifying settings.ini
The necessary `docker-compose.yml` file is created by the `gen_docker_compose.py` script via consuming the parameters from the `settings.ini` file. The current logic includes also a hardware definition for CPU architecture and I2C bus device. It is not strictly necessary to add those if they are equal to an existing option (Like similarity between Nebra RasPi devices and RAK devices).

#Checks basic hardware features.

import os
import qrcode
import json

#Variables for all Checks

ethernetMacAddress = ""
wifiMacAddress = ""
balenaName = ""
rpiSerialNumber = ""
loraTest = False

diagnostics = {
}

#Check the ECC
eccTest = os.popen('i2cdetect -y 1').read()

if "60 --" in eccTest:
    diagnostics["ecc"] = True
else:
    diagnostics["ecc"] = False

#Get ethernet MAC address
try:
    diagnostics["E0"] = open("/sys/class/net/eth0/address").readline().strip()
except:
    diagnostics["E0"] = "FF:FF:FF:FF:FF:FF"


#Get wifi MAC address
try:
    diagnostics["W0"] = open("/sys/class/net/wlan0/address").readline().strip()
except:
    diagnostics["W0"] = "FF:FF:FF:FF:FF:FF"

#Get Balena Name
try:
    diagnostics["BN"] = os.getenv('BALENA_DEVICE_NAME_AT_INIT')
except:
    diagnostics["BN"] = "BALENA-FAIL"

#Get Balena App and therefore Frequency
try:
    diagnostics["BA"] = os.getenv('BALENA_APP_NAME')
except:
    diagnostics["BA"] = "APP-FAIL"

#Get RPi serial number
try:
    diagnostics["RPI"] = open("/proc/cpuinfo").readlines()[38].strip()[10:]
except:
    diagnostics["RPI"] = "FFFFFFFFFFFFFFFF"

#Get USB IDs to check for BT And Modem
usbids = os.popen('lsusb').read()

if "0a12:0001" in usbids:
    diagnostics["BT"] = True
else:
    diagnostics["BT"] = False

if "2c7c:0125" in usbids:
    diagnostics["LTE"] = True
else:
    diagnostics["LTE"] = False

#LoRa Module Test
with open("/var/pktfwd/diagnostics") as diagOut:
    loraStatus = diagOut.read()

print(loraStatus)


print(diagnostics)

diagJson = json.dumps(diagnostics)

with open("/var/pktfwd/diagnostics.json", 'w') as diagOut:
    diagOut.write(diagJson)

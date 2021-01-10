#Checks basic hardware features.

import os

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
    diagnostics["eth0"] = open("/sys/class/net/eth0/address").readline().strip()
except:
    diagnostics["eth0"] = "FF:FF:FF:FF:FF:FF"


#Get wifi MAC address
try:
    diagnostics["wlan0"] = open("/sys/class/net/wlan0/address").readline().strip()
except:
    diagnostics["wlan0"] = "FF:FF:FF:FF:FF:FF"

#Get Balena Name
try:
    diagnostics["name"] = os.getenv('BALENA_DEVICE_NAME_AT_INIT')
except:
    diagnostics["name"] = "BALENA-FAIL"

#Get Balena App and therefore Frequency
try:
    diagnostics["app"] = os.getenv('BALENA_APP_NAME')
except:
    diagnostics["app"] = "APP-FAIL"

#Get RPi serial number
try:
    diagnostics["cpu"] = open("/proc/cpuinfo").readlines()[38].strip()[10:]
except:
    diagnostics["CPU"] = "FFFFFFFFFFFFFFFF"

#Get USB IDs to check for BT And Modem
usbids = os.popen('lsusb').read()

if "0a12:0001" in usbids:
    diagnostics["bluetooth"] = True
else:
    diagnostics["bluetooth"] = False

if "2c7c:0125" in usbids:
    diagnostics["modem"] = True
else:
    diagnostics["modem"] = False

#LoRa Module Test
with open("/var/pktfwd/diagnostics") as diagOut:
    loraStatus = diagOut.read()

print(loraStatus)


print(diagnostics)

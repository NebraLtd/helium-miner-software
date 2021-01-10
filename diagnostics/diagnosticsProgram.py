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

#Get ethernet MAC address
diagnostics["eth0"] = open("/sys/class/net/eth0/address").readline().strip()

#Get wifi MAC address
diagnostics["wlan0"] = open("/sys/class/net/wlan0/address").readline().strip()

#Get Balena Name
diagnostics["name"] = os.getenv('BALENA_DEVICE_NAME_AT_INIT')

#Get Balena App and therefore Frequency
diagnostics["app"] = os.getenv('BALENA_APP_NAME')

#Get RPi serial number
diagnostics["cpu"] = open("/proc/cpuinfo").readlines()[38].strip()[10:]

#Get USB IDs to check for BT And Modem
usbids = os.popen('lsusb').read()

print(diagnostics)
print(usbids)

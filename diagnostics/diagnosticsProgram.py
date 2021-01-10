#Checks basic hardware features.

import os

#Variables for all Checks

ethernetMacAddress = ""
wifiMacAddress = ""
balenaName = ""
eccDetected = False
rpiSerialNumber = ""
loraTest = False


#Check the ECC
eccTest = os.popen('i2cdetect -y 1').read()

if "60 --" in eccTest:
    eccDetected = True

#Get ethernet MAC address
ethernetMacAddress = open("/sys/class/net/eth0/address").readline().strip()

#Get wifi MAC address
wifiMacAddress = open("/sys/class/net/wlan0/address").readline().strip()

#Get Balena Name
balenaName = os.getenv('BALENA_DEVICE_NAME_AT_INIT')

#Get RPi serial number
rpiSerialNumber = open("/proc/cpuinfo").readlines()[38].strip()[10:]

print(ethernetMacAddress)
print(wifiMacAddress)
print(balenaName)
print(eccDetected)
print(rpiSerialNumber)
print(loraTest)

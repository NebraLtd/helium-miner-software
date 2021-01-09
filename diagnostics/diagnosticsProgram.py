#Checks basic hardware features.

import os

#Variables for all Checks

ethernetMacAddress = ""
wifiMacAddress = ""
balenaName = ""
eccDetected = False
rpiSerialNumber = ""
loraTest = False

eccTest = os.popen('i2cdetect -y 1').read()

if "60 --" in euiTest:
    eccDetected = True

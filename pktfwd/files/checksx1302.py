import os, subprocess
from pprint import pprint

euiTest = os.popen('./chip_id -d /dev/spidev1.2').read()

#pprint(euiTest)

if "concentrator EUI:" in euiTest:
    print("SX1302")
else:
    print("SX1301")

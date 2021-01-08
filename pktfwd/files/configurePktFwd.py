#Configure Packet Forwarder Program
#Configures the packet forwarder based on the YAML File and Env Variables
import os
import subprocess
import json
from pprint import pprint

from time import sleep
regionID = str(os.environ['REGION'])
#moduleId = 0

print("Sleeping 10 seconds")
sleep(10)

#Region dictionary
regionList = {
    "AS920" : "AS1-global_conf.json",
    "AS923" : "AS1-global_conf.json",
    "AU915" : "AU-global_conf.json",
    "CN470" : "CN-global_conf.json",
    "EU868" : "EU-global_conf.json",
    "IN865" : "IN-global_conf.json",
    "KR920" : "KR-global_conf.json",
    "RU864" : "RU-global_conf.json",
    "US915" : "US-global_conf.json"
}

#Configuration function

def writeRegionConf(regionId):
    regionconfFile = "/opt/iotloragateway/packet_forwarder/lora_templates/"+regionList[regionId]
    with open(regionconfFile) as regionconfJFile:
        newGlobal = json.load(regionconfJFile)
    globalPath = "/opt/iotloragateway/packet_forwarder/global_conf_sg0.json"

    with open(globalPath, 'w') as jsonOut:
        json.dump(newGlobal, jsonOut)




#If HAT Enabled


#Reset on pin 38
while True:

    print("Nebra Smart Gateway 1")
    print("Frequency" + regionID)
    writeRegionConf(regionID)
    print("Starting")
    os.system("./reset-38.sh")
    sleep(2)
    os.system("./packetforwarder_sg0")
    print("Software crashed, restarting, hatsg0")




#Sleep forever

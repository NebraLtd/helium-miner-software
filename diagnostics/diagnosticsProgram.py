#Checks basic hardware features.

import os, dbus, qrcode, json
from genHTML import generateHTML
from PIL import Image, ImageDraw, ImageFont
from time import sleep

while True:
    print("Starting Diag")


    #Variables for all Checks

    diagnostics = {
    }

    #Check the ECC
    eccTest = os.popen('i2cdetect -y 1').read()

    if "60 --" in eccTest:
        diagnostics["ECC"] = True
    else:
        diagnostics["ECC"] = False

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

    #Get Balena App
    try:
        diagnostics["BA"] = os.getenv('BALENA_APP_NAME')
    except:
        diagnostics["BA"] = "APP-FAIL"

    #Get Frequency
    try:
        diagnostics["RE"] = os.getenv('REGION')
    except:
        diagnostics["RE"] = "NO420"

    #Get Variant
    try:
        diagnostics["VA"] = os.getenv('VARIANT')
    except:
        diagnostics["VA"] = "UNKNOWN"

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

    if(loraStatus == "true"):
        diagnostics["LOR"] = True
    else:
        diagnostics["LOR"] = False


    try:
        miner_bus = dbus.SystemBus()
        miner_object = miner_bus.get_object('com.helium.Miner', '/')
        miner_interface = dbus.Interface(miner_object, 'com.helium.Miner')
        p2pstatus = miner_interface.P2PStatus()
        print(p2pstatus)
        diagnostics["MH"] = str(p2pstatus[3][1])
        diagnostics['MC'] = str(p2pstatus[0][1])
    except:
        diagnostics["MH"] = "000000"
        diagnostics['MC'] = "Error"
        print("P2PFAIl")

    try:
        public_keys_file = open("/var/data/public_keys").readline().split('"')
        diagnostics["PK"] = str(public_keys_file[1])
        diagnostics["OK"] = str(public_keys_file[3])
        diagnostics["AN"] = str(public_keys_file[5])
    except:
        diagnostics["PK"] = "Error"
        diagnostics["OK"] = "Error"
        diagnostics["AN"] = "Error"

    print(diagnostics)

    qrCodeDiagnostics = {
        "BN" : diagnostics['BN'],
        "BA" : diagnostics['BA'],
        "E0" : diagnostics['E0'],
        "W0" : diagnostics['W0'],
        "RPI" : diagnostics['RPI'],
        "OK" : diagnostics['OK']
    }
    diagJson = json.dumps(diagnostics)

    with open("/opt/nebraDiagnostics/html/diagnostics.json", 'w') as diagOut:
        diagOut.write(diagJson)


    qrcodeJson = json.dumps(qrCodeDiagnostics)
    qrcodeOut = qrcode.make(qrcodeJson)

    canvas = Image.new('RGBA', (600, 700), (255,255,255,255))

    addText = ImageDraw.Draw(canvas)

    fnt = ImageFont.truetype("/opt/nebraDiagnostics/Ubuntu-Bold.ttf", 24)

    modelString = "Nebra %s Helium Hotspot" % diagnostics["VA"]
    nameString = "ID: %s" % diagnostics["BN"]
    macString = "ETH: %s" % diagnostics["E0"]
    freqString = "Region: %s" % diagnostics["RE"]

    addText.text((60,575), modelString, (0,0,0) , font=fnt)
    addText.text((60,600), nameString, (0,0,0) , font=fnt)
    addText.text((60,625), macString, (0,0,0) , font=fnt)
    addText.text((60,650), freqString, (0,0,0) , font=fnt)

    canvas.paste(qrcodeOut, (20,0))
    #qrcodeOut.save('/opt/nebraDiagnostics/html/diagnosticsQR.png')
    canvas.save('/opt/nebraDiagnostics/html/diagnosticsQR.png')

    with open("/opt/nebraDiagnostics/html/index.html", 'w') as htmlOut:
        htmlOut.write(generateHTML(diagnostics))
    sleep(300)

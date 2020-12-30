#!/usr/bin/env bash

sleep 15
echo "Starting connmand"
connmand --device wlan0

sleep 15
echo "Starting gateway_config"
/opt/gateway_config/bin/gateway_config start

sleep 30
echo "advertise on"

/opt/gateway_config/bin/gateway_config advertise on

sleep 5

while true; do sleep 1; done

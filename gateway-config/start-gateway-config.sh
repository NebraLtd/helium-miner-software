#!/usr/bin/env bash

sleep 30
/opt/gateway_config/bin/gateway_config start

sleep 30

/opt/gateway_config/bin/gateway_config advertise on

sleep 5

while true; do sleep 1; done

#!/usr/bin/env bash
/opt/gateway_config/bin/gateway_config start

sleep 10

/opt/gateway_config/bin/gateway_config advertise on

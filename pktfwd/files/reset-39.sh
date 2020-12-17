#!/usr/bin/env bash
sleep 5
if [ ! -d "/sys/class/gpio/gpio39" ]; then
    echo "39" > /sys/class/gpio/export
fi
echo "out" > /sys/class/gpio/gpio39/direction
sleep 2
echo "1" > /sys/class/gpio/gpio39/value
sleep 2
echo "0" > /sys/class/gpio/gpio39/value
sleep 2
echo "1" > /sys/class/gpio/gpio39/value
sleep 2
echo "0" > /sys/class/gpio/gpio39/value
sleep 2

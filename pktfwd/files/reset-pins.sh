#!/usr/bin/env bash
whoami
if [ ! -d "/sys/class/gpio/gpio22" ]; then
    echo "22" > /sys/class/gpio/export
fi
if [ ! -d "/sys/class/gpio/gpio38" ]; then
    echo "38" > /sys/class/gpio/export
fi
if [ ! -d "/sys/class/gpio/gpio39" ]; then
    echo "39" > /sys/class/gpio/export
fi

echo "out" > /sys/class/gpio/gpio22/direction
echo "out" > /sys/class/gpio/gpio38/direction
echo "out" > /sys/class/gpio/gpio39/direction


echo "1" > /sys/class/gpio/gpio22/value
echo "1" > /sys/class/gpio/gpio38/value
echo "1" > /sys/class/gpio/gpio39/value
sleep 2
echo "0" > /sys/class/gpio/gpio22/value
echo "0" > /sys/class/gpio/gpio38/value
echo "0" > /sys/class/gpio/gpio39/value
sleep 2
echo "1" > /sys/class/gpio/gpio22/value
echo "1" > /sys/class/gpio/gpio38/value
echo "1" > /sys/class/gpio/gpio39/value
sleep 2
echo "0" > /sys/class/gpio/gpio22/value
echo "0" > /sys/class/gpio/gpio38/value
echo "0" > /sys/class/gpio/gpio39/value
sleep 2

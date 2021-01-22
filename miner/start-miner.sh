#!/bin/sh

PUBLIC_KEYS=$(/opt/miner/bin/miner print_keys)
[ $? -ne 0 ] && exit 1
echo $PUBLIC_KEYS > /var/data/public_keys

/opt/miner/bin/miner foreground

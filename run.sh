#!/bin/bash

date
cd /home/pi/Development/eero-tools/
source bin/activate
# First generate the source JSONs from the network
./start.py eeros >eeros.json
./start.py devices >devices.json

# Now convert those into a hosts.conf
touch hosts.conf
touch newhosts.conf
./process.py

if [ ! -s newhosts.conf ]; then
  echo "The newhosts.conf file is empty. Exiting."
  exit 1
fi

# Now see if it's the same as the old
if ! cmp -s hosts.conf newhosts.conf; then
  echo "The files are different"
  cp newhosts.conf hosts.conf
  sudo cp hosts.conf /etc/dnsmasq-hosts.conf
  sudo service dnsmasq reload
else
  echo "The files are the same."
fi

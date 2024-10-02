#!/bin/env python
import json


fout = open("newhosts.conf", "w")

# Read the eeros.json file and parse it into memory
with open("eeros.json", "r") as file:
    eeros = json.load(file)
print("%i eeros found" % len(eeros))
for eero in eeros:
    hostname = eero["location"].replace(" ", "_")
    hostname = hostname.replace("'", "")
    hostname = hostname.replace("’", "")
    hostname = hostname.replace(":", "")
    hostname = hostname.replace("_-_", "_")

    fout.write("%s\teero_%s.home\n" % (eero["ip_address"], hostname))

# Read the devices.json file and parse it into memory
with open("devices.json", "r") as file:
    devices = json.load(file)

print("%i connected devices found" % len(devices))
count = 0
for device in devices:
    if ("nickname" in device) and (device["nickname"] is not None):
        if device["ip"] is not None:
            count = count + 1
            hostname = device["nickname"].replace(" ", "_")
            hostname = hostname.replace("'", "")
            hostname = hostname.replace("’", "")
            hostname = hostname.replace(":", "")
            hostname = hostname.replace("_-_", "_")

            fout.write("%s\t%s.home\n" % (device["ip"], hostname))

print("%i valid hostname" % count)

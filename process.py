#!/bin/env python
import json


# Read the eeros.json file and parse it into memory
with open("eeros.json", "r") as file:
    eeros = json.load(file)
for eero in eeros:
    hostname = eero["location"].replace(" ", "_")
    hostname = hostname.replace("'", "")
    hostname = hostname.replace("’", "")
    hostname = hostname.replace(":", "")
    hostname = hostname.replace("_-_", "_")

    print("eero_%s -> %s" % (hostname, eero["ip_address"]))

# Read the devices.json file and parse it into memory
with open("devices.json", "r") as file:
    devices = json.load(file)

for device in devices:
    if ("nickname" in device) and (device["nickname"] is not None):
        if device["ip"] is not None:
            hostname = device["nickname"].replace(" ", "_")
            hostname = hostname.replace("'", "")
            hostname = hostname.replace("’", "")
            hostname = hostname.replace(":", "")
            hostname = hostname.replace("_-_", "_")

            print("%s -> %s" % (hostname, device["ip"]))

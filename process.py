#!/bin/env python
import json


def tidyName(host):
    hostname = host.replace(" ", "_")
    hostname = hostname.replace("'", "")
    hostname = hostname.replace("’", "")
    hostname = hostname.replace(":", "")
    hostname = hostname.replace("_-_", "_")
    return hostname


fout = open("newhosts.conf", "w")

# Read the eeros.json file and parse it into memory
with open("eeros.json", "r") as file:
    eeros = json.load(file)
print("%i eeros found" % len(eeros))
for eero in eeros:
    hostname = tidyName(eero["location"])
    fout.write("%s\teero_%s\n" % (eero["ip_address"], hostname))
    with open("%s.conf" % hostname, "w") as file:
        for field in [
            "ip_address",
            "serial",
            "model",
            "model_number",
            "os_version",
            "model",
            "model_number",
            "os_version",
            "mac_address",
            "location",
            "connected_wired_clients_count",
            "connected_wireless_clients_count",
            "state",
        ]:
            file.write("%s=%s\n" % (field, eero[field]))

# Read the devices.json file and parse it into memory
with open("devices.json", "r") as file:
    devices = json.load(file)

# Read the aliases list
aliases = dict()
with open("aliases.txt", "r") as file:
    for line in file.readlines():
        hosts = line.split(",")
        aliases[hosts[0]] = hosts[1:]

print("%i connected devices found" % len(devices))
count = 0
for device in devices:
    if ("nickname" in device) and (device["nickname"] is not None):
        if device["ip"] is not None:
            count = count + 1
            hostname = tidyName(device["nickname"])
            aliasList = ""
            if device["nickname"].lower() in aliases:
                aliasList = " ".join(
                    tidyName(alias) for alias in aliases[device["nickname"].lower()]
                )
            fout.write("%s\t%s %s\n" % (device["ip"], hostname, aliasList))

print("%i valid hostname" % count)

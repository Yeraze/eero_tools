#!/bin/env python
import json


def tidyName(host):
    hostname = host.replace(" ", "_")
    hostname = hostname.replace("'", "")
    hostname = hostname.replace("’", "")
    hostname = hostname.replace(":", "")
    hostname = hostname.replace("_-_", "_")
    return hostname



# Read the eeros.json file and parse it into memory
with open("eeros.json", "r") as file:
    eeros = json.load(file)
print("%i eeros found" % len(eeros))
# Read the devices.json file and parse it into memory
with open("devices.json", "r") as file:
    devices = json.load(file)
print("%i connected devices found" % len(devices))

if (len(eeros) == 0) or (len(devices) == 0):
    print("-> ABORTING due to missing data.")
    exit(1)


fout = open("newhosts.conf", "w")
for eero in eeros:
    hostname = tidyName(eero["location"])
    fout.write("%s\teero_%s\n" % (eero["ip_address"], hostname))
    with open("%s.conf" % hostname, "w") as file:
        for field in [
            "location",
            "ip_address",
            "serial",
            "model",
            "model_number",
            "os_version",
            "status",
            "mesh_quality_bars",
            "mac_address",
            "connected_wired_clients_count",
            "connected_wireless_clients_count",
            "state",
            "last_reboot",
            "last_heartbeat"
        ]:
            file.write("%s=%s\n" % (field, eero[field]))


# Read the aliases list
aliases = dict()
with open("aliases.txt", "r") as file:
    for line in file.readlines():
        hosts = line.split(",")
        aliases[hosts[0]] = hosts[1:]

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

This is a simple project to build an /etc/hosts file from an EERO Network

I got tired of trying to maintain one statically when I let Eero do DHCP, and even with
DHCP reservations the eero's themselves keep moving. 


This is meant to be run as part of a cron job (the `run.sh` script) that will drop a suitable
hosts file in `/etc/dnsmasq-hosts.conf` and then bounce dnsmasq.  Configure dnsmasq with `no-hosts` 
and the `addn-hosts` directive to include this file. 

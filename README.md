This is a simple project to build an /etc/hosts file from an EERO Network

I got tired of trying to maintain one statically when I let Eero do DHCP, and even with
DHCP reservations the eero's themselves keep moving. 


This is meant to be run as part of a cron job (the `run.sh` script) that will drop a suitable
hosts file in `/etc/dnsmasq-hosts.conf` and then bounce dnsmasq.  Configure dnsmasq with `no-hosts` 
and the `addn-hosts` directive to include this file.  In addition, set the `expand-hosts` and `domain` directive to append a domain name to every entry in the list.

If you have aliases (for example, something service up HTTPS reverse
proxies on your network), create an 'aliases.txt' file with a list of
the system nickname, and any aliases you want to use separated by commas. For example:

```
synology nas,plex,openvas,adguard
```

(NOTE: keep everything lowercase.  The first entry should match the
eero Nickname, and will be postprocessed into the hostname same as the
regular name.)


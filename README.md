# dnsping
Utility for setting an A record to the local machines public IP with Digital Ocean DNS hosting

Usage:

  The following command will set the A record for `machineip.mydomain.com` to the IP returned from ipv4.icanhazip.com using digital ocean key `ABC`
  
  ```python dnsping -t ABC -d mydomain.com -s machineip```
  
Installation:

```pip install -e .```

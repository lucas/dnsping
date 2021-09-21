from dnsping import token, domain, subdomain, del_dupes
from dnsping.checker import DnsChecker

if __name__ == '__main__':
  dc = DnsChecker(token, domain, subdomain, del_dupes)
  dc.run()


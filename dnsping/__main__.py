from dnsping import token, domain, subdomain
from dnsping.checker import DnsChecker

if __name__ == '__main__':
  dc = DnsChecker(token, domain, subdomain)
  dc.run()


from digitalocean import Domain, Record
import sys
from urllib2 import urlopen

class DnsChecker(object):
  def __init__(self, token, domain, subdomain):
    self.token = token
    self.domain = domain
    self.subdomain = subdomain
    self.full_domain = '%s.%s' % (self.subdomain, self.domain)
    self.ip = self.get_ip()

    if not self.ip:
      print 'Unable to retrieve current IP'
      sys.exit(-1)

  def get_ip(self):
    f = urlopen('https://ipv4.icanhazip.com')
    return f.read().strip()

  def get_record(self):
    # initialize Digital Ocean
    do_d = Domain(token=self.token, name=self.domain)

    # loop records looking for the right one
    for record in do_d.get_records():
      if record.name != self.subdomain:
        continue
      return record

    return None

  def create_a_record(self):
    r = Record(domain_name=self.domain, token=self.token)
    r.type = 'A'
    r.data = self.ip
    r.name = self.subdomain
    r.priority = None
    r.port = None
    r.weight = None
    r.create()

  def run(self):
    # get current DNS record
    record = self.get_record()

    if not record:
      print 'Creating record pointing %s to %s' % (self.full_domain, self.ip)
      self.create_a_record()
      print 'Done!'
    else:
      if record.data != self.ip:
        print 'Updating record (%s) from %s to %s' % (self.full_domain,
            record.data, self.ip)
        record.data = self.ip
        record.save()
        print 'Done!'
      else:
        print 'No update needed'

import sys
import requests

from digitalocean import Domain, Record

class DnsChecker(object):
  def __init__(self, token, domain, subdomain, del_dupes=None):
    self.token = token
    self.domain = domain
    self.subdomain = subdomain
    self.del_dupes = del_dupes
    self.full_domain = f'{self.subdomain}.{self.domain}'
    self.ip = self.get_ip()

    if not self.ip:
      print('Unable to retrieve current IP')
      sys.exit(-1)

  def get_ip(self):
    req = requests.get('https://ipv4.icanhazip.com')
    return req.text.strip()

  def get_record(self):
    # initialize Digital Ocean
    do_d = Domain(token=self.token, name=self.domain)

    # loop records looking for the right one
    for record in do_d.get_records():
      if record.name != self.subdomain:
        continue
      return record

    return None

  def delete_duplicates(self, name, real_id):
    do_d = Domain(token=self.token, name=self.domain)

    num = 0
    # loop records, destroy any duplicates with same name
    for record in do_d.get_records():
      if record.id == real_id or record.name != self.subdomain:
        continue
      record.destroy()
      num += 1

    return num

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

    if self.del_dupes:
      # remove any duplicate records
      num = self.delete_duplicates(record.name, record.id)
      print(f'Destroyed {num} duplicates that were found for {record.name}')

    if not record:
      print(f'Creating record pointing {self.full_domain} to {self.ip}')
      self.create_a_record()
      print('Done!')
    else:
      if record.data != self.ip:
        print(f'Updating record ({self.full_domain}) from {record.data} to {self.ip}')
        record.data = self.ip
        record.save()
        print('Done!')
      else:
        print('No update needed')

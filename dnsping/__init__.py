# standard libs
import ConfigParser
import argparse
import os.path

from dnsping.checker import DnsChecker

config = None
token = None
domain = None
subdomain = None

if not config:
  # get command line options
  parser = argparse.ArgumentParser(prog='dnsping')
  parser.add_argument(
    '-t',
    dest='token',
    help='Digital Ocean API Key Token',
  )

  parser.add_argument(
    '-d',
    dest='domain',
    help='Root Domain for DNS management',
  )

  parser.add_argument(
    '-s',
    dest='subdomain',
    help='Subdomain for DNS management',
  )

  parser.add_argument(
    '-i',
    dest='ini',
    default='config.ini',
    help='Path to configuration ini file for environment'
  )

  (options, args) = parser.parse_known_args()

  if options.token and options.domain and options.subdomain:
    token = options.token
    domain = options.domain
    subdomain = options.subdomain
  elif os.path.isfile(options.ini):
    # read config
    config = ConfigParser.ConfigParser()
    config.read(options.ini)

    # digital ocean
    token = config.get('digitalocean', 'key')
    domain = config.get('digitalocean', 'domain')
    subdomain = config.get('digitalocean', 'subdomain')
  else:
    raise Exception('Unable to run, either i or t,d,s must be set')

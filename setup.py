try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='dnsping',
    version='0.1',
    description='update dynamic DNS with Digital Ocean for local IP',
    author='lucas',
    author_email='',
    url='',
    install_requires=[
      'python-digitalocean==1.9.0',
    ],
    zip_safe=False,
    entry_points="""
    """,
)

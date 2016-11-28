xivo-ctid-client
================

[![Build Status](https://travis-ci.org/wazo-pbx/xivo-ctid-client.png?branch=master)](https://travis-ci.org/wazo-pbx/xivo-ctid-client)

A python library to access the REST API of xivo-ctid not to be confused with [the xivo client](https://github.com/xivo-pbx/xivo-client-qt)

Running unit tests
------------------

```
apt-get install libpq-dev python-dev libffi-dev libyaml-dev
pip install tox
tox --recreate -e py27
```

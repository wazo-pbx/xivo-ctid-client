__Important: Please note this repository is now deprecated in Wazo, we don't support it anymore.__

---------------------------------

xivo-ctid-client
================

[![Build Status](https://jenkins.wazo.community/buildStatus/icon?job=xivo-ctid-client)](https://jenkins.wazo.community/job/xivo-ctid-client)

A python library to access the REST API of xivo-ctid not to be confused with [the xivo client](https://github.com/wazo-pbx/xivo-client-qt)

Running unit tests
------------------

```
apt-get install libpq-dev python-dev libffi-dev libyaml-dev
pip install tox
tox --recreate -e py27
```

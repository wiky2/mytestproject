#!/usr/bin/env python
# -*- coding: utf-8 -*-
import htmlentitydefs
import httplib
import locale
import math
import netrc
import os
import os.path
import re
import socket
import string
import sys
import time
import urllib
import urllib2

url='http://mp3.m.mop.com/mp3/new_mp3/2010/2/13/20c2b77a676c46bab8f9965e07392a7b.mp3'
matcho=re.search("[a-zA-Z0-9]+\.mp3",url)
print matcho.group(0)
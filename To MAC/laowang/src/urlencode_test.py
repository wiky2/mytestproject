#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
s="%D6%D0%B9%FA"
print urllib.unquote(s)
s='中国'
print urllib.unquote(s)
ss={'a':'中国'}
print urllib.urlencode(ss)
#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import os
import chardet
def _smartcode(stream):
    """smart recove stream into UTF-8"""
    ustring = stream
    codedetect = chardet.detect(ustring)["encoding"]
    print codedetect
    try:
        print ustring
        ustring = unicode(ustring, codedetect)
        print ustring
        return "%s %s"%("",ustring.encode('utf8'))
    except:
        return u"bad unicode encode try!"
def cdWalker(cdrom,cdcfile):
    export = ""
    for root, dirs, files in os.walk(cdrom):
        export+="\n %s;%s;%s" % (root,dirs,files)
        export=_smartcode(export)
        open(cdcfile, 'w').write(export)
    
cdWalker('J:\VBA','cd1.cdc')
cdWalker('J:\VBA','cd2.cdc')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

myname = socket.getfqdn(socket.gethostname())

myaddr = socket.gethostbyname(myname) 

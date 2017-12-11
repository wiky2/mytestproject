#!/usr/bin/python
#dict_switch.py

def print_adam():
    print "Adam is awesome"

def print_john():
    print "John is so-so"

def error_msg():
    print "What are you typing"


switch = {
'adam':print_adam,
'john':print_john}

default = error_msg

def do_switch(input):
    if switch.has_key(input):
        return switch[input]
    else:
        return default

do_switch("adam")()
do_switch("john")()
do_switch("adfakhl")()


#!/usr/bin/env python
# coding: utf-8
from operator import attrgetter
class User(object):
    """sort by attrgetter"""
    def __init__(self,x,y ):
        """初始化 """
        self.name=x
        self.user_id=y
    def __repr__(self):
        """method documentation"""
        return self.name+":"+str(self.user_id)
users = [
        User('Bucky', 43),
        User('Sally', 5),
        User('Tuna', 61),
        User('Brian', 2),
        User('Joby', 77),
        User('Amanda', 9)

]
for user in users:
    print user
print '---------'
for user in sorted(users,key=attrgetter('name')):
    print user


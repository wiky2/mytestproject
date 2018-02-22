#!/usr/bin/env python
# coding: utf-8
from PIL import Image
#3.4 Pillow
#2.7 PIL
img = Image.open('timg.jpg')
r,g,b=img.split()
r.save('timg-r.jpg')
g.save('timg-g.jpg')
b.save('timg-b.jpg')
print img.size
print img.format
# img.show()

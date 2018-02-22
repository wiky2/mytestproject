#!/usr/bin/env python
# coding: utf-8
from PIL import Image
#3.4 Pillow
#2.7 PIL
img = Image.open('timg.jpg')
r,g,b=img.split()
new_img=Image.merge('RGB',(r,g,b))
new_img2=Image.merge('RGB',(r,b,g))
new_img.save('timg-rgb-merge.jpg')
new_img2.save('timg-rgb-merge2.jpg')
print img.size
print img.format
# img.show()

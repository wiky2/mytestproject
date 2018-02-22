#!/usr/bin/env python
# coding: utf-8
from PIL import Image
#3.4 Pillow
#2.7 PIL
img = Image.open('timg.jpg')
img2 = Image.open('timg2.jpg')
(r1,g1,b1) = img.split()
(r2,g2,b2) = img2.split()

area=(0,0,480,240)
r1=r1.crop(area)
g1=g1.crop(area)
b1=b1.crop(area)
r2=r2.crop(area)
g2=g2.crop(area)
b2=b2.crop(area)
print r1.size
print r2.size
new_img=Image.merge('RGB',(r1,g1,b2))
new_img2=Image.merge('RGB',(r2,g2,b1))
new_img.save('timg-rgb-merge-3.jpg')
new_img2.save('timg-rgb-merge-4.jpg')
print img.size
print img.format
# img.show()

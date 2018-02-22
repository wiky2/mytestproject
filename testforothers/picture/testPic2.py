#!/usr/bin/env python
# coding: utf-8
from PIL import Image
#3.4 Pillow
#2.7 PIL
img = Image.open('timg.jpg')
img4 = Image.open('timg4.jpg')
area=(0,0,480,240)
img.paste(img4,area)
img.save('img_combine.jpg')
print img.size
print img.format
# img.show()

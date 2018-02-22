#!/usr/bin/env python
# coding: utf-8
from PIL import Image
#3.4 Pillow
#2.7 PIL
img = Image.open('timg.jpg')
area=(100,100,300,375)
cropped_img=img.crop(area)
cropped_img.save('timg-crop.jpg')
print img.size
print img.format
# img.show()

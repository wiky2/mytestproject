#!/usr/bin/env python
# coding: utf-8
from PIL import Image
from PIL import ImageFilter
#3.4 Pillow
#2.7 PIL
img = Image.open('timg.jpg')
black_white=img.convert('L')#balck,white
black_white.save('timg_black_white.jpg')
blur=img.filter(ImageFilter.BLUR)
blur.save('timg_blur.jpg')
print img.size
print img.format
# img.show()

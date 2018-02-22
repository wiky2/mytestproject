#!/usr/bin/env python
# coding: utf-8
from PIL import Image
#3.4 Pillow
#2.7 PIL
img = Image.open('timg.jpg')
img_flip_left_right=img.transpose(Image.FLIP_LEFT_RIGHT)
img_flip_rotate=img.transpose(Image.ROTATE_90)
img_flip_left_right.save('timg_flip_left_right.jpg')
img_flip_rotate.save("timg_flip_rotate.jpg")
print img.size
print img.format
# img.show()

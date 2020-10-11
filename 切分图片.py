# -*- coding: utf-8 -*-

from PIL import Image

filename = r'C:\Users\12517\Desktop\UNET\img\full-orignal-chang-size - 副本.png'
img = Image.open(filename)
size = img.size
#print(size)

# 准备将图片切割成100张小图片
weight = int(size[0] // 10)
height = int(size[1] // 10)
# 切割后的小图的宽度和高度
#print(weight, height)

for j in range(10):
    for i in range(10):
        box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
        region = img.crop(box)
        region.save('139_{}{}.png'.format(j, i))
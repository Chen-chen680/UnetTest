# -*- coding: utf-8 -*-

import xml.etree.cElementTree as et
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
dir='C:\\Users\\12517\\Desktop\\cnn\\11111\\easydl2labelImg\\image2\\'
def crop_img(dir,target_size,num):
    i=0
    for file in os.listdir(dir):
        if('xml'in file):
            s=dir+file
            tree=et.parse(s)
            root=tree.getroot()
            filename=root.find('filename').text
            for Object in root.findall('object'):
                bndbox=Object.find('bndbox')
                xmin=bndbox.find('xmin').text
                ymin=bndbox.find('ymin').text
                xmax=bndbox.find('xmax').text
                ymax=bndbox.find('ymax').text
                img=Image.open(dir+filename)
                #img=img0.rotate(random.randint(-180,180))
                size=img.size
                for count in range(1,num):
                    amin=random.randint(0,int(xmin))
                    bmin=random.randint(0,int(ymin))
                    cmax=random.randint(int(xmax),size[0])
                    dmax=random.randint(int(ymax),size[1])
                    box=(int(xmin),int(ymin),int(xmax),int(ymax))
                    box2=(amin,bmin,cmax,dmax)
                    print(box)
                    print(box2)
                    image=img.crop(box)
                    image2=img.crop(box2)
                    image2=image.resize((target_size,target_size),Image.ANTIALIAS)
                   # image1.save(dir+"chuli222_"+str(i)+".jpg")
                    image2.save(dir+"chuli_"+str(i)+".jpg")
                    i=i+1




crop_img(dir,target_size=599,num=101)

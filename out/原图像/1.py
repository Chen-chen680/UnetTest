import os
import cv2

a = os.walk('C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\\out\\label')
a = a.__next__()

RootPath = a[0]
FileNameList = a[2]

for filename in FileNameList:
    if '.png' not in filename:
        continue
    path = RootPath + '\\' + filename
    img = cv2.imread(path)
    print(path)

    img_shape = img.shape  # 图像大小(565, 650, 3)
    print(img_shape)
    h = img_shape[0]
    w = img_shape[1]
    # 彩色图像转换为灰度图像（3通道变为1通道）
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    # 最大图像灰度值减去原图像，即可得到反转的图像
    dst = 255 - gray
    cv2.imwrite('.\\trans\\' + filename,dst)
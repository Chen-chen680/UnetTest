import cv2
import os

def getfilename(path):
    hhh = os.walk(path)
    listsave = []
    for i, j, k in hhh:
        print(i)
        listsave.append(k)
    return listsave

SaveImageList = getfilename('C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\\image')
SaveLabelList = getfilename('C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\\label')



ImageOutPath = 'C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\\out\\image'
LabelOutPath = ImageOutPath.replace('image','label')

def ImageFlip(AList,ImagePath,outpath):
    for list1 in AList:
        for filename in list1:

            filename_img = ImagePath + '\\' + filename

            img = cv2.imread(filename_img)
            h_img = cv2.flip(img,1)
            v_img = cv2.flip(img,0)
            hv_img = cv2.flip(img,-1)

            cv2.imwrite(outpath + '\\' + filename ,img)
            cv2.imwrite(outpath + '\\' + filename.replace('.png','_v') + '.png',h_img)
            cv2.imwrite(outpath + '\\' + filename.replace('.png','_v') + '.png',v_img)
            cv2.imwrite(outpath + '\\' + filename.replace('.png','_hv') + '.png',hv_img)

#ImageFlip(SaveImageList,'C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\\image',ImageOutPath)
#ImageFlip(SaveLabelList,'C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\\label',LabelOutPath)

# img = cv2.imread('C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\\label\\1.png')
# img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.imwrite('C:\\Users\\12517\\Desktop\\PaddleSeg\\huidu.png',img)

img = cv2.imread('C:\\Users\\12517\\Desktop\\PaddleSeg\\huidu.png')
img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
cv2.imwrite('C:\\Users\\12517\\Desktop\\PaddleSeg\\RGB.png',img=img)


# pic = cv2.imread('C:/Users/12517/Desktop/IMG_LABEL/train/1.png') #读入图片
# outpath = 'C:\\Users\\12517\\Desktop\\IMG_LABEL\\train\out'
# h_pic = cv2.flip(pic, 1)#水平翻转
# cv2.imwrite(outpath+'\\h.png',h_pic)
#
#
# v_pic = cv2.flip(pic, 0)#垂直翻转
# cv2.imwrite(outpath+'\\v.png',v_pic)
#
# hv_pic = cv2.flip(pic, -1)#水平垂直翻转
# cv2.imwrite(outpath+'\\hv.png',hv_pic)


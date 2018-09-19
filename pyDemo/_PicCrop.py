#!/usr/bin/env python3
import os
import sys
import random
import os.path
from PIL import Image
from svmutil import *
##################切割要识别的图片###############
def GetCropImgs(imgPicImg):
    img = Image.open(imgPicImg)
    ImgList = []
    for i in range(4):
        x = 6 + i * 13
        y = 3
        SubImg = img.crop((x, y, x + 13, y + 15))
        ImgList.append(SubImg)
    return ImgList


g_Count = 0
strStep6Dir = 'D:/1/step6/'
strFullPath = 'D:/1/step6/001.png'
#图片文件路径信息
ImgList = GetCropImgs(strFullPath)
for img in ImgList:
    strImgName = "%04d%04d.png" % (g_Count, random.randint(0, 9999))
    strImgPath = os.path.join(strStep6Dir, strImgName)
    img.save(strImgPath)
    g_Count += 1

print("OK！")
############################
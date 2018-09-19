#!/usr/bin/env python3
#对一张验证码图片进行识别测试

##1.获取一张验证码图片
##2.对图片进行处理
##  2.1.二值化处理，增加对比度，锐化，增加亮度，滤镜，转为黑白，
##  2.2.去除噪点
##  2.3.切割图片
##3.生成向量文件
##4.再利用之前的模型文件进行识别测试

################
import _PicDealWith
import os
import random
import _SVMDemo


##测试
g_Count = 0
strDirPath = 'D:/1/test/'
strFileName = '001.png'
#1.图片文件路径信息
strFullPath = os.path.join(strDirPath, strFileName)
#2.对图片进行处理
#2.1二值化处理
imgBinImg = _PicDealWith.BinaryzationImg(strFullPath)
#2.2去除噪点
imgClrImg = _PicDealWith.ClearNoise(imgBinImg)
#2.3切割图片
ImgList = _PicDealWith.GetCropImgs(imgClrImg)
#2.3循环写入文件
for img in ImgList:
    strImgName = "%04d%04d.png" % (g_Count, random.randint(0, 9999))
    strImgPath = os.path.join(strDirPath, strImgName)
    img.save(strImgPath)
    g_Count += 1

print("OK")

os.remove(strFullPath)

#3.生成向量文件
_SVMDemo.OutPutTestVectorData('0', 'D:/1/test/', 'D:/1/test/Vector.txt')

#4.利用之前的模型文件进行识别测试
pLabel = _SVMDemo.SvmModelTest('D:/1/test/Vector.txt', 'D:/1/step5/Model.txt')
for i in pLabel:
    print('%d' % i, end = '')
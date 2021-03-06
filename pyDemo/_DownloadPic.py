#!/usr/bin/nev python3
#利用python从站点下载验证码图片

import requests

## 1.在 http://mmbox.myuni.com.cn/portalWeb/validationServlet?onlyNum=
#  获取验证码URL
def Downloads_Pic(strPath, strName):
    #设置url
    url = 'http://mmbox.myuni.com.cn/portalWeb/validationServlet?onlyNum='

    #以二进制方式发送Get请求,(如何知道是get？post？请求)，
    #将stream = True，
    #数据读取完成前不要断开链接
    rReq = requests.get(url, stream = True)

    #尝试保存图片
    with open(strPath + strName + '.png', 'wb') as fpPic:
        #循环读取1024Byte到byChunk中，读完则跳出
        for byChunk in rReq.iter_content(chunk_size = 1024):
            if byChunk:
                fpPic.write(byChunk)
                fpPic.flush()
        fpPic.close()

for i in range(1, 10 + 1):
    strFileName = "%03d" % i
    Downloads_Pic('D:/1/', strFileName)

#!/usr/bin/env python3
#破解zip文件密码
#指定zip文件名为upzip.zip
#指定字典文件名为dictionary.txt
import zipfile
import os


def extractFile(zFile, password):
    try:
        if password == None:
            zFile.extractall()
        else:
            #需要指定赋值给形参
            zFile.extractall(path = os.getcwd(), pwd = password.encode('utf-8'))
        print("FoundPassword:", password)
        return True
    except:
        return False

def main():
    zFile = zipfile.ZipFile('D:/1/upzip.zip')
    passFile = open('D:/1/dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        if extractFile(zFile, password):
            break


    print("结束!")

if __name__ == '__main__':
    main()


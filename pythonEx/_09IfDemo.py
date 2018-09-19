#!/usr/bin/env Python3
##ex9. _09IfDemo.py

num = float(input("输入一个数字："))
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")


num = float(input("输入一个数字："))
if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else :
    print("负数")
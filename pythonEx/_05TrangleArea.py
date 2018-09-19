#!/usr/bin/env Python3
##ex5. _05TrangleArea.py

a = float(input('请输入三角形第一边长：'))
b = float(input('请输入三角形第二边长：'))
c = float(input('请输入三角形第三边长：'))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s -c)) ** 0.5

print('三角形面积为%0.2f' %area)
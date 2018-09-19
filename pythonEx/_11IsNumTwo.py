#!/usr/bin/env Python3
##ex11. _11IsNumTwo.py

num = int(input("请输入一个数字："))
if (num % 2) == 0:
    print("{0} 是偶数".format(num))
else:
    print("{0} 是奇数".format(num))
#!/usr/bin/env Python3
##ex14. _14Prime.py

##循环语句可以有 else 子句，
##它在穷尽列表(以for循环)或条件变为 false
##(以while循环)导致循环终止时被执行,
##但循环被break终止时不执行。
num = int(input("请输入一个数字："))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘与", num // i, "是", num)
            break
    else:
        print(num, "是质数")
else:
    print(num, "不是质数")
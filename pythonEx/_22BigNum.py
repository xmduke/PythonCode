#!/usr/bin/python3
##ex22. _22BigNum.py

def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))

print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))
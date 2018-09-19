#!/usr/bin/python3
##ex23. _23MinNum.py

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("输入第一个数字"))
num2 = int(input("输入第二个数字"))

print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))
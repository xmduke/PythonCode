#!/usr/bin/python3
##ex19. _19AmstlNum.py

##如果一个n位正整数等于其各位数字的n次方之和,
##则称该数为阿姆斯特朗数

num = int(input("请输入一个数字："))

sum = 0

n = len(str(num))

temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")
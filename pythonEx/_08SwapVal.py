#!/usr/bin/env Python3
##ex8. _08SwapVal.py

x = input('输入 x 值：')
y = input('输入 y 值：')

temp = x
x = y
y = temp

print('交换后 x 的值为：{}'.format(x))
print('交换后 x 的值为：{}'.format(y))

#不使用临时变量
x = input('输入 x 值：')
y = input('输入 y 值：')

x, y = y, x

print('交换后 x 的值为：{}'.format(x))
print('交换后 x 的值为：{}'.format(y))



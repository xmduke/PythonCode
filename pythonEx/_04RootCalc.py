#!/usr/bin/env Python3
##ex4. _04RootCalc.py

import cmath
a = float(input('输入a:'))
b = float(input('输入b:'))
c = float(input('输入c:'))

#计算
d = (b ** 2) - (4 * a * c)

mol1 = (-b + cmath.sqrt(d)) / (2 * a)
mol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为{0} 和 {1}'.format(mol1, mol2))

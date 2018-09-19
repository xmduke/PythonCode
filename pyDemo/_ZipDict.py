#!/usr/bin/env python3
#生成字典文件

#写文件
fp = open('D:/1/dictionary.txt', 'w')

#循环生成6位数字密码
#rangeList = [0, 1, 2, 3, 4, 5 ,6, 7, 8, 9]
for i in range(1000):
    a = str(i).zfill(3)
    #print(a)
    fp.write(a + '\n')
    fp.flush()

print('生成完成!')
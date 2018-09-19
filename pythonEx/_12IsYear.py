#!/usr/bin/env Python3
##ex12. _12IsYear.py

year = int(input("输入一个年份："))
if (year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("{0}是润年:".format(year))
        else:
            print("{0}不是润年:".format(year))
    else:
        print("{0}是润年:".format(year))
else:
    print("{0}不是润年:".format(year))

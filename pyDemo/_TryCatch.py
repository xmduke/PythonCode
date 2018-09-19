#!/usr/bin/env python3
#异常跳转
import sys

zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

one = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]

Two = [" *** ",
       "*   *",
       "*  * ",
       "   * ",
       "  *  ",
       "*    ",
       "*****"]

Digits = [zero, one, Two]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = " "
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digits[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)

#!/usr/bin/python3
##ex27. _27FIleRW.py

with open("test.txt", "wt") as out_file:
    out_file.write("写入文本")

with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)
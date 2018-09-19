#!/usr/bin/env python3
#导入socket sys模块
import socket
import sys

#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#获取本地主机名192.168.3.100
#host = socket.gethostname()

#设置端口号2333
port = 2333

#连接服务，指定主机和端口号
s.connect(("192.168.3.100", port))

#发送"ps -a"命令
s.send("ps -a")

#接收小于1024字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))

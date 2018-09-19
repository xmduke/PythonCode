#!/usr/bin/env python
#coding:utf-8
import socket
import os, signal
from struct import pack, unpack
from MemTrace import *
import ctypes as C


INT32  = C.c_int32
UINT32 = C.c_uint32
INT64  = C.c_int64
UINT64 = C.c_uint64

#开启ip和端口
ip_port = ('0.0.0.0', 2333)
#生成一个句柄
sk = socket.socket()
#绑定ip端口
sk.bind(ip_port)
#最多连接数
sk.listen(1)

os.popen("/home/montage/Desktop/Demo/cecgwDumpMem &")

#开启死循环
while True:
    print ('[server]server waiting...')
    conn,addr = sk.accept()
    data = conn.recv(1024)

    # 开始循环，第一个命令为 "ps -a"
    if data=="ps -a":
        print("[server]receive command:" + data)
        res = os.popen("ps -a");
        conn.sendall(res.read())

        # 接收PID
        data = conn.recv(1024)
        pid  = UINT32(ntohl(data))
        
        # 暂停进程
        try:
            os.kill(pid, signal.SIGSTOP)
        except:
            print("[server]can't stop %d" % (pid))
            exit()

        # 根据PID获取内存信息
        mapPath = "/proc" + str(pid) + "maps"
        try:
            mapFd = open(mapPath)
        except:
            print("[server]file %s not exist" % (mapPath))
            exit()
        mapFile = mapFd.read()

        # 发送内存布局长度
        conn.sendall(htonl(UINT32(len(mapFile))))
        # 发送内存布局
        conn.sendall(mapFile)

        # 接收监控间隔
        data     = conn.recv(1024)
        interval = UINT32(ntohl(data))
        # 监控信息长度，作为 Demo 目前仅考虑监控一个段
        data  = conn.recv(1024)
        length = UINT32(ntohl(data))
        # 监控段信息
        data      = conn.recv(16)
        segStart  = UINT64(ntohl(data[0:7]))
        segLength = UINT64(ntohl(data[8:15]))
        ruleComp  = MemTrace("/home/montage/Desktop/Demo/libhsdimm.so")
        ruleComp.HsdimmDevOpen()
        ruleComp.RuleCompute(pid, segStart, segLength)
        ruleComp.RUleDump()
        ruleComp.ProcMemAttrUpdate(pid, segStart, segLength, 1)

        os.popen("python hsdimm.py 2")
        os.kill(pid, signal.SIGCONT)

        while True:
            data = conn.recv(1024)
            if data=="stop":
                print("[server]receive command:" + data)
                conn.close()
                break
            os.popen("python hsdimm.py 0")
            os.kill(pid, signal.SIGCONT)
            sleep(interval)

            try:
                os.kill(pid, signal.SIGSTOP)
            except:
                print("[server]can't stop %d" % (pid))
                exit()
            os.popen("python hsdimm.py 1")

            caFd     = open("/home/montage/Desktop/Demo/dump_ca.log")
            dataFd   = open("/home/montage/Desktop/Demo/dump_data.log")
            caFile   = caFd.read()
            dataFile = dafaFd.read()

            # 先发送 dump_ca.log
            conn.sendall(len(caFile))
            conn.sendall(caFile)

            # 接下来发送 dump_data.log
            conn.sendall(len(dataFile))
            conn.sendall(dataFile)
            
            caFd.close()
            dafaFd.close()
    else:
        print("[server]client wrong command, close connection");
        conn.sendall("err")
        conn.close()


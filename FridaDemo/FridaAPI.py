# -*- coding:utf-8 -*-
#测试python frida api
import frida,sys
#  获取远程设备
rdev = frida.get_remote_device();
print rdev
#  遍历进程
processes = rdev.enumerate_processes();
for process in processes:
    print process
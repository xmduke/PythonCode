#!/usr/bin/env python3
#客户端：与C++服务端配合进行网络通讯
#1.创建socket对象
#2.获取本地主机名
#3.设置连接的端口号
#4.连接服务器
#5.6.数据的接收和发送
  #根据接收和发送的消息类型不同进行不同的处理
#7.关闭套接字，退出客户端

#导入socket sys模块
import socket
import sys
import struct
from enum import Enum

class EnumMessage(Enum):

    #发送注册信息
    sendRegister = 1,
    #发送登录信息
    sendLogin = 2,
    #给聊天室发送文字
    sendMessageRoom = 3,
    #给聊天室发送图片
    sendPicRoom = 4,
    #给好友单独发送文字
    sendMessageSingl = 5,
    #给好友单独发送图片
    sendPicSingl = 6,
    #获取所有在线玩家列表
    getUserList = 7,
    #获取好友玩家列表
    getFriendList = 8,
    #添加好友关系
    addFriends = 9,
    #其他类型信息
    otherInfo = 10,
    #客户端退出消息
    sendLogout = 11,
    #远程控制消息
    sendCMDShell = 12,

#初始化套接字
def initSock():
    #创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #获取本地主机名
    host = socket.gethostname()
    localAddr = socket.gethostbyname(host)
    #设置端口号
    port = 9999
    #连接服务，指定主机和端口号
    s.connect(("127.0.0.1", port))
    return s

#发送消息
def sendMsg(socket, EnumMessage):
    message = input(":")
    message1 = ("127.0.0.1" + "说：" + message).encode("gbk")
    #message_type = (EnumMessage)
    message_len = len(message1)
    ss = "II%ds" % message_len
    #print(EnumMessage.value)
    #对构造的消息进行打包发送
    message_send = struct.pack(ss, EnumMessage.value[0], message_len, message1)
    socket.send(message_send)

#注册用户信息
def sendResMsg(socket, EnumMessage):
    message = input("请输入用户名:")
    message1 = (message).encode("gbk")
    # message_type = (EnumMessage)
    message_len = len(message1)
    ss = "II%ds" % message_len
    # print(EnumMessage.value)
    # 对构造的消息进行打包发送
    message_send = struct.pack(ss, EnumMessage.value[0], message_len, message1)
    socket.send(message_send)

# 远程CMD命令信息
def sendCMDMsg(socket, EnumMessage):
    message = input(">>>")
    message1 = (message).encode("gbk")
    # message_type = (EnumMessage)
    message_len = len(message1)
    ss = "II%ds" % message_len
    #print(type(EnumMessage.value[0]))
    # 对构造的消息进行打包发送
    message_send = struct.pack(ss, EnumMessage.value[0], message_len, message1)
    socket.send(message_send)

#接收消息
def recvMsg(socket):
    MESSAGEBUF = 2048;
    message = socket.recv(MESSAGEBUF)
    #消息类型
    type, = struct.unpack("i", message[:4])
    #消息长度
    length, = struct.unpack("I", message[4:8])
    #对收到的消息进行解析
    msgtext = message[8:length+8]
    msgLength = len(msgtext)
    msglen = "%ds" % (length)
    buf, = struct.unpack(msglen, msgtext)
    message_recv = buf.decode("gbk")

    if EnumMessage.sendLogin.value[0] == type:
        #接收来自服务端的登录成功消息
        print(message_recv)
        #发送注册信息
        sendResMsg(socket, EnumMessage.sendRegister)

    elif EnumMessage.otherInfo.value[0] == type:
        print(message_recv)
        #sendMsg(socket, EnumMessage.sendPicSingl)
        # 向服务器发送消息
        print("******Menu******")
        print("1.发送消息\n2.客户端下线\n3.群聊\n4.远程CMD")
        print("******Menu******")
        choice = int(input(">>请选择:"))
        if choice == 1:
            #发送文字
            sendMsg(socket, EnumMessage.otherInfo)
        elif choice == 2:
            #发送要下线的消息
            typeformat = EnumMessage.sendLogout.value[0]
            messageformat = "下线".encode("gbk")
            lengthformat = len(messageformat)
            strformat = "II%ds" % lengthformat
            message_sendlogout = struct.pack(strformat, typeformat, lengthformat, messageformat)
            socket.send(message_sendlogout)
        elif choice == 3:
            #消息发送到服务器，通过服务器进行转发给存在的客户端
            sendMsg(socket, EnumMessage.sendMessageRoom)
        elif choice == 4:
            #向服务端发送CMD命令
            sendCMDMsg(socket, EnumMessage.sendCMDShell)


    elif EnumMessage.sendLogout.value[0] == type:
        #客户端退出
        print(message_recv)
        print("127.0.0.1" + "下线!")
        return 0

    elif EnumMessage.sendMessageRoom.value[0] == type:
        #处理接收到来自聊天室的消息
        print("群聊信息：" + message_recv)
        return

    elif EnumMessage.sendRegister.value[0] == type:
        #处理来自服务端的注册信息处理结果(失败)，若成功在otherInfo中处理
        print(message_recv)
        # 发送注册信息
        sendResMsg(socket, EnumMessage.sendRegister)
        return

    elif EnumMessage.sendCMDShell.value[0] == type:
        #处理来自服务端的消息结果，最后的1024个自己消息由otherInfo处理
        print(message_recv)
        return
        # 向服务端发送CMD命令
        #sendCMDMsg(socket, EnumMessage.sendCMDShell)

    else:
        print(message_recv + "No Msg!")
        return 0

#关闭客户端
def closeClient(socket):
    #退出客户端
    socket.close()

#程序入口
def main():
    #初始化套接字
    s = initSock()
    while True:
        # 接收消息
        if 0 == recvMsg(s):
            break

    #关闭套接字连接
    closeClient(s)

if __name__ == '__main__':
    main()
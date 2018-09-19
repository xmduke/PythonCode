# -*- coding:utf-8 -*-
import codecs
import frida,sys
#  输出的消息回调
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

#  获取远程设备
rdev = frida.get_remote_device();
#  附加进程
hooked_process = rdev.attach("com.example.y0n.fridasample");
#  创建一个 js 脚本
with codecs.open('./hookjs2.js', 'r', 'utf-8') as f:
    source = f.read()
#  创建脚本对象
script = hooked_process.create_script("Java.perform("+source+")");
#  指定消息回调
script.on('message', on_message);
#  加载脚本
script.load();
sys.stdin.read();
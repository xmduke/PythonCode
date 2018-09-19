# -*- coding:utf-8 -*-
#方式二：js代码和python代码分离
import codecs
import frida,sys
#  获取远程设备
rdev = frida.get_remote_device();
#  附加进程
hooked_process = rdev.attach("com.example.y0n.fridasample");
#  创建一个 js 脚本
with codecs.open('./hookjs.js', 'r', 'utf-8') as f:
    source = f.read()
#  创建脚本对象
script = hooked_process.create_script("Java.perform("+source+")");
#  加载脚本
script.load();
sys.stdin.read();
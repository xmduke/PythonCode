# -*- coding:utf-8 -*-

#方式一，将js作为字符串传入
import frida,sys
#  获取远程设备
rdev = frida.get_remote_device();
#  附加进程
hooked_process = rdev.attach("com.example.y0n.fridasample");
#  创建一个 js 脚本
jscode = """
Java.perform(function (v) {
// get hook Class
var MainActivity =
Java.use('com.example.y0n.fridasample.MainActivity');
// hook Method
MainActivity.add.implementation = function (v) {
return true;
};
});
"""
#  创建脚本对象
script = hooked_process.create_script(jscode);
#  加载脚本
script.load();
sys.stdin.read();
/**
 * Created by y0n on 2018/5/24.
 */
//方式三，hook住之后将js执行的结果进行回调，在python中显示
function hookcall() {
    // get hook Class
    var MainActivity =
    Java.use('com.example.y0n.fridasample.MainActivity');
    // hook Method
    MainActivity.add.implementation = function () {
        //  调用原始方法
        var bRet = this.add();
        send('bRet:' + bRet);
        //  访问成员变量
        //this.mString.value = 'hello';
        console.log("bRet: " + bRet);
        return true;
    };
}
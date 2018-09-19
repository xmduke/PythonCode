/**
 * Created by y0n on 2018/5/24.
 */
//方式二：js代码和python代码分离
function hookcall() {
    // get hook Class
    var MainActivity =
    Java.use('com.example.y0n.fridasample.MainActivity');
    // hook Method
    MainActivity.add.implementation = function (v) {
        var bRet = this.add(v);
        Console.log("bRet: " + bRet);
        return true;
    };
}
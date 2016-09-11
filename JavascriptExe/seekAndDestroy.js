/**
 * Created by meixuhong on 9/9/16.
 实现一个摧毁(destroyer)函数，第一个参数是待摧毁的数组，其余的参数是待摧毁的值。

 arguments 是一个类数组对象。代表传给一个function的参数列表。

 */


function destroyer(arr) {

    //从形参的第一个数字开始比较
    for(var i=1; i<arguments.length;i++){
        var num = arguments[i];

        //说明:filter的参数为需要过滤的函数function(名称可以省略), function的参数为前面数组arguments[0]的全部元素(依次遍历)
        arr = arguments[0].filter(function (x) {
            return x != num;

        });
    }
    console.log("arr:",arr);
    return arr;
}



destroyer([1, 2, 3, 1, 5,6,7,2, 3], 2, 3);
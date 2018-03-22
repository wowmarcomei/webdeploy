/**
 * Created by meixuhong on 9/9/16.
 */

/**
 真假美猴王！

 删除数组中的所有假值。

 在JavaScript中，假值有false、null、0、""、undefined 和 NaN。

 filter() 方法使用指定的函数测试所有元素，并创建一个包含所有通过测试的元素的新数组。

* */

//
// function isTrueValue(element) {
//     return Boolean(element);
//
// }

function bouncer(arr) {
    // Don't show a false ID to this bouncer.

    //说明:filter的参数为需要过滤的函数function(名称可以省略,与上面注释的函数isTrueValue功能类似), 此函数的参数是arr的每个元素的遍历
    arr= arr.filter(function (x) {
        return Boolean(x);
    });

    console.log(arr);

    return arr;
}

bouncer([7, "ate", "", false, 9]);
bouncer([false, null, 0, NaN, undefined, ""]);
bouncer([1, null, NaN, 2, undefined]);



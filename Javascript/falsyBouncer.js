/**
 * Created by meixuhong on 9/9/16.
 */

/**
 真假美猴王！

 删除数组中的所有假值。

 在JavaScript中，假值有false、null、0、""、undefined 和 NaN。

 filter() 方法使用指定的函数测试所有元素，并创建一个包含所有通过测试的元素的新数组。

* */


function isTrueValue(element) {
    return Boolean(element);

}

function bouncer(arr) {
    // Don't show a false ID to this bouncer.

    arr= arr.filter(isTrueValue);

    console.log(arr);

    return arr;
}

bouncer([7, "ate", "", false, 9]);
bouncer([false, null, 0, NaN, undefined, ""]);
bouncer([1, null, NaN, 2, undefined]);



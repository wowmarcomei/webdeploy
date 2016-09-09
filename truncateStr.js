/*
* 截断一个字符串！

 如果字符串的长度比指定的参数num长，则把多余的部分用...来表示。

 切记，插入到字符串尾部的三个点号也会计入字符串的长度。

 但是，如果指定的参数num小于或等于3，则添加的三个点号不会计入字符串的长度。
*/
function truncate(str, num) {
    // Clear out that junk in your trunk
    var strTemp = "";

    //如果要求截断的长度大于3

    if(num >= str.length){
        strTemp = str.slice(0,num);
        console.log(strTemp);
    } else if(num >= 3){
        strTemp = str.slice(0,num-3).concat("...");
        console.log(strTemp);
    } else { //如果要求截断的长度小于3
        strTemp = str.slice(0,num).concat("...");
    }

    return strTemp;
}

truncate("A-tisket a-tasket A green and yellow basket", 11);
truncate("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length);

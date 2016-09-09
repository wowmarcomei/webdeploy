/**
 * Created by meixuhong on 9/2/16.
 */

//确保字符串的每个单词首字母都大写，其余部分小写。
function titleCase(str) {
    //使用空格将字符串分成数组
    myArray = str.split(" ");

    //定义一个字符串,初始化为空,用于将二维数组重新转换为字符串
    var myStr = "";

    //新建一个一维数组,初始化为空
    var myObject = new Array();
    for(var i=0; i<myArray.length; i++){
        //建一个二维数组初始化为空,注意:只能对空数组赋值才有效
        myObject[i] = new Array();
        for (var j=0; j<myArray[i].length; j++)
        {
            if (j == 0){
                //首个字母大写
                myObject[i][j] = myArray[i].split("").shift().toLocaleUpperCase();
            } else{
                //其它小写
                myObject[i][j] = myArray[i][j].toLocaleLowerCase();
            }

        }
        //将数组重新转换为字符串
        myStr += myObject[i].join("").concat(" ");
      //  console.log("myStr:",i," times:", myStr);

    }
    //去掉字尾部的空格符号
    return myStr.substring(0,myStr.length-1);
}

console.log(titleCase("I'm a little tea pot"));
console.log(titleCase("sHoRt AnD sToUt"));
console.log(titleCase("HERE IS MY HANDLE HERE IS MY SPOUT"));

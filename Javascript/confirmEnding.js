/**
 * Created by meixuhong on 9/5/16.
 */
function confirmEnding(str, target) {

    //将字符串使用空格分离成数组
    var myArray = str.split(" ");

    //如果是单词则比较最后一个字符
    if(myArray.length == 1){

        //console.log( myArray[0].substr(myArray[0].length-target.length,target.length) === target );
        return myArray[0].substr(myArray[0].length-target.length,target.length) === target;

    }else { //如果是字符串则比较最后一个单词
        //console.log( myArray[myArray.length-1].substr(myArray[myArray.length-1].length-target.length,target.length) === target );
        return myArray[myArray.length-1].substr(myArray[myArray.length-1].length-target.length,target.length) === target;
    }

}

confirmEnding("Bastian", "an");
confirmEnding("He has to give me a new name", "name");
confirmEnding("He has to give me a new name", "me");
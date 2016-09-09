/**
 * Created by meixuhong on 9/8/16.
 */

function mutation(arr) {

    var myArray = new Array;

    //将传进来的字符串全部小写，赋值给新数组
    for(var i=0; i<arr.length; i++){
        myArray[i] = arr[i].toLowerCase();
    }

    var result1 = 0;
    var result2 = 0;
    var secondInFirst = 1;
    var firsrInSecond = 1;

    //查找第二个元素是否在第一个元素中,如果第二个字符串中有一个字符不出现在第一个字符串中，那么secondInFirst的值就会等于0，否则就会大于0
    for(var i=0; i<myArray[1].length; i++){
        result1 = myArray[0].indexOf(myArray[1][i]);
        secondInFirst *= (result1+1);
    }


    ////查找第一个元素是否在第二个元素中,如果第一个字符串中有一个字符不出现在第二个字符串中，那么firstInSecond的值就会等于0，否则就会大于0
    for(var i=0; i<myArray[0].length; i++){
        result2 = myArray[1].indexOf(myArray[0][i]);
        firsrInSecond *= (result2+1);
    }


    if(secondInFirst | firsrInSecond){
        console.log("true");
        return true;
    } else {
        console.log("false");
        return false;
    }

}

mutation(["hello", "hey"]);
mutation(["hello", "Hello"]);
mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]);
mutation(["Mary", "Army"]);
mutation(["Mary", "Aarmy"]);
mutation(["Alien", "line"]);
mutation(["floor", "for"]);
mutation(["hello", "neo"]);
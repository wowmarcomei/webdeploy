/**
 * Created by meixuhong on 9/10/16.
 */

/*
 凯撒密码Caesar cipher，又叫移位密码。

 移位密码也就是密码中的字母会按照指定的数量来做移位。

 一个常见的案例就是ROT13密码，字母会移位13个位置。由'A' ↔ 'N', 'B' ↔ 'O'，以此类推。

 写一个ROT13函数，实现输入加密字符串，输出解密字符串。

 所有的字母都是大写，不要转化任何非字母形式的字符(例如：空格，标点符号)，遇到这些特殊字符，跳过它们。

 rot13("SERR PBQR PNZC") 应该解码为 "FREE CODE CAMP"
 rot13("SERR CVMMN!") 应该解码为 "FREE PIZZA!"
 rot13("SERR YBIR?") 应该解码为 "FREE LOVE?"
 rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.") 应该解码为 "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."

 String.fromCharCode(65,66,67) // returns A,B,C
 "ABC".charCodeAt(0); // returns 65

 */



function rot13(str) {

    var myTemp = [];

    for(var i = 0; i<str.length; i++){

        if (str.charCodeAt(i) >= 65 && str.charCodeAt(i) <=77){
            myTemp[i]= String.fromCharCode(str.charCodeAt(i)+13);
            // console.log(String.fromCharCode(str.charCodeAt(i)+13));
        }else if(str.charCodeAt(i) >=78 && str.charCodeAt(i) <=90){
            myTemp[i]= String.fromCharCode(str.charCodeAt(i)-13);
            // console.log(String.fromCharCode(str.charCodeAt(i)-13));
        }else {
            myTemp[i] = str[i];
        }

    }
    str = myTemp.join("");
    return str;
}

// Change the inputs below to test
rot13("SERR PBQR PNZC");
rot13("SERR CVMMN!");
// rot13("A Z S");
// rot13("ABCDEFGHIJKLM NOPQRSTUVWXYZ");
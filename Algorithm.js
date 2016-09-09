/**
 * Created by meixuhong on 9/1/16.
 */

/*
//1.计算阶乘n!,例如: 5! = 1 * 2 * 3 * 4 * 5 = 120
 function factorialize(num) {

     var mySum = 1;

     if(num < 0)

         return -1;

     else if(num == 0 || num == 1){

        return 1;

     } else{

            while(num>0){

             mySum *= num--;

             }
     }

    return mySum;

   }

 factorialize(5);
*/

function findLongestWord(str) {
    var myLength = [0];
    var newRes = 0;
    var myArray = str.split(" ");
    for (var i = 0; i<myArray.length; i++){
        myLength[i] = myArray[i].length;
    }

    myLength.sort(function (a,b) {
        return b-a;
    });
    return myLength[0];

}

console.log(findLongestWord("What if we try a super-long word such as otorhinolaryngology"));
findLongestWord("What if we try a super-long word such as otorhinolaryngology");


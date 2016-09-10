/**
 * Created by meixuhong on 9/5/16.
 */
function largestOfFour(arr) {
    // You can do this!

    var myArray = [];

    for (var i=0; i< arr.length; i++)
    {
        for(var j=0;j<arr[i].length; j++)
        {
            //将二维数组排序,从大到小排序
            arr[i].sort(function (a,b) {
                return b-a;
            });
            console.log("j:",j);
        }
        myArray[i] = arr[i][0];
    }
    return myArray;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);

/**
 * Created by meixuhong on 9/6/16.
 */
/*
 猴子吃香蕉可是掰成好几段来吃哦！

 把一个数组arr按照指定的数组大小size分割成若干个数组块。

 例如:chunk([1,2,3,4],2)=[[1,2],[3,4]];

 chunk([1,2,3,4,5],2)=[[1,2],[3,4],[5]];
 */

function chunk(arr, size) {
    // Break it up.
    var myLength = Math.floor(arr.length/size);
    var myLeft = arr.length%size;

    if(myLeft){
        //需要分成size+1个数组

        //构造一维数组
        var myArray = new Array();

        //构造二维数组，取数组长度为size,使用slice()获取
        for (var i = 0; i < myLength; i++){
            myArray[i] = arr.slice(i*size,(i+1)*size);
        }

        //输出倒数myLeft个,组成最后一个数组
        for(var j=0; j<myLeft; j++){
            //myArray.push(arr[arr.length-myLeft+j]);
            myArray[myLength] = arr.slice(size*myLength,arr.length);
        }

    } else {
        //需要分成size个数组,每个数组中包含arr.length/size个元素
        var myArray = new Array();

        for (var i = 0; i < myLength; i++){

            myArray[i] = arr.slice(i*size,(i+1)*size);

        }

        console.log("myarray:",myArray);

    }


    return myArray;
}

chunk(["a", "b", "c", "d"], 2);// [["a", "b"], ["c", "d"]]
chunk([0, 1, 2, 3, 4, 5], 3); //[[0, 1, 2], [3, 4, 5]].
chunk([0, 1, 2, 3, 4, 5], 2);//[[0, 1], [2, 3], [4, 5]].
chunk([0, 1, 2, 3, 4, 5], 4);// [[0, 1, 2, 3], [4, 5]].
chunk([0, 1, 2, 3, 4, 5, 6], 3);//[[0, 1, 2], [3, 4, 5], [6]].
chunk([0, 1, 2, 3, 4, 5, 6, 7, 8], 4);//[[0, 1, 2, 3], [4, 5, 6, 7], [8]].

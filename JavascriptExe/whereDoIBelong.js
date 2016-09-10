/**
 * Created by meixuhong on 9/10/16.
 */


function where(arr, num) {
    // Find my place in this sorted array.

    arr.push(num);

    arr.sort(function compareValue(a,b) {
        return a - b;
    });

    return arr.indexOf(num);
}

where([40, 60,1,10,70,23,24], 50);

/**
 * Created by meixuhong on 9/8/16.
 */
function slasher(arr, howMany) {
    var myArray = arr.splice(0,howMany);

    console.log("myArray:",myArray,"\narr:",arr);

    return arr;
}

slasher([1, 2, 3], 9);
slasher(["burgers", "fries", "shake"], 1);
slasher([1, 2, "chicken", 3, "potatoes", "cheese", 4], 5);
/**
 * Created by meixuhong on 19/11/2016.
 */
$(document).ready(function () {
    // $("li").eq(2).css({
    //     backgroundColor: "red",
    // });

    $("li").filter(".top").css("backgroundColor", "red");
    $("li").not(".top").css("backgroundColor", "green");
});
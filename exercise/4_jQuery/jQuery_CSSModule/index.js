/**
 * Created by meixuhong on 19/11/2016.
 */
$(document).ready(function () {
    $("div").on("click",function () {
       $(this).height(30).css({
           cursor: "auto",
           backgroundColor: "green"
       });
    });
});
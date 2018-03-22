/**
 * Created by meixuhong on 16/11/2016.
 */
$("document").ready(function () {

    var clickTime = 1;
    $("#btn1").bind("click",function () {
        $("#p1").hide(1000);
        $("#p2").hide(1000);
    });

    $("#btn2").bind("click",function () {
        $("#p1").show(1000);
        $("#p2").show(1000);
    });

    $("#btn3").bind("click",function () {
        clickTime += 1;
        $("#p1").toggle(1000);
        $("#p2").toggle(1000);
        if(clickTime%2){
            $("#btn3").text("显示");
        }else{
            $("#btn3").text("隐藏");
        }
    });

    /**
     * 下面的这段是为了使用jQuery创建几个div，然后实现点击删除的效果
     *
    **/
    for(var i = 0; i<5; i++){
        $("<div>").appendTo(document.body);  //注意这里加元素的时候需要加<>符号。
    }

    $("div").bind("click",function () {
        $(this).hide(2000,function () {
            $(this).remove();
        });
    });

});
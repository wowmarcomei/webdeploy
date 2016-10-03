/**
 * Created by meixuhong on 10/3/16.
 */

function controlDisp() {
    var radio1 = document.getElementById("radio1");
    var radio2 = document.getElementById("radio2");
    var text = document.getElementById("text1");

    if(radio1.checked){
        text.disabled="";
    }else {
        text.value="";
        text.disabled = "disabled";
    }
}
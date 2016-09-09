/**
 * Created by meixuhong on 9/6/16.
 */
function repeat(str, num) {
    // repeat after me
    var strTemp = str;
    if(num<0){
        str = "";
    }else {
        for(var i=0; i<num-1; i++){
            str += strTemp;
        }
    }

    return str;
}

repeat("abc", 3);
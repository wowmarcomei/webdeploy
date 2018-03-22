/**
 * Created by meixuhong on 9/28/16.
 */

var box1Div, box2Div, msgDiv, img1;

window.onload = function () {
    //得到html页面上的div
    box1Div = document.getElementById("box1");
    box2Div = document.getElementById("box2");
    msgDiv = document.getElementById("msg");
    img1 = document.getElementById("img1");

    //监听div的拖入对象进入到target事件ondragenter,定义函数，传入事件对象e
    // box1Div.ondragenter = function (e) {
    //     showObj(e);
    // }

    //阻止系统的默认事件
    box1Div.ondragover = function (e) {
        e.preventDefault();
    }
    box2Div.ondragover = function (e) {
        e.preventDefault();
    }

    //通过监听被拖对象的ondragstart事件来获取被拖对象本身，
    img1.ondragstart = function (e) {
        //通过事件的dataTrasfer元素的setData函数获取,
        //注意，第二个参数为通过document.getElementByID得到的图片ID，第一个参数为将要设置的data的ID，可以在getData中调用
        e.dataTransfer.setData("imgID","img1");
    }

    //监听div的drop事件
    box1Div.ondrop = DragImage;
    box2Div.ondrop = DragImage;

function DragImage(e) {
    showObj(e.dataTransfer);
    e.preventDefault();

    //添加一个节点img，赋值为drag中设置的数据
    var img = document.getElementById(e.dataTransfer.getData("imgID"));
    //将节点数据放置在目标（div1box）中
    e.target.appendChild(img);
}
}

//创建一个函数遍历显示对象信息
function showObj(obj) {
    var s = "";

    for( var i in obj){
        s += i + ":" + obj[i] + "<br/>";
    }
    msgDiv.innerHTML = s;
}
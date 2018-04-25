> 浏览器所支持的唯一语言是javascript.

### 使用document选择文档
```js
document
```

### 使用querySelector选择元素，使用var定义变量
- 选择CSS类时，使用`,`选择元素

```js
var obj = document.querySelector(".hot-list");
```

- 选择ID时，使用`#`选择元素

```js
var obj = document.querySelector("#hot-list");
```

### 使用setAttribute设置对象属性

- 例：将元素隐藏

```js
obj.setAttribute("style","display:none");
```

- 将元素按照块元素显示

```js
obj.setAttribute("style","display:block");
```

#### 定义函数

```js
var dark = "background-color: black; color: white;";
var day = "background-color: white; color: black;";

var button = document.querySelector(".s_tab");
var web = document.querySelector("body");

function lightSwitch() {
    if (web.style.cssText == dark) {
        web.style.cssText = day;
        alert("Day mode");
    } else {
        web.style.cssText = dark;
        alert("Night mode");
    }
}
```

绑定单击元素事件为上诉定义的函数。

```js
button.onclick = lightSwitch
```


# Vue.js初使用

### 1.在模板中引用vue.js

```html
<script type="text/javascript" src="js/vue1.js"></script>
```

### 2.直接在模板中创建实例

```html
<script>
    // 创建Vue实例来进行管理页面
    var vm = new Vue({
        // 使用el(element)来定义管理区域，一般这个el选择这个页面的body
        // 定义完了el后，Vue就可以管理整个body
        el: "#app",
        // 使用data管理数据，配合django使用时，一般是从django中取出数据，相当于在django
        // 中从view往template中输送数据的context字典
        data: {
		
        }
    })
</script>
```

> - 使用`el`来定义管理区域，一般这个`el`选择这个页面的`body`


### Get 与 Post的区别

多数网页的访问一般使用GET方法，在需要使用身份验证等不希望数据参数暴露的情况时使用POST方法。

- 使用GET方法访问时，表单form中的参数会包含在URL中。

> https://duckduckgo.com/?q=cat&ia=web 其中的参数q与参数ia的值为cat与web，直接可以通过url观察到。

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fq56lmhnh5j30xa0fvt9p.jpg)

- 使用POST方法访问时，表单form中的参数不会包含在URL中。

> 从相同的client端POST数据到服务器时，URL没有变化，依然为"https://duckduckgo.com/"从URL中无法看出参数，只有通过调试器才可以观察到变量。

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fq56lnivf9j30w309z74f.jpg)

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fq56lmwf6dj30wd0fyjs8.jpg)

### form表单

form表单用于收集用户的输入信息。表单元素包含了`input元素`，`复选框`，`单选按钮`, `提交按钮`等等。

1. 文本输入

   ```html
   <input type="text" name="firstname">
   ```

2. 单选按钮输入

   ```html
   <input type="radio" name="sex" value="male">
   ```

3. 提交按钮

   ```html
   <input type="submit" value="Submit">
   ```

   或者

   ```html
   <button class="button" type="submit">Submit</button>
   ```

4. action属性

   表示将数据提交到服务器的哪个文件处理，如下表示提交到网站http://duckduckgo.com根目录处理

   ```html
   <form action="http://duckduckgo.com" method="post" class="ui form"></form>
   ```

5. method属性

   指示使用的方法为`get`，`post`或者其他。
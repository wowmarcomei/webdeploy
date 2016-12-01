### MongoDB使用

1. 在pycharm中使用Mongo Explorer插件进行管理

2. 使用pymongo包连接MongoDB数据库，例子：

   ```python
   from pymongo import MongoClient

   host = 'localhost'
   port = 27017

   client = MongoClient(host,port)
   db = client['test']
   sheet = db['sheet']

   for i in range(1001):
       print(i)
       sheet.insert_one({
           'name': 'name'+ str(i),
           'age': i,
       })
   ```

3. 将MongoDB数据库文件导出为json文件的方法：

   `mongoexport -d <数据库名称> -c <Collection名称> -o <输出的json文件的名称>`

4. 将MongoDB数据库文件导出为csv文件的方法：

   `mongoexport -d <数据库名称> -c <Collection名称> --csv -f <字段名称> -o <csv文件名称>`

5. 将json文件导入到MongoDB数据库中的方法：

   `mongoimport -d <数据库名称> -c <Collection名称> --file <json文件名称>`

6. 将csv文件导入到MongoDB数据库中的方法：

   `mongoimport -d <数据库名称> -c <Collection名称> --type csv --headerline --file <csv文件名称>`

7. MongoDB的常用命令

   ```python
   - mongo：启动mongo命令
   - mongod: 启动mongo数据库
   - db.createCollection('name'): 创建连接（相当于创建数据表）
   - db.'collctionname'.find(): 显示mongodb数据库中collection表的所有数据
   ```


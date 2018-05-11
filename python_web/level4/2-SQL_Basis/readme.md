

## 1. 连接MySQL服务器

> 输入用户名`root`,密码`***`

```mysql
$ mysql -u root -p
Enter password: *****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 5.7.21-log MySQL Community Server (GPL)

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

## 2. 查询当前服务器上有哪些数据库

```mysql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| demo               |
| django             |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
8 rows in set (0.00 sec)

mysql>
```

可以看出本服务器上存储的数据库文件有8个，其中`django`与`demo`是我们使用`Navicat`图形化工具创建的数据库。

## 3. 连接到其中一个数据库`django`中

```mysql
mysql> use django;
Database changed
mysql>
```

## 4. 查询当前数据库`django`中有哪些数据表

```mysql
mysql> show tables;
+----------------------------+
| Tables_in_django           |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| firstapp_article           |
| firstapp_book              |
| firstapp_book_authors      |
| firstapp_userprofile       |
+----------------------------+
14 rows in set (0.00 sec)

mysql>
```

其中`firstapp_article`，`firstapp_book `，`firstapp_book_authors`与`firstapp_userprofile`均是**自定义**的**Django**自动使用**Models**模型创建的数据表。

## 5. 查看数据表详情

```mysql
mysql> select * from firstapp_article;
+----+------------------------+----------------------------------+-------------+-------------+-------+-----------+
| id | title                  | content                          | create_time | like_counts | score | author_id |
+----+------------------------+----------------------------------+-------------+-------------+-------+-----------+
|  1 | 来试试看               | asdsf                            | 2018-05-08  |           3 |   6.1 |      NULL |
|  3 | OK, Lets try it again | 按时到家乐福及水电费垃圾堆上两个 | 2018-05-08  |           0 |   1.1 |      NULL |
+----+------------------------+----------------------------------+-------------+-------------+-------+-----------+
2 rows in set (0.01 sec)

mysql>
```

查询数据表`firstapp_article`的全部字段与记录。可以看出字段有`id`,`title`,`content`,`create_time`，`like_counts`，`score`和`author_id`。每条记录里均有这些字段的定义。

如果创建了一张数据表，未更新数据时，里面表是空的，可以通过以下命令来查询这个表有哪些字段。

```mysql
#查询数据表的字段信息
mysql> describe firstapp_article;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| title       | varchar(100) | NO   |     | NULL    |                |
| content     | longtext     | YES  |     | NULL    |                |
| create_time | date         | NO   |     | NULL    |                |
| like_counts | int(11)      | NO   |     | NULL    |                |
| score       | double       | NO   |     | NULL    |                |
| author_id   | int(11)      | YES  | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
7 rows in set (0.01 sec)

mysql>
```



## 6. 使用SQL语句创建用户账号并添加权限

- 添加账号命令格式如下，注意`允许IP`与`密码`是有单引号的。

```mysql
CREATE USER 用户名@'允许IP' IDENTIFIED BY '密码'
```

如使用root用户创建一个名为`marco`，密码为`root`的账号：

```mysql
mysql> CREATE USER marco@'localhost' IDENTIFIED BY 'root';
Query OK, 0 rows affected (0.04 sec)

mysql>
```

- 设置用户权限命令格式如下。

```mysql
//开放所有权限给marco用户，可以这样来写: 
mysql> GRANT ALL PRIVILEGES ON 数据库.数据表 TO marco@localhost;
//刷新系统权限表。 
mysql>flush privileges; 

//如果想指定部分权限（select,update）给marco用户，可以这样来写: 
mysql>grant select,update on phplampDB.* to marco@localhost; 
//刷新系统权限表。 
mysql>flush privileges; 
```

如，本例中给新建的账号`marco`对所有数据库中的所有数据表添加全部权限。

```mysql
mysql> GRANT ALL PRIVILEGES ON *.* TO marco@localhost;
Query OK, 0 rows affected (0.00 sec)

mysql>
```

## 7. SQL语句删除用户。 
其格式为：
```mysql
mysql> DELETE FROM user WHERE User="marco" and Host="localhost";  
mysql>flush privileges; 

//删除用户的数据库 
mysql>drop database 数据库;  
```

## 8. 使用SQL语句创建数据库

其格式如下（建议分下面三行创建，更清晰理解）,注意`utf-8`与`utf8_general_ci`是有单引号的：

```mysql
CREATE DATABASE 数据库 
DEFAULT CHARSET 'utf8' 
COLLATE 'utf8_general_ci';
```

如下面的例子中新创建一个名为`django_test`的数据库。

```mysql
mysql> CREATE DATABASE django_test
    -> DEFAULT CHARSET 'utf8'
    -> COLLATE 'utf8_general_ci';
Query OK, 1 row affected (0.00 sec)

mysql>
```

## 9. 删除数据库

其格式为：

```mysql
drop databse 数据库;
```

如下面的例子中删除新创建的数据库`django_test`.

```mysql
mysql> drop databse django_test;
```

## 10. 为数据库`database`添加数据表`table`

### 10.1 方法1：进入数据库直接添加

```mysql
mysql>use django_test
mysql>CREATE TABLE table_name (column_name column_type);
```

以下例子中我们将在 `django_test`数据库中创建数据表`article_test`：

```mysql
CREATE TABLE IF NOT EXISTS article_test(
   article_id INT UNSIGNED AUTO_INCREMENT,
   article_title VARCHAR(100) NOT NULL,
   article_author VARCHAR(40) NOT NULL,
   article_date DATE,
   PRIMARY KEY (article_id) 
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

实例解析：

- 如果不想字段为 **`NULL`** 可以设置字段的属性为 **`NOT NULL`**， 在操作数据库时如果输入该字段的数据为**`NULL`** ，就会报错。
- `AUTO_INCREMENT`定义列为自增的属性，一般用于主键，数值会自动加1。
- `PRIMARY KEY`关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。
- `ENGINE` 设置存储引擎，`CHARSET` 设置编码。

实例演示结果：

```mysql
mysql> CREATE TABLE IF NOT EXISTS article_test(
    ->  article_id INT UNSIGNED AUTO_INCREMENT,
    -> article_title VARCHAR(100) NOT NULL,
    -> article_author VARCHAR(40) NOT NULL,
    -> article_date DATE,
    -> PRIMARY KEY (article_id)
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
Query OK, 0 rows affected (0.03 sec)

mysql>
mysql> show tables;
+-----------------------+
| Tables_in_django_test |
+-----------------------+
| article_test          |
+-----------------------+
1 row in set (0.00 sec)

#查询数据表内容
mysql> select * from article_test;
Empty set (0.01 sec)

#查询数据表有哪些字段**Field**
mysql> describe article_test;
+----------------+------------------+------+-----+---------+----------------+
| Field          | Type             | Null | Key | Default | Extra          |
+----------------+------------------+------+-----+---------+----------------+
| article_id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| article_title  | varchar(100)     | NO   |     | NULL    |                |
| article_author | varchar(40)      | NO   |     | NULL    |                |
| article_date   | date             | YES  |     | NULL    |                |
+----------------+------------------+------+-----+---------+----------------+
4 rows in set (0.01 sec)

mysql>
mysql> drop table article_test;
Query OK, 0 rows affected (0.02 sec)

mysql>
```

### 10.2 方法2：指定数据库`database`添加数据表`table`

```mysql
mysql>CREATE TABLE database.table_name (column_name column_type);
```

以下例子中我们将在 `django_test`数据库中创建数据表`article_test`：

```mysql
CREATE TABLE IF NOT EXISTS django_test.article_test(
   article_id INT UNSIGNED AUTO_INCREMENT,
   article_title VARCHAR(100) NOT NULL,
   article_author VARCHAR(40) NOT NULL,
   article_date DATE,
   PRIMARY KEY (article_id) 
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

实例演示结果：

```mysql
#创建数据表，数据库django_test的数据表article_test
mysql> CREATE TABLE IF NOT EXISTS django_test.article_test(
    -> article_id INT UNSIGNED AUTO_INCREMENT,
    -> article_title VARCHAR(100) NOT NULL,
    -> article_author VARCHAR(40) NOT NULL,
    -> article_date DATE,
    -> PRIMARY KEY (article_id)
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
Query OK, 0 rows affected (0.03 sec)

#查询数据表被成功创建
mysql> show tables;
+-----------------------+
| Tables_in_django_test |
+-----------------------+
| article_test          |
+-----------------------+
1 row in set (0.00 sec)

#查询数据表的字段信息
mysql> describe article_test;
+----------------+------------------+------+-----+---------+----------------+
| Field          | Type             | Null | Key | Default | Extra          |
+----------------+------------------+------+-----+---------+----------------+
| article_id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| article_title  | varchar(100)     | NO   |     | NULL    |                |
| article_author | varchar(40)      | NO   |     | NULL    |                |
| article_date   | date             | YES  |     | NULL    |                |
+----------------+------------------+------+-----+---------+----------------+
4 rows in set (0.01 sec)

mysql>
```

## 11. 对数据库中的数据表进行增删该查操作

> 数据库的常见的四种操作即是：增、删、改、查

### 11.1 向表中插入新数据：增

##### 语法

以下为向MySQL数据表插入数据通用的 **INSERT INTO** SQL语法：

```mysql 
INSERT INTO table_name ( field1, field2,...fieldN )
VALUES
                       ( value1, value2,...valueN );
```

如果数据是字符型，必须使用单引号或者双引号，如："value"。

------

以下我们将使用 SQL **INSERT INTO** 语句向 MySQL 数据表 `article_test`插入数据

##### 实例

以下实例中我们将向 `article_test`表插入三条数据:

```mysql
#插入第一条数据到表article_test中，写了三个字段
mysql> INSERT INTO article_test (article_id, article_title, article_author)
    -> VALUES
    -> (1, 'first article', 'marco');
Query OK, 1 row affected (0.01 sec)

mysql>
mysql> select * from article_test;
+------------+---------------+----------------+--------------+
| article_id | article_title | article_author | article_date |
+------------+---------------+----------------+--------------+
|          1 | first article | marco          | NULL         |
+------------+---------------+----------------+--------------+
1 row in set (0.00 sec)

#插入第二条数据到表article_test中，写了三个字段
mysql>  INSERT INTO article_test (article_id, article_title, article_author)
    -> VALUES
    -> (2, 'second article', 'marco');
Query OK, 1 row affected (0.01 sec)

#插入第三条数据到表article_test中，写了两个字段
mysql> INSERT INTO article_test (article_title, article_author)
    -> VALUES
    -> ('third article','marco');
Query OK, 1 row affected (0.01 sec)

#查询数据表article_test内容，可知即使第三条数据没有写Article_id，默认也会被自动写入，因为
#article_id是主键，设置为自动增加的
mysql> select * from article_test;
+------------+----------------+----------------+--------------+
| article_id | article_title  | article_author | article_date |
+------------+----------------+----------------+--------------+
|          1 | first article  | marco          | NULL         |
|          2 | second article | marco          | NULL         |
|          3 | third article  | marco          | NULL         |
+------------+----------------+----------------+--------------+
3 rows in set (0.00 sec)

#查询表的字段信息，可知article_id为主键，自动增加
mysql> describe article_test;
+----------------+------------------+------+-----+---------+----------------+
| Field          | Type             | Null | Key | Default | Extra          |
+----------------+------------------+------+-----+---------+----------------+
| article_id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| article_title  | varchar(100)     | NO   |     | NULL    |                |
| article_author | varchar(40)      | NO   |     | NULL    |                |
| article_date   | date             | YES  |     | NULL    |                |
+----------------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql>
```

**注意：** 使用箭头标记 -> 不是 SQL 语句的一部分，它仅仅表示一个新行，如果一条SQL语句太长，我们可以通过回车键来创建一个新行来编写 SQL 语句，SQL 语句的命令结束符为分号 ;。

### 11.2 对表中删除数据：删

##### 语法

以下是`DELETE`命令删除 MySQL 数据表数据的通用 SQL 语法：

```mysql
DELETE FROM 数据表 WHERE 字段1='xxx' AND 字段2='xxx'
```

- 如果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。
- 可以在 WHERE 子句中指定任何条件。
- 可以在单个表中一次性删除记录。

以下我们将在 SQL `DELETE` 命令来删除 `article_test`表中指定的数据：

##### 实例

以下实例将删除数据表中 `article_id`为 1 的 记录：

```mysql
mysql> DELETE FROM article_test WHERE article_id=1;
Query OK, 1 row affected (0.01 sec)

mysql> select * from article_test;
+------------+----------------+----------------+--------------+
| article_id | article_title  | article_author | article_date |
+------------+----------------+----------------+--------------+
|          2 | second article | marco          | NULL         |
|          3 | third article  | marco          | NULL         |
+------------+----------------+----------------+--------------+
2 rows in set (0.00 sec)

mysql> DELETE FROM article_test WHERE article_id=2 AND article_author='marco';
Query OK, 1 row affected (0.01 sec)

mysql> select * from article_test;
+------------+---------------+----------------+--------------+
| article_id | article_title | article_author | article_date |
+------------+---------------+----------------+--------------+
|          3 | third article | marco          | NULL         |
+------------+---------------+----------------+--------------+
1 row in set (0.00 sec)

mysql>

```

### 11.3 向表中更新数据：改

##### 语法

以下是 `UPDATE `命令修改 MySQL 数据表数据的通用 SQL 语法：

```
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

- 你可以同时更新一个或多个字段。
- 你可以在 WHERE 子句中指定任何条件。
- 你可以在一个单独表中同时更新数据。

当你需要更新数据表中指定行的数据时 WHERE 子句是非常有用的。

------

以下我们将在 SQL `UPDATE` 命令使用` WHERE` 子句来更新 `article_test`表中指定的数据：

##### 实例

以下实例将更新数据表中 `article_id`为 1 的 `article_title与`与`article_author`字段值：

```mysql
mysql> UPDATE article_test SET article_title='update a new title', article_author='marco2' WHERE article_id=1;
Query OK, 0 rows affected (0.01 sec)
Rows matched: 1  Changed: 0  Warnings: 0
mysql> 
mysql> select * from article_test;
+------------+--------------------+----------------+--------------+
| article_id | article_title      | article_author | article_date |
+------------+--------------------+----------------+--------------+
|          1 | update a new title | marco2         | NULL         |
|          2 | second article     | marco          | NULL         |
|          3 | third article      | marco          | NULL         |
+------------+--------------------+----------------+--------------+
3 rows in set (0.00 sec)
mysql>
```

从结果上看，第一条记录的两个字段已经被成功修改。

### 11.4 查询数据表中的数据：查

##### 语法

以下是 `SELECT `命令查询 MySQL 数据表数据的通用 SQL 语法：

```
SELECT 数据表中字段 FROM 数据表 [WHERE Clause]
```

- 查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
- SELECT 命令可以读取一条或者多条记录。
- 你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据
- 你可以使用 WHERE 语句来包含任何条件。
- 你可以使用 LIMIT 属性来设定返回的记录数。
- 你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。

------

以下我们将在 SQL `SELECT` 命令使用` WHERE` 子句来查询表中指定的数据：

##### 实例

以下实例将查询`id`为3的article_test数据表的记录：

```mysql
mysql> SELECT * FROM article_test WHERE article_id=3;
+------------+---------------+----------------+--------------+
| article_id | article_title | article_author | article_date |
+------------+---------------+----------------+--------------+
|          3 | third article | marco          | NULL         |
+------------+---------------+----------------+--------------+
1 row in set (0.01 sec)

mysql>
```

查询article_test数据表的所有记录：

```mysql
mysql> select * from article_test;
+------------+----------------+----------------+--------------+
| article_id | article_title  | article_author | article_date |
+------------+----------------+----------------+--------------+
|          1 | first article  | marco          | NULL         |
|          2 | second article | marco          | NULL         |
|          3 | third article  | marco          | NULL         |
|          4 | forth article  | marco          | NULL         |
+------------+----------------+----------------+--------------+
4 rows in set (0.00 sec)

mysql>
```

### 11.5 使用`ORDER BY`对数据进行排序

##### 语法

以下是 SQL `SELECT` 语句使用 `ORDER BY` 子句将查询数据排序后再返回数据 ：

```mysql
SELECT field1, field2,...fieldN table_name1, table_name2...
ORDER BY field1, [field2...] [ASC [DESC]]
```

- 可以使用任何字段来作为排序的条件，从而返回排序后的查询结果。
- 可以设定多个字段来排序。
- 可以使用 `ASC` （Ascending）或 `DESC` （Descending ）关键字来设置查询结果是按升序或降序排列。 默认情况下，它是按升序排列。
- 可以添加 `WHERE...LIKE` 子句来设置条件。

**注意**：`ORDER BY`后面的字段必须跟的`int`型或者`date`型数据。

------

以下我们将使用 SQL `ORDER BY` 命令查询表中数据并进行排序：

##### 实例

以下示例将按照时间先后进行顺序排序。

```mysql
#原始数据库表内容
mysql> select * from article_test;
+------------+---------------+----------------+--------------+
| article_id | article_title | article_author | article_date |
+------------+---------------+----------------+--------------+
|          1 | 第一篇        | marco          | 2018-05-12   |
|          2 | 第二篇        | marco          | 2018-05-08   |
|          3 | 第三篇        | marco          | 2018-05-07   |
|          4 | 第四篇        | marco          | 2018-05-10   |
|          5 | 第五篇        | marco          | 2018-05-11   |
+------------+---------------+----------------+--------------+
5 rows in set (0.00 sec)

mysql>

#将数据表中数据按照时间先后进行正向排序，注意下面的例子中给字段添加了反引号，也可与上面的这些例子一样不加
#最好还是加上反引号，因为有可能该字段与数据库或者别的语言中的关键字冲突，
#还需要注意的是这个是反引号，不是单引号
mysql> SELECT * FROM `article_test` ORDER BY `article_date` ASC;
+------------+---------------+----------------+--------------+
| article_id | article_title | article_author | article_date |
+------------+---------------+----------------+--------------+
|          3 | 第三篇        | marco          | 2018-05-07   |
|          2 | 第二篇        | marco          | 2018-05-08   |
|          4 | 第四篇        | marco          | 2018-05-10   |
|          5 | 第五篇        | marco          | 2018-05-11   |
|          1 | 第一篇        | marco          | 2018-05-12   |
+------------+---------------+----------------+--------------+
5 rows in set (0.00 sec)

#将数据表中数据按照时间先后进行反向排序
mysql> SELECT * FROM `article_test` ORDER BY `article_date` DESC;
+------------+---------------+----------------+--------------+
| article_id | article_title | article_author | article_date |
+------------+---------------+----------------+--------------+
|          1 | 第一篇        | marco          | 2018-05-12   |
|          5 | 第五篇        | marco          | 2018-05-11   |
|          4 | 第四篇        | marco          | 2018-05-10   |
|          2 | 第二篇        | marco          | 2018-05-08   |
|          3 | 第三篇        | marco          | 2018-05-07   |
+------------+---------------+----------------+--------------+
5 rows in set (0.00 sec)

mysql>
```


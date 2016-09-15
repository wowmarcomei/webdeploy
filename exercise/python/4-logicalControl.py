
album = ['black star','David Bowie',25,True]
album.append('new album')

#定义if else条件判断语句,设置一个密码验证函数,并且设置函数的默认参数
def auto_login(password='abcdn'):
    password = input("Please input the password:")
    if password == '123456':
        print("correct, welcome to the new life!")
    else:
        print("your password is wrong, please check it again.")
        auto_login()

# auto_login()


#改进上面的函数,要求密码验证增加密码重置的功能
password_list= ['*#*#','123456']
def auto_login_pass():
    password = input("password:")
    correct_password = password == password_list[-1]
    reset_password = password == password_list[0]
    if correct_password:
        print("correct, welcome to the new life!\n")
    elif reset_password:
        password_list.append(input("Please input the new password:\n"))
        print("You've changed the password successfully!\n")
        auto_login_pass()
    else:
        print("password error, please try it again.\n")
        auto_login_pass()

# auto_login_pass()



# 定义for循环, 注意: for后面的变量即是in后面变量的每个item
for letter in "Hello world!":
    print(letter)

for num in range(1,11):
    print(num)

songlist = ['Holy driver','ThunderStack','Rebel Rebel']
for song in songlist:
    print(song)

#写一个函数定义9*9乘法表
for i in range(1,10):
    for j in range(1,10):
        print("{}*{}:{}".format(i,j,i*j))

#while循环
count = 0
result = 1;
while result:
    count += 1
    print("count:{}".format(count))
    if count == 5:
        result = 0
        break

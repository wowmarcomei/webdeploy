#定义一个函数将其从g转换为kg
def g2kg(val):
    return str(val/1000)+'kg'

print(g2kg(200))

#求直角三角形斜边长度
def getThiangle(a,b):
    return "The right triangle third side's length is: "+str((a*a + b*b)**(1/2))

print(getThiangle(3,4))

#定义函数的默认参数,设置一个函数求梯形面积
def trapezoid_area(base_up,base_down,height=5):
    return (base_up+base_down)*height*1/2

print("The area is: {}".format(trapezoid_area(3,4)))
print("The area is: {}".format(trapezoid_area(3,4,6)))


#定义一个函数,在桌面写入字符到文件,如果文件不存在,则创建该文件
def text_create(file_name, my_message):
    myPath = '/Users/meixuhong/webdeploy/pythonExe/' + file_name + '.txt'
    file = open(myPath,'a')
    print("myfile:{}".format(myPath))
    file.write(my_message)
    file.close()
    print("Done")
text_create('myText','Please try it first\n')
text_create('myText','Please try it again\n')

#定义一个文本过滤函数,设置默认参数为需要过滤的值与改变的值
def text_filter(word,censored_word='lame',changed_word='Awesome'):
    return word.replace(censored_word,changed_word)
# print(text_filter('Python is lame!'))
#定义一个函数,结合上面两个函数,创建一个文本,且将文本的内容进行过滤
def text_censored_create(name,msg):
    msg = text_filter(msg)
    text_create(name,msg)
text_censored_create('myText','Python is lame')
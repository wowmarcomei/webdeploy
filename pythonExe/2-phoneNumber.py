#隐藏Phone Number
phoneNumber = '185-8826-9898'
hideNumber = phoneNumber.replace(phoneNumber[:9],"*"*9)

print(hideNumber)

#查找Phone Number
phoneNumber1 = '185-1800-982'
phoneNumber2 = '180-0018-897'

search = '180'
print(search +' is at: '+str(phoneNumber1.find(search)) + ' to ' + str(phoneNumber1.find(search) + len(search)) + ' of '+ phoneNumber1);
print(search +' is at: '+str(phoneNumber2.find(search)) + ' to ' + str(phoneNumber2.find(search) + len(search)) + ' of '+ phoneNumber2);

#format格式化字符串
city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print("url is {0}: comes from {1}".format(url,city))

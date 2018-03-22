import requests
from bs4 import BeautifulSoup

headers= {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

proxies = {"https":"https://35.185.46.164:80"}

class Index(object):
    def __init__(self):
    	# 登陆地址
        self.loginurl = "http://passport.lianjia.com/cas/login?service=http%3A%2F%2Fsz.lianjia.com%2F"

    def login(self):
    	# 参数
        payload = {'Username': '18565687621', 'Password': 'Iou19871011'}
        # 保存cookie
        s = requests.Session()
        # 登陆
        r = s.get(self.loginurl, data=payload,headers=headers,proxies=proxies)

        wb_data = s.get("http://sz.lianjia.com/ershoufang/",headers = headers,proxies = proxies)
        soup = BeautifulSoup(wb_data.text,'lxml')
        print(soup)

    # def userinfo(self,s):
    #     r = s.get("http://sz.lianjia.com/ershoufang/",headers = headers,proxies = proxies)
    #     soup = BeautifulSoup(r.text,'lxml')
    #     print(soup)


username = '18565687621'
password = 'Iou19871011'

login_url = 'http://passport.lianjia.com/cas/login?service=http%3A%2F%2Fsz.lianjia.com%2F'
login = requests.session() #创建session进程会话，通过它，就可以共享cookie
q = login.get(login_url,headers=headers,proxies=proxies)  #访问需要模拟登录的网站，获取cookie
payload = { 'username': username,'password': password}
r = login.get(login_url,data = payload,headers=headers,proxies=proxies) #发送模拟登录的请求，顺利登录成功

wb_data = login.get('http://sz.lianjia.com/ershoufang/',data = payload,headers=headers,proxies=proxies)
soup = BeautifulSoup(wb_data.text,'lxml')
print(soup)

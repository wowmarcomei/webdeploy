from bs4 import BeautifulSoup
import requests
import time
from pymongo import MongoClient
import random
# 导入类库的时候就会进行类的初始化,执行__init__函数
# from extract_proxies import Proxies


host = 'localhost'
port = 27017

# 创建一个数据库client
client = MongoClient(host,port,connect=False)
# 创建一个数据库,名为58tongcheng
db = client['lianjia_sz']
# 给数据库添加collection
sheet_area= db['area']

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'sz.lianjia.com',
    'Cookie':'lianjia_uuid=8766201a-c321-fb3a-936b-1fbd77ee8625; lianjia_ssid=f52cf10a-f204-94a8-0afd-811856f35160',
    'Referer':'http://captcha.lianjia.com/?redirect=http%3A%2F%2Fsz.lianjia.com%2Fchengjiao%2Fluohuqu%2F',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

def get_area_deal_url(area,page,proxy = None):
    url = '{}pg{}'.format(area,str(page))

    if proxy == None:
        wb_data = requests.get(url, headers=headers,proxies={'http':'http://138.68.132.206:3128'})
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if soup.find_all('p',id="authType"):
            print("哎呀,我去,被抓了!============================\n\n\n\n\n\n\n\n")
            print(soup)
        else:
            pass
    else:
        wb_data = requests.get(url,headers={'User-Agent':random.choice(proxy.user_agent_list)},proxies = random.choice(proxy.ip_list))
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if soup.find_all('p',id="authType"):
            print("哎呀,悲剧了哦,被抓了!*************************\n\n\n\n\n\n\n\n")
            print(soup)
        else:
            pass

    time.sleep(2)

    xiaoqu = soup.select('div.info > div.title > a')
    area = soup.select('div > a.selected')[0].text if soup.find_all('a',class_='selected') else None

    for i in xiaoqu:
        data = {
            'title': i.get_text(),
            'url':i.get('href'),
            'area': area
        }

        # url数据库断点设计
        if data['url'] in [item['url'] for item in sheet_area.find()]:
            print('\n之前已经爬取了该url,跳过...\n')
            pass
        else:
            sheet_area.insert_one(data)
            print(data)

# 测试,实例化类Procies
get_area_deal_url('http://sz.lianjia.com/chengjiao/luohuqu/',1)



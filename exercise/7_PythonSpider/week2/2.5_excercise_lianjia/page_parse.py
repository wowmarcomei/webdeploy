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
sheet_item = db['item']

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

def get_area_deal_url(area,page,proxy = None):
    url = '{}pg{}'.format(area,str(page))

    if proxy == None:
        wb_data = requests.get(url, headers=headers,proxies={'http':'http://162.243.77.188:3128'})
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

    # time.sleep(2)

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
# get_area_deal_url('http://sz.lianjia.com/chengjiao/luohuqu/',1)

def get_deal_info(url,proxy = None):
    if proxy == None:
        wb_data = requests.get(url)
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


    # time.sleep(5)

    title = soup.select('div.house-title > div.wrapper')[0].get_text()
    deal_date = soup.select('div.house-title > div.wrapper > span')[0].get_text()
    dealTotalPrice = soup.select('div.price > span.dealTotalPrice > i')[0].get_text()
    unit_price = soup.select('div.price > b')[0].get_text()
    initial_price = soup.select('div.info.fr > div.msg > span:nth-of-type(1) > label')[0].get_text()
    dealDays = soup.select('div.info.fr > div.msg > span:nth-of-type(2) > label')[0].get_text()
    modify_price_times = soup.select('div.info.fr > div.msg > span:nth-of-type(3) > label')[0].get_text()
    huxing = soup.select('div.base > div.content > ul > li:nth-of-type(1)')[0].get_text()
    position = soup.select('div.base > div.content > ul > li:nth-of-type(2)')[0].get_text()
    square = soup.select('div.base > div.content > ul > li:nth-of-type(3)')[0].get_text()
    direction = soup.select('div.base > div.content > ul > li:nth-of-type(7)')[0].get_text()
    build_years = soup.select('div.base > div.content > ul > li:nth-of-type(8)')[0].get_text()
    hutibili = soup.select('div.base > div.content > ul > li:nth-of-type(12)')[0].get_text()
    years = soup.select('div.base > div.content > ul > li:nth-of-type(13)')[0].get_text()
    elevator = soup.select('div.base > div.content > ul > li:nth-of-type(14)')[0].get_text()

    data = {
        '小区': title.split()[0],
        '成交日期': deal_date.split()[0],
        '总价': dealTotalPrice,
        '单价': unit_price,
        '挂牌价格': initial_price,
        '成交周期': dealDays,
        '调价次数': modify_price_times,
        '户型': huxing,
        '楼层': position,
        '面积': square,
        '朝向': direction,
        '建筑年代': build_years,
        '户梯比例': hutibili,
        '产权年限': years,
        '配电电梯': elevator,
        '链接': url,
        #  注: mongodb的find函数返回一个cursor对象,类似于python的字典,但是无法像字典对象一样直接使用[]引用,故采用列表式
        '区域': [item['area'] for item in sheet_area.find({"url": "{}".format(url)})][0]
        # '区域': sheet_area.find({"url":"{}".format(url)})['area']
    }
    print(data)
    sheet_item.insert_one(data)


# get_deal_info('http://sz.lianjia.com/chengjiao/105100705533.html')


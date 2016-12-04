from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random
from channel_extract import url_list

client = pymongo.MongoClient('localhost',27017)
ganjidb = client['ganjidb']
ganji_url_list = ganjidb['ganji_url_list']
ganji_item_info = ganjidb['ganji_item_info']

headers  = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection':'keep-alive'
}

# http://cn-proxy.com/
proxy_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
    ]
proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}


# 爬虫1: 查询某个频道的第几页的所有商品的链接,存进数据库
def get_links_from(channel, page):
    url_page = '{}o{}'.format(channel,str(page))
    # print(url_pages)
    wb_data = requests.get(url_page)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #如果页面包含了'noinfotishi'类则表示当前的page里已经没有item了
    noMoreItems = len(soup.find_all('div', class_='noinfotishi'))
    print('hasMorePages is: {}.'.format(noMoreItems))
    if noMoreItems: # 如果值非0,表示确实出现了noinfotishi(404),那么该页面没有更多item了
        pass
        print('#########################################\nNo more items!!!\n')
    else:
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            ganji_url_list.insert_one({'url':item_link})
            print(item_link)

def get_allcategory_from(channel,numbers):
    for i in range(1,numbers+1):
        for url in channel.split():
            get_links_from(url,i)

#获取所有类别的前60页的链接
# get_allcategory_from(url_list,60)

# 爬虫2: 查询item的详细信息
def get_detail_from(url):
    wb_data = requests.get(url)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if wb_data.status_code == 404:
        pass
        print('\n************ good not exsit **************\n')
    else:
        title = soup.select('h1.info_titile')
        want_person = soup.select('p.info_p > span.want_person')
        price = soup.select('span.price_now > i')
        area = soup.select('div.palce_li > span > i')
        ganji_item_info.insert_one({'title':title[0].text,'want_person':want_person[0].text[0],'price':price[0].text,'area':area[0].text,'url':url})
        print('title[0].text:',title[0].text,'want_person[0].text:',want_person[0].text[0],'price[0].text:',price[0].text,'area[0].text:',area[0].text)

# get_detail_from('http://zhuanzhuan.ganji.com/detail/764638951092338689z.shtml')

def get_detail_pages(numbers):
    for item in ganji_url_list.find().limit(numbers):
        # print(item['url'])
        get_detail_from(item['url'])

get_detail_pages(10000)

from bs4 import BeautifulSoup
import requests
import time
import pymongo
from channel_extract import url_list

client = pymongo.MongoClient('localhost',27017)
ganjidb = client['ganjidb']
ganji_url_list = ganjidb['ganji_url_list']
ganji_item_info = ganjidb['ganji_item_info']

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
get_allcategory_from(url_list,60)

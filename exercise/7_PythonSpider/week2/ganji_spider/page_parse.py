from bs4 import BeautifulSoup
import requests
import time
from pymongo import MongoClient

host = 'localhost'
port = 27017

# 创建一个数据库client
client = MongoClient(host,port)
# 创建一个数据库,名为ganji_bj
db = client['bj_ganji']
# 给数据库添加collection
sheet_url = db['urls']
sheet_item = db['items']

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

def get_item_urls(cate_url,page):
    try:
        url_list_view = '{}o{}'.format(cate_url,str(page))
        print(url_list_view)
        wb_data = requests.get(url_list_view,headers=headers)
        soup = BeautifulSoup(wb_data.text,'lxml')
        time.sleep(1)

        # 去掉那些没有的页面,比如100页之后就是空的,所以不再爬取
        if soup.find_all('div',class_='noinfotishi'):
            pass
        else:
            links = soup.select('td.t > a.t')
            for link in links:
                # 判断是否为精准解析,通过对比分析发现,如果a的上上层父类,包含了zzjingzhun这个类的话,就是精准分析,我们过滤掉这部分的内容
                # 后来又发现还有一些分期付款的item,也将其过滤掉
                if len(link.find_parents("tr", class_="zzjingzhun")) or len(link.find_parents("tr", class_="fenqi_tr")) or len(link.find_parents("div", class_="zhiding")):
                    pass;
                else:
                    data = {
                        'title': link.get_text(),
                        'url': link.get('href'),
                    }
                    print(data)

                    # url数据库断点设计
                    # if data['url'] in [item['url'] for item in sheet_url.find()]:
                    #     print('\n之前已经爬取了该url,跳过...\n')
                    #     pass
                    # else:
                    #     sheet_url.insert_one(data)
                    #     print(data)
    except Exception as e:
        print('出现错误:{}'.format(e))
        # if num_retries > 0:
        #     print('xici proxy网站获取数据错误, 10s后即将重试!!!\n\n')
        #     time.sleep(10)
        #     return get_xici_proxies(url, num_retries - 1)

get_item_urls('http://bj.ganji.com/jiaju/',1)
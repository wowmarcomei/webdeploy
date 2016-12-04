from multiprocessing import Pool
from channel_extact import channel_list
from pages_parsing  import get_links_from, tongcheng_url_list,tongcheng_item_info,client,tongcheng


def get_all_links_from(channel):
    #获取某channel下的前100页的所有商品的links,将其存进数据库
    for i in range(1,100):
        get_links_from(channel,i)

def query_mongodb():
    for item in tongcheng_url_list.find():
        db_urls = [item['url']]
        print(item,db_urls)
        return db_urls

def select_mongodb():
    for item in tongcheng_url_list.find('url'):  # 1<value<5
        print(item)

if __name__ == '__main__':
    # pool = Pool()
    # pool.map(get_all_links_from,channel_list.split())
    query_mongodb()






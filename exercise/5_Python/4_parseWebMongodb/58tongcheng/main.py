from multiprocessing import Pool
from channel_extact import channel_list
from pages_parsing  import get_links_from,get_item_info, tongcheng_url_list,client,tongcheng


def get_all_links_from(channel):
    #获取某channel下的前100页的所有商品的links,将其存进数据库
    for i in range(1,100):
        get_links_from(channel,i)

def query_mongodb(db_numbers):
    '''
    查询数据库前db_numbers条数据,获取url列表并返回
    :param db_numbers: url数目
    :return: url列表
    '''
    db_urls = []
    #查询前20条数据库,获取得到非跳转"http://jump.zhineng.58.com/jump"的网址列表
    for item in tongcheng_url_list.find({'url':{'$ne':'http://jump.zhineng.58.com/jump'}}).limit(db_numbers):
        # db_urls = [item['url']]
        # print(item,db_urls)
        # return db_urls
        db_urls.append(item['url'])
    # print(db_urls)
    return db_urls

def query_items(numbers):
    for i in range(1,numbers+1):
        get_item_info(query_mongodb(numbers)[i-1])

if __name__ == '__main__':


    #查询前100条数据,单线程方法
    query_items(100)

    #多线程查询数据,查询前100条数据
    # pool = Pool()
    # pool.map(get_item_info, query_mongodb(100))






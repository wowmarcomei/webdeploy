from multiprocessing import Pool
from chanel_extract import channel_url_list
from page_parse import get_item_urls,get_item_details
from page_parse import sheet_url,sheet_item

# 获取没有被爬取的url列表
# 1.总的url
db_urls = [item['url'] for item in sheet_url.find()]
# 2.已经爬取了的url
index_urls = [item['url'] for item in sheet_item.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x - y

def get_all_links_from(channel):
    # 设置函数只有一个软参,便于传入map函数进行多进程运行
    for i in range(1,101):
        get_item_urls(channel,i)

if __name__ == '__main__':
    # 创建进程池,后续将需要多进程运行的函数放进进程池即可
    pool = Pool()
    # map函数比较神奇,会将第二个参数依次传给第一个参数(函数),并执行该函数,map返回一个list

    # 第一次执行爬虫1,爬取url,执行爬虫1的时候注释爬虫2
    # pool.map(get_all_links_from,channel_url_list.split())

    # 第二次执行爬虫2,爬取item信息,执行爬虫2的时候注释爬虫1
    pool.map(get_item_details,rest_of_urls)

    pool.close()
    pool.join()

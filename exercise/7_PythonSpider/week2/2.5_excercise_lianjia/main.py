from multiprocessing import Pool
from page_parse import get_area_deal_url,get_deal_info,sheet_area,sheet_item
from extract_area import area_name,area_deal_url,pages,area_name_test,area_list_test,pages_test
from extract_proxies import Proxies

# 获取没有被爬取的url列表

# 1.总的url
db_urls = [item['url'] for item in sheet_area.find()]
# 2.已经爬取了的url
index_urls = [item['链接'] for item in sheet_item.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x - y

def get_all_links_from(area,proxy = None):
    # 设置函数只有一个软参,便于传入map函数进行多进程运行
    for i in range(0,len(pages_test)):
        for page in range(1,pages_test[i]+1):
            # get_area_deal_url(area,page,proxy=proxy)
            get_area_deal_url(area,page)

if __name__ == '__main__':
    # 实例化Proxies类
    proxy = Proxies()

    # 创建进程池,后续将需要多进程运行的函数放进进程池即可
    pool = Pool()
    # map函数比较神奇,会将第二个参数依次传给第一个参数(函数),并执行该函数,map返回一个list

    # 第一次执行爬虫1,爬取url,执行爬虫1的时候注释爬虫2
    # pool.map(get_all_links_from,area_list_test)

    # 第二次执行爬虫2,爬取item信息,执行爬虫2的时候注释爬虫1
    pool.map(get_deal_info,rest_of_urls)

    pool.close()
    pool.join()

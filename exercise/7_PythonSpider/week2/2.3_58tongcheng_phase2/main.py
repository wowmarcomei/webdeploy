from multiprocessing import Pool
from chanel_extract import channel_url_list
from page_parse import get_item_urls

def get_all_links_from(channel):
    # 设置函数只有一个软参,便于传入map函数进行多进程运行
    for i in range(1,101):
        get_item_urls(channel,i)

if __name__ == '__main__':
    # 创建进程池,后续将需要多进程运行的函数放进进程池即可
    pool = Pool()
    # map函数比较神奇,会将第二个参数依次传给第一个参数(函数),并执行该函数,map返回一个list
    pool.map(get_all_links_from,channel_url_list.split())


print(channel_url_list.split())
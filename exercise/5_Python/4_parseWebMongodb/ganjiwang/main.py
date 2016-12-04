from multiprocessing import Pool
from pages_parse import ganji_url_list,ganji_item_info,get_links_from,get_allcategory_from,get_detail_from
from channel_extract import url_list

db_urls = [item['url'] for item in ganji_url_list.find()]
index_urls = [item['url'] for item in ganji_item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y

print('x:{},y:{},rest_of_urls:{}'.format(x,y,rest_of_urls))

# def get_all_links_from(channel):
#     for i in range(1,100):
#         ganji_url_list(channel,i)


# if __name__ == '__main__':
    # pool = Pool()
    # # pool = Pool()
    # # pool.map(get_all_links_from,url_list.split())
    # pool.close()
    # pool.join()
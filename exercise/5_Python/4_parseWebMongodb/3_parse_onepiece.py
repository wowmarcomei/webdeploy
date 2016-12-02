from bs4 import BeautifulSoup
import requests
import time
import pymongo
import urllib.request
path = '/Users/meixuhong/aaa'

# ================================== 设计数据库 ====================================
client = pymongo.MongoClient('localhost',27017)
onepiece = client['onepiece']
onepiece_pic = onepiece['onepiece_pic']

# ================================== 抓取多页数据 ==================================
def parseMultiplePages(chapter,page_num):
    img_urls = []
    for page_num in range(1,page_num+1):
        time.sleep(4)
        wb_data = requests.get('http://manhua.fzdm.com/2/{}/index_{}.html'.format(chapter,page_num))
        soup = BeautifulSoup(wb_data.text,'lxml')
        imgs = soup.select('div#mh > li > a > img')

        for img in imgs:
            data = {
                'img': img.get('src')
            }
            onepiece_pic.insert_one(data)

# 837话的前16页
parseMultiplePages(837,16)

# def dl_image(url):
#     urllib.request.urlretrieve(url,path + url.split('/')[-2] + url.split('/')[-1])
#     print('Done')
#
# #
# for url in get_image_url(10):
#     dl_image(url)

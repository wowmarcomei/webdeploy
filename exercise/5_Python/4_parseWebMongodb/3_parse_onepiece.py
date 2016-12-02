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



# ================================== 抓取单页数据 ==================================
def parseSinglePage(to_page_):
    url = 'http://manhua.fzdm.com/2/837/index_{}.html'.format(to_page_)
    wb_data = requests(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # titles = soup.select('#mh > h1')
    imgs = soup.select('#mhpic').get('src')
    print(imgs,url.split('/'),sep='\n================\n')

    #
    # for i in imgs:
    #     img_urls.append(i.get('src'))
    #
    # print((len(img_urls)), 'images shall be downloaded!')

    # urllib.request.urlretrieve(imgs,)


# def dl_image(url):
#     urllib.request.urlretrieve(url,path + url.split('/')[-2] + url.split('/')[-1])
#     print('Done')
#
# #
# for url in get_image_url(10):
#     dl_image(url)
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
            print(data)

# 837话的前16页
parseMultiplePages(837,16)


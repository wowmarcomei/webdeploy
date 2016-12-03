from bs4 import BeautifulSoup
import requests
import time
import pymongo
import urllib.request
import os
path = '/Users/meixuhong/OnePiece/'

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
            print(data)
            # onepiece_pic.insert_one(data)
            img_urls.append(data['img'])
    print('img_urls is a list as:',img_urls)
    return img_urls

# 837话的前16页
# parseMultiplePages(837,16)

# ================================== 下载漫画并命名 ==================================
def dl_images(chapter,img_urls):
    #==判断并创建目录==
    subPath = path + str(chapter) + '/'
    isExists = os.path.exists(subPath)
    if not isExists:
        print('create the path: {}...'.format(subPath))
        os.mkdir(subPath)
    else:
        print('the path already exsiting ...')
    # ==判断并创建目录==

    for i in range(1,len(img_urls)+1):
        # 使用urllib.request.urlretrieve(url, fine_path_name)下载文件
        urllib.request.urlretrieve(img_urls[i-1],subPath+str(i)+'_'+img_urls[i-1].split('/')[-1])
        print('\n{} downloaded and has been named as {}.\n'.format(img_urls[i-1],subPath+str(i)+'_'+img_urls[i-1].split('/')[-1]))

# ================================== 下载多话漫画 ==================================
def dl_chapters(chapter_from_,chapter_to_):
    for i in range(1,chapter_to_ - chapter_from_ + 1):
        dl_images(i,parseMultiplePages(i,18))

dl_chapters(800,848)

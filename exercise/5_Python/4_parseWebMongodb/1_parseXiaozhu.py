from bs4 import BeautifulSoup
import requests
import time
import pymongo

# ================================== 设计数据库 ====================================

client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
bnb_info = xiaozhu['bnb_info']

# ================================== 抓取单页数据 ==================================
def parseSinglePage():
    url = 'http://bj.xiaozhu.com/search-duanzufang-p20-0/'
    wb_data = requests(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('span.result_title')
    prices = soup.select('span.result_price > i')

    for title, price in zip(titles, prices):
        data = {
            'title': title.get_text(),
            'price': int(price.get_text())
        }
        bnb_info.insert_one(data)

    print('Done...')

# ================================== 抓取多页数据 ==================================
def parseMultiPageWithin(pages):
    for page_num in range(1,pages+1):
        time.sleep(4)
        wb_data = requests.get('http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(page_num))
        soup = BeautifulSoup(wb_data.text,'lxml')
        titles = soup.select('span.result_title')
        prices = soup.select('span.result_price > i')
        for title, price in zip(titles, prices):
            data = {
                'title': title.get_text(),
                'price': int(price.get_text())
            }
            bnb_info.insert_one(data)

    print('Done...')

# =================================== 查找数据库数据 ================================
def select_mongodb(db):
    '''
    筛选出所有words=0的行
    注: $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
    :return:
    '''
    for item in db.find({'price':{'$lt':500}}): #value>500
        print(item)

# =================================== 测试抓取数据 ==================================
# parseMultiPageWithin(4)
select_mongodb(bnb_info)




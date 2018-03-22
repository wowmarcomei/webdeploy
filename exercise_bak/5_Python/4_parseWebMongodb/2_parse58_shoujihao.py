from bs4 import BeautifulSoup
import requests
import time
import pymongo

url_shoujihao = 'http://bj.58.com/shoujihao/pn2'

client = pymongo.MongoClient('localhost',27017)
tongcheng = client['tongcheng']
tongcheng_phoneNumber = tongcheng['tongcheng_phoneNumber']

# ==================================爬取单页======================================
def get_single_page(url):
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    phoneNumbers = soup.select('strong.number')
    prices = soup.select('li > a.t > b.price')
    links = soup.select('a.t')

    for phoneNumber, price, link in zip(phoneNumbers,prices,links):
        data={
            'phoneNumber': phoneNumber.get_text(),
            'price': price.get_text(),
            'link': link.get('href')
        }
        print(data)
        tongcheng_phoneNumber.insert_one(data)


# get_single_page(url_shoujihao)

# ==================================爬取多页======================================
def get_multiple_pages(from_page_,to_page_):
    for i in range(from_page_, to_page_  + 1):
        url_list = 'http://bj.58.com/shoujihao/pn{}'.format(i)
        # print(url_list)
        get_single_page(url_list)

get_multiple_pages(2,12)
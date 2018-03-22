from bs4 import BeautifulSoup
import requests
import time
from pymongo import MongoClient

host = 'localhost'
port = 27017

# 创建一个数据库connection
client = MongoClient(host,port)
# 创建一个数据库,名为Test1
db = client['xiaozhu']
# 给数据库添加一个表,名为sheet
sheet_url = db['url']
sheet_detail = db['detail']

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i) for i in range(1,4,1)]

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'gr_user_id=317eb6b0-0ebc-45b4-89f8-12e1b882a011; abtest_ABTest4SearchDate=b; xzuuid=4b89a6a3; __utmt=1; OZ_1U_2282=vid=v8e06b1f46fd5d.0&ctime=1491736867&ltime=1491736865; OZ_1Y_2282=erefer=-&eurl=http%3A//bj.xiaozhu.com/&etime=1491736765&ctime=1491736867&ltime=1491736865&compid=2282; _ga=GA1.2.904424540.1491102496; __utma=29082403.904424540.1491102496.1491104424.1491736784.3; __utmb=29082403.5.10.1491736784; __utmc=29082403; __utmz=29082403.1491102500.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); gr_session_id_59a81cc7d8c04307ba183d331c373ef6=70da5677-1f98-4e59-bfd0-84ca5cbf221d'
}
proxies = {'https':'https://35.184.201.254:80'}

def get_house_links(url_list):
    for url in url_list:
        wb_data = requests.get(url,headers=headers,proxies=proxies)
        soup = BeautifulSoup(wb_data.text,'lxml')

        links = soup.select('div.result_btm_con.lodgeunitname')
        for link in links:
            data = {
                'link': link.get('detailurl')
            }
            print(data)
            sheet_url.insert_one(data)

# link获取之后注释掉,不再执行
# get_house_links(urls)

def get_house_details(url):
    wb_data = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    title = soup.select('div.pho_info > h4 > em')[0].text
    area = soup.select('div.pho_info > p')[0].get('title')
    price = soup.select('div.day_l > span')[0].get_text(),
    lorder_name = soup.select('a.lorder_name')[0].get_text(),
    lorder_gender = 'Man' if soup.find_all('span',class_='member_boy_ico') else 'Woman'
    lorder_profile = soup.select('div.member_pic > a > img')[0].get('src')

    data = {
        'title':title,
        'area':area,
        'price':int(price[0]), #观察价格最终打印出来的是一个小括号括起来的元祖变量,所以取其第一个数据,并将其转换为int变量
        'lorder_name':lorder_name[0], #观察房东姓名最终打印出来的是一个小括号括起来的元祖变量,所以取其第一个数据
        'lorder_gender':lorder_gender,
        'lorder_profile':lorder_profile,
        # '价格属性': isinstance(price[0],str),# 判断变量是否为字符串
    }
    print(data)
    sheet_detail.insert_one(data)

# 获取到数据写进数据库之后,不再执行
'''
for item in sheet_url.find():
    print(item['link'])
    get_house_details(item['link'])
'''

for item in sheet_detail.find({'price': {'$gt': 800}}):
    print(item)


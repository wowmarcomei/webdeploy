from bs4 import BeautifulSoup
import requests
import time
from pymongo import MongoClient

host = 'localhost'
port = 27017

# 创建一个数据库client
client = MongoClient(host,port)
# 创建一个数据库,名为58tongcheng
db = client['58tongcheng']
# 给数据库添加collection
sheet_phonenumber = db['58_phonenumber']

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'id58=c5/nn1jG1nt7740tOqjDAg==; bj58_id58s="SFkzaFJHS0R5UjNSNDc0Mg=="; als=0; myfeet_tooltip=end; bdshare_firstime=1491265900161; bj58_new_uv=2; final_history=26520838295997%2C29602192246606%2C26088204291258; _ga=GA1.2.1479444230.1491872757; sz=20174117375; 58home=sz; commontopbar_city=4%7C%u6DF1%u5733%7Csz; commonTopbar_myfeet_tooltip=end; city=bj; 58tj_uuid=341a5926-7769-47a6-a2eb-d054038f094c; new_session=0; new_uv=3; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.google.com.mm%252F; f=n'
}

proxies = {'https':'https://35.164.104.8:3128'}

base_url = 'http://bj.58.com/shoujihao/'

def get_phonenumber_info(url,page):
    url_list_view = '{}pn{}'.format(url,page)
    print(url_list_view)
    wb_data = requests.get(url_list_view, headers=headers, proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    time.sleep(1)

    if len(soup.select('div.boxlist > ul > div.boxlist')):

        links = soup.select('ul > li > a.t')
        phone_numbers = soup.select('ul > li > a.t > strong.number')

        for link, phone_number in zip(links,phone_numbers):
            # 判断是否为精准解析,通过对比分析发现,如果a的上上层父类,boxbg,就是精准分析,我们过滤掉这部分的内容
            if len(link.find_parents("div", class_="boxbg")):
                pass
            else:
                data = {
                    'link': link.get('href'),
                    'phone_number': phone_number.get_text()
                }
                print(data)
    else:
        return None
get_phonenumber_info(base_url,1)
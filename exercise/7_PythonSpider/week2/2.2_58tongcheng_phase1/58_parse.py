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
sheet_url = db['58_urls']
sheet_item = db['58_items']

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'id58=c5/nn1jG1nt7740tOqjDAg==; bj58_id58s="SFkzaFJHS0R5UjNSNDc0Mg=="; als=0; myfeet_tooltip=end; bdshare_firstime=1491265900161; bj58_new_uv=2; final_history=26520838295997%2C29602192246606%2C26088204291258; _ga=GA1.2.1479444230.1491872757; sz=20174117375; 58home=sz; commontopbar_city=4%7C%u6DF1%u5733%7Csz; commonTopbar_myfeet_tooltip=end; city=bj; 58tj_uuid=341a5926-7769-47a6-a2eb-d054038f094c; new_session=0; new_uv=3; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.google.com.mm%252F; f=n'
}

proxies = {'https':'https://35.164.104.8:3128'}

def has_class_but_not_id(tag,target_class,target_id):
    return tag.has_attr('{}'.format(target_class)) and not tag.has_attr('id')

def get_item_urls(cate_url,page,who_sell=0,):
    url_list_view = '{}{}/pn{}'.format(cate_url,str(who_sell),str(page))
    print(url_list_view)
    wb_data = requests.get(url_list_view,headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(1)

    # 去掉那些没有的页面,比如100页之后就是空的,所以不再爬取
    if soup.find_all('div',class_='noinfotishi'):
        pass
    else:
        links = soup.select('td.t > a.t')
        for link in links:
            # 判断是否为精准解析,通过对比分析发现,如果a的上上层父类,包含了zzjingzhun这个类的话,就是精准分析,我们过滤掉这部分的内容
            # 后来又发现还有一些分期付款的item,也将其过滤掉
            if len(link.find_parents("tr", class_="zzjingzhun")) or len(link.find_parents("tr", class_="fenqi_tr")) or len(link.find_parents("div", class_="zhiding")):
                pass;
            else:
                data = {
                    'title': link.get_text(),
                    'url': link.get('href'),
                }
                print(data)
                sheet_url.insert_one(data)
'''
for page in range(1,121,1):
    get_item_urls('http://bj.58.com/shouji/',page)
'''
def get_item_details(url):
    wb_data = requests.get(url,headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(1)

    title = soup.select('h1.info_titile')[0].get_text()
    price = soup.select('span.price_now > i')[0].get_text()
    area = soup.select('div.palce_li > span > i')[0].get_text()
    want_person = list(soup.select('span.want_person')[0].get_text())[0] if soup.find_all('span',class_='want_person') else None

    data = {
        'title':title,
        'price':price,
        'area':area,
        'want_person':want_person
    }
    print(data)
    sheet_item.insert_one(data)

for item in sheet_url.find().limit(2000):
    get_item_details(item['url'])





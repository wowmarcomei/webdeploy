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
sheet_url = db['urls']
sheet_item = db['items']

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'id58=c5/nn1jG1nt7740tOqjDAg==; bj58_id58s="SFkzaFJHS0R5UjNSNDc0Mg=="; als=0; myfeet_tooltip=end; bdshare_firstime=1491265900161; _ga=GA1.2.1479444230.1491872757; sz=20174117375; 58home=sz; commonTopbar_myfeet_tooltip=end; city=bj; es_ab=0; Hm_lvt_4f8818470616ef40f492f2b00cb36839=1492134401,1492178153; Hm_lpvt_4f8818470616ef40f492f2b00cb36839=1492178197; sessionid=58390cfc-8fff-449b-960d-3a15ab34b87c; Hm_lvt_3013163ef40dcfa5b06ea83e8a1a797f=1492134249,1492188021; Hm_lpvt_3013163ef40dcfa5b06ea83e8a1a797f=1492188028; bangbigtip2=1; Hm_lvt_ef9ab733a6772ffc77e498ec3aee46bd=1492188222; Hm_lpvt_ef9ab733a6772ffc77e498ec3aee46bd=1492188270; 58tj_uuid=341a5926-7769-47a6-a2eb-d054038f094c; new_uv=12; final_history=29695486354362%2C29682805275452%2C29717712878283%2C29718702442553%2C29718705361455; bj58_new_session=0; bj58_init_refer=""; bj58_new_uv=13'
}

proxies = {'https':'https://52.39.165.127:3128'}

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

# for item in sheet_url.find().limit(2000):
#     get_item_details(item['url'])





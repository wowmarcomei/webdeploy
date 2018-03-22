from bs4 import BeautifulSoup
import requests
import time

base_url = ['http://bj.58.com/pbdn/0/pn{}/'.format(str(i)) for i in range(1,10,1)]

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':'f=n; myfeet_tooltip=end; id58=c5/nn1jG1nt7740tOqjDAg==; bj58_new_session=1; bj58_init_refer=""; bj58_new_uv=1; bj58_id58s="SFkzaFJHS0R5UjNSNDc0Mg=="; sessionid=09d41ba9-5d74-4009-bb11-584e621d0c52; 58tj_uuid=341a5926-7769-47a6-a2eb-d054038f094c; new_session=1; new_uv=1; utm_source=; spm=; init_refer=; als=0; f=n'
}

headers_item_info = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
}

# 从https://www.us-proxy.org/处获取最新的免费proxy IP
proxies = {"https": "https://50.234.30.34:8080"}

links = []

def get_singlepage_link(url):
    '''
    获取单页面上所有平板电脑的link
    :param url:
    :return:
    '''
    wb_data = requests.get(url,headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(2)

    hrefs = soup.select('tr.zzinfo > td.t > a')
    for href in hrefs:
        a = href.get('href')
        links.append(a)
    print(links)

def get_links(pages):
    '''
    获取前pages页的所有平板电脑的link
    :param pages:
    :return:
    '''
    for i in range(0,pages):
        get_singlepage_link(base_url[i])
        print('\npage {} done!\n'.format(i))

def get_item_info(url):
    '''
    获取商品信息
    :param url:
    :return:
    '''
    wb_data = requests.get(url,headers=headers_item_info,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(2)
    cate = soup.select('div.breadCrumb.f12 > span.crb_i > a')[0].get_text()
    title = soup.select('div.info_lubotu.clearfix > div.box_left_top > h1')[0].get_text()
    price = soup.select('div.info_massege.left > div.price_li > span > i')[0].get_text()
    area = soup.select('div.palce_li > span > i')[0].get_text()
    print(cate,title,price,area,sep='\n=============\n')


# 获取前两页商品的link
get_links(2)
# 对每个link进行抓取数据
for link in links:
    get_item_info(link)
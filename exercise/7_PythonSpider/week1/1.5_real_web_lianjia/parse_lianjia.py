from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

headers_m = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

proxies = {"https":"https://191.96.43.23:8080"}

base_urls = ['http://sz.lianjia.com/chengjiao/pg{}/'.format(str(i)) for i in range(1,101,1)]

base_info = {}

def get_house_name_link(url):
    wb_data = requests.get(url,headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')

    titles = soup.select('ul.listContent > li > div.info > div.title > a')
    links = soup.select('div.info > div.title > a')

    for title,link, in zip(titles,links):
        # 插入字典数据
        base_info['{}'.format(title.get_text().split()[0])] = '{}'.format(link.get('href').split('/')[-1])
    print(base_info)

def get_house_name_links(pages):
    for i in range(0,pages,1):
        get_house_name_link(base_urls[i])
        print('\n\nDone {}\n\n'.format(i))

# get_house_name_links(10)

def get_house_info(url):
    wb_data = requests.get(url,headers=headers_m,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')

    a = soup.select('div > a.btn.btn_gray.post_ulog')[0].get('href')
    # a = soup.find_all('a',class_='getMoreHouse')
    print(a)

get_house_info('https://m.lianjia.com/sz/chengjiao/105100678720.html')
# get_house_info('http://sz.lianjia.com/chengjiao/105100688335.html')
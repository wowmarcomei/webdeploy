from bs4 import BeautifulSoup
import requests
import time
import urllib

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':'__whiAnonymousID=d3598a0375584aceab30c6e341a87736; __qca=P0-1145656028-1491176890838; login_token=3nyncjnpeHJPe96Km8n7; logged_in_earlier=true; auth=yes; _session=77e662483f0521cc06ff45222dc77c81; _ga=GA1.2.2032750655.1491176890; _gat=1; _weheartit_anonymous_session=%7B%22page_views%22%3A7%2C%22search_count%22%3A0%2C%22last_searches%22%3A%5B%5D%2C%22last_page_view_at%22%3A1491177979651%7D'
}

# 从网站http://freeproxylists.net/zh/?page=1处查找可以使用的代理服务器IP
proxies = {"http": "http://121.8.98.202:8081"}

urls = ['http://weheartit.com/inspirations/taylorswift?page={}'.format(str(i)) for i in range(1,21,1)]

pics = []

def get_singleurl_pic(url):
    wb_data = requests.get(url,headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(2)

    imgs = soup.select('img.entry-thumbnail')
    for img in imgs:
        pics.append(img.get('src'))

def get_pics(pages):
    for i in range(1,pages+1):
        get_singleurl_pic(urls[i-1])
        print('Done {}\n'.format(i))

def downlaod_pic(url):


get_pics(20)
print(pics)

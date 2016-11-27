from bs4 import BeautifulSoup
import requests
import time

url = 'http://wh.xiaozhu.com/'

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Cookie':'abtest_ABTest4SearchDate=b; gr_user_id=56d16465-6b38-406b-810a-9c1654776d7e; OZ_1U_2283=vid=v83a5d487b8dca.0&ctime=1480221204&ltime=1480221169; OZ_1Y_2283=erefer=-&eurl=http%3A//m.xiaozhu.com/search.html%3Fcityid%3D194%26city%3D%2525E6%2525AD%2525A6%2525E6%2525B1%252589%26offset%3D1%26step%3D15%26st%3D2016-11-27%26et%3D2016-11-28%26&etime=1480219976&ctime=1480221204&ltime=1480221169&compid=2283; OZ_1U_2282=vid=v83a5c8238700f.0&ctime=1480221524&ltime=1480221508; OZ_1Y_2282=erefer=https%3A//www.google.com.mm/&eurl=http%3A//www.xiaozhu.com/&etime=1480219778&ctime=1480221524&ltime=1480221508&compid=2282; _ga=GA1.2.536727213.1480219779; __utma=29082403.536727213.1480219779.1480219891.1480219891.1; __utmb=29082403.6.10.1480219891; __utmc=29082403; __utmz=29082403.1480219891.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); startDate=2016-11-27; endDate=2016-11-28; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=e7ba66f3-e339-46ff-88ce-2292e5d2c937',
}

def parse_attractions(url,data=None):
    wb_data = requests.get(url,headers=data)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('span.result_title.hiddenTxt')
    prices = soup.select('span.result_price')
    images = soup.select('img.lodgeunitpic')

    for title, price, image in zip(titles,prices,images):
        data={
            'title': title.get_text(),
            'price': price.get_text(),
            'image': image.get('src')
        }
        print(data)


def parse_attractions_byHeaders(url,data=None):
    wb_data = requests.get(url,headers=data)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('span.result_title.hiddenTxt')
    prices = soup.select('span.result_price')
    images = soup.select('img.lodgeunitpic')
    for title, price, image in zip(titles,prices,images):
        data={
            'title': title.get_text(),
            'price': price.get_text(),
            'image': image.get('src')
        }
        print(data)

parse_attractions_byHeaders(url,headers)
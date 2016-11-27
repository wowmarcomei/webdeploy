from bs4 import BeautifulSoup
import requests
import time

url = 'http://wh.xiaozhu.com/'


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


parse_attractions(url)


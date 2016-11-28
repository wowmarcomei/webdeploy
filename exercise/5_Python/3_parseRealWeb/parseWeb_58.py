from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.58.com/pbdn/0/'

def get_page(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(4)
    titles = soup.select('tr.zzinfo > td.t > a.t')
    prices = soup.select('tr.zzinfo > td.t > span.pricebiao > span.price')
    areas = soup.select('tr.zzinfo > td.t > span.fl > span')
    # print(titles,prices,areas,sep='\n==============\n')
    for title, price, area in zip(titles,prices,areas):
        data = {
            'title': title.get_text(),
            'price': price.get_text(),
            'area': area.get_text()
        }
        print(data)

get_page(url)




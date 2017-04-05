from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

proxies = {"https":"https://191.96.43.23:8080"}

base_urls = ['http://sz.lianjia.com/chengjiao/pg{}/'.format(str(i)) for i in range(1,101,1)]


wb_data = requests.get(base_urls[0],headers=headers,proxies=proxies)
soup = BeautifulSoup(wb_data.text,'lxml')

titles = soup.select('ul.listContent > li > div.info > div.title > a')
deal_dates = soup.select('div.dealDate')
total_prices = soup.select('div.totalPrice > span.number')
original_prices = soup.select('div.dealCycleeInfo > span.dealCycleTxt > span:nth-of-type(1)')
unit_prices = soup.select('div.unitPrice > span.number')
deal_cycle_dates = soup.select('div.dealCycleeInfo > span.dealCycleTxt > span:nth-of-type(2)')

for title,deal_date,total_price,original_price,unit_price,deal_cycle_date in zip(titles,deal_dates,total_prices,original_prices,unit_prices,deal_cycle_dates):
    data = {
        'title':title.get_text(),
        'deal_date':deal_date.get_text(),
        'total_price':total_price.get_text(),
        'original_price':original_price.get_text(),
        'unit_price':unit_price.get_text(),
        'deal_cycle_date':deal_cycle_date.get_text()
    }
    print(data)
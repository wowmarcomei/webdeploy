from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

proxies = {"https":"https://35.185.46.164:80"}

base_deal_urls = ['http://sz.lianjia.com/chengjiao/pg{}/'.format(str(i)) for i in range(1,101,1)]

xiaoqu_name = []
deal_xiaoqu_url = []

def get_xiaoqu_name(url_list,pages):
    '''
    通过成交的pages页的小区名字,构造一个url列表,里面的url对应各个小区的查询交易历史
    :param url_list: 每页的url
    :param pages: 前pages页
    :return:
    '''
    if pages <= len(url_list):
        for i in range(0,pages+1,1):
            wb_data = requests.get(url_list[i], headers=headers, proxies=proxies)
            soup = BeautifulSoup(wb_data.text, 'lxml')
            print(soup)

            titles = soup.select('ul.listContent > li > div.info > div.title > a')

            for title in titles:
                xiaoqu_name.append(title.get_text().split()[0])
                deal_xiaoqu_url.append('http://sz.lianjia.com/chengjiao/rs{}/'.format(title.get_text().split()[0]))
            print('\npage {} parse done.\n'.format(i+1))
    else:
        print('\n查询页数超过范围\n')
        i = 0
        for url in url_list:
            wb_data = requests.get(url, headers=headers, proxies=proxies)
            soup = BeautifulSoup(wb_data.text, 'lxml')

            titles = soup.select('ul.listContent > li > div.info > div.title > a')

            for title in titles:
                xiaoqu_name.append(title.get_text().split()[0])
                deal_xiaoqu_url.append('http://sz.lianjia.com/chengjiao/rs{}/'.format(title.get_text().split()[0]))
            print('\npage {} parse done.\n'.format(i + 1))

def get_xiaoqu_deal_history(url_list):
    '''
    获取小区成交历史
    :param url_list:
    :return:
    '''
    for url in url_list:
        wb_data = requests.get(url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(wb_data.text, 'lxml')

        titles = soup.select('div.title > a')
        deal_dates = soup.select('div.dealDate')
        total_prices = soup.select('div.totalPrice > span.number')
        unit_prices = soup.select('div.unitPrice > span.number')
        positions = soup.select('div.positionInfo')

        for title, deal_date, total_price, unit_price, position in zip(titles,deal_dates,total_prices,unit_prices,positions):
            data = {
                '小区':title.get_text(),
                '成交日期':deal_date.get_text(),
                '总价':total_price.get_text(),
                '单价':unit_price.get_text(),
                '楼层': position.get_text(),
                '链接': title.get('href')
            }
            print(data)
get_xiaoqu_name(base_deal_urls,1)
print(deal_xiaoqu_url)
get_xiaoqu_deal_history(deal_xiaoqu_url)
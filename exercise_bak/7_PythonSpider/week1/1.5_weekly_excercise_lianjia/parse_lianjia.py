from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie':'lianjia_uuid=44570456-454f-4fea-b50c-16782a84167c; UM_distinctid=15b3ba80a07431-060d7030b8029d-1d3c6853-100200-15b3ba80a08424; all-lj=c28812af28ef34a41ba2474a2b5c52c2; select_city=440300; _jzqckmp=1; select_nation=1; _smt_uid=589fe47d.30ecd8e7; CNZZDATA1255849469=839187306-1486871167-%7C1491611476; CNZZDATA1254525948=929449163-1486872105-%7C1491612403; CNZZDATA1255633284=658846300-1486873517-%7C1491612164; CNZZDATA1255604082=1608157061-1486873225-%7C1491611026; _jzqa=1.498319517247289860.1486873726.1491611556.1491616159.12; _jzqc=1; _jzqx=1.1486873726.1491616159.6.jzqsr=google%2Ecom|jzqct=/.jzqsr=sz%2Elianjia%2Ecom|jzqct=/; _qzja=1.1192549459.1486873744623.1491611555733.1491616159316.1491613506125.1491616159316.0.0.0.69.12; _qzjc=1; _qzjto=7.2.0; _ga=GA1.2.1716571364.1486873731'
}

proxies = {"https":"https://35.185.46.164:80"}

base_deal_urls = ['http://sz.lianjia.com/chengjiao/pg{}/'.format(str(i)) for i in range(1,101,1)]

# 存储前100页成交的小区名字列表
xiaoqu_name = []
# 存储小区成交记录的url列表
deal_xiaoqu_url = []

def get_xiaoqu_name(url_list,pages):
    '''
    通过前pages页填写小区名字列表与成交记录列表
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
    获取单个小区成交历史
    :param url_list: 成交小区的url列表
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

# 获取前第1页成交小区名字
# get_xiaoqu_name(base_deal_urls,1)

# 获取前第一页成交的各个小区的成交历史
# get_xiaoqu_deal_history(deal_xiaoqu_url)

def get_house_deal_details(url):
    wb_data = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    area = list(soup.select('div.deal-bread')[0].stripped_strings)
    labels = list(soup.select('div.base > div.content > ul')[0].stripped_strings)
    transaction = list(soup.select('div.transaction > div.content > ul')[0].stripped_strings)

    print('\n区域为:{}\n'.format(area))
    print('\n其他信息为:{}\n'.format(labels))
    print('\n交易信息为:{}\n'.format(transaction))


get_house_deal_details('http://sz.lianjia.com/chengjiao/105100125100.html')
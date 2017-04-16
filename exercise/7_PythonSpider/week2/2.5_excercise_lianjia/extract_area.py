from bs4 import BeautifulSoup
import requests
import re
import time

url_start = 'http://sz.lianjia.com/chengjiao/'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'lianjia_uuid=44570456-454f-4fea-b50c-16782a84167c; UM_distinctid=15b3ba80a07431-060d7030b8029d-1d3c6853-100200-15b3ba80a08424; _jzqx=1.1486873726.1491785863.8.jzqsr=google%2Ecom|jzqct=/.jzqsr=lianjia%2Ecom|jzqct=/; _jzqa=1.498319517247289860.1486873726.1491785863.1492129028.17; _qzja=1.1192549459.1486873744623.1491785861685.1492129027946.1491786324624.1492129027946.0.0.0.94.16; select_city=440300; all-lj=c28812af28ef34a41ba2474a2b5c52c2; _smt_uid=589fe47d.30ecd8e7; CNZZDATA1255849469=839187306-1486871167-%7C1492302664; CNZZDATA1254525948=929449163-1486872105-%7C1492303659; CNZZDATA1255633284=658846300-1486873517-%7C1492300898; CNZZDATA1255604082=1608157061-1486873225-%7C1492302371; _ga=GA1.2.1716571364.1486873731; lianjia_ssid=0c2d97d4-41eb-4f36-8273-cc2956d55dfa'
}

proxies = {'https':'https://35.164.104.8:3128'}

area_name = []
area_deal_url = []
pages = []

def get_area_name_urls(url=url_start):
    wb_data = requests.get(url,headers =headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')

    areas = soup.select('div.m-filter > div.position > dl > dd > div > div > a')

    for area in areas:
        data = {
            'area':area.get_text(),
            'url': 'http://sz.lianjia.com'+area.get('href')
        }
        print(data)
        area_name.append(data['area'])
        area_deal_url.append(data['url'])


def get_area_pages(area):
    '''
    获取单个area的成交页数
    :param area: 区域url
    '''
    wb_data = requests.get(area,headers=headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(1)

    page_num = int(re.findall(r"\d+\.?\d*",soup.select('div.page-box.house-lst-page-box')[0].get('page-data').split(',')[0])[0]) if soup.find_all('div',class_='page-box') else 1
    pages.append(page_num)
    print(page_num)

'''
# 获取各个区域名字与对应url
get_area_name_urls()
# 获取各个区域对应的成交页数
for area in area_deal_url:
    get_area_pages(area)

print('\n=========================================\n')
print(area_name)
print(area_deal_url)
print(pages)
'''

area_name_test = ['罗湖区', '福田区', '南山区', '盐田区', '宝安区', '龙岗区', '龙华区', '光明新区', '坪山区', '大鹏新区']
area_list_test = ['http://sz.lianjia.com/chengjiao/luohuqu/', 'http://sz.lianjia.com/chengjiao/futianqu/', 'http://sz.lianjia.com/chengjiao/nanshanqu/', 'http://sz.lianjia.com/chengjiao/yantianqu/', 'http://sz.lianjia.com/chengjiao/baoanqu/', 'http://sz.lianjia.com/chengjiao/longgangqu/', 'http://sz.lianjia.com/chengjiao/longhuaqu/', 'http://sz.lianjia.com/chengjiao/guangmingxinqu/', 'http://sz.lianjia.com/chengjiao/pingshanqu/', 'http://sz.lianjia.com/chengjiao/dapengxinqu/']
pages_test = [100, 100, 100, 49, 100, 100, 100, 1, 1, 1]

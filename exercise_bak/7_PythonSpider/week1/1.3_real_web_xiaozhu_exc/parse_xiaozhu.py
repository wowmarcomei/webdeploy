from bs4 import BeautifulSoup
import requests
import time

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,14,1)]

links = []

def get_link(url):
    '''
    获取某页的各个链接的url
    :param url:
    :return:
    '''
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(4)

    links = soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname')
    hrefs = [row.get('detailurl') for row in links]
    # print(hrefs)
    return hrefs

def get_links(links=None):
    '''
    获取所有页面的链接url,这个例子中是1-13页,将其结果存放于列表links中
    :param links:
    :return:
    '''
    for url in urls:
        links += get_link(url)

def get_details(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    time.sleep(4)

    # 说明: soup.select返回的是一个列表,对于详情页一般只有一个结果,这个时候可以使用[0]来获取列表内容,使用.text获取内容,get函数获取相应属性内容
    title = soup.select('div.con_l > div.pho_info > h4 > em')[0].text
    address = soup.select('div.con_l > div.pho_info > p > span')[0].text
    price = soup.select('#pricePart > div.day_l > span')[0].text
    image = soup.select('#curBigImage')[0].get('src')
    landlord_profile = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
    landlord_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text
    landlord_gender = 'Man' if soup.find_all('span',class_='member_boy_ico') else 'Woman'

    data = {
        'title':title,
        'address':address,
        'price':price,
        'image':image,
        'landlord_profile':landlord_profile,
        'landlord_name':landlord_name,
        'landlord_gender':landlord_gender
    }

    print('\n==================================\n')
    print(data)
    print('\n==================================\n')


# 获取到所有链接,将其赋值到links中
get_links(links=links)

for link in links:
    get_details(link)

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
tongcheng = client['tongcheng']
tongcheng_url_list = tongcheng['tongcheng_url_list']
tongcheng_item_info = tongcheng['tongcheng_item_info']

# 爬虫1: 查询某个频道的第几页的所有商品的链接,存进数据库
def get_links_from(channel, pages, who_sells=0):
    '''
    查询某个频道的第几页的所有商品的链接,存进数据库
    :param channel: 某个频道,分类
    :param pages: 第几页
    :param who_sells: 0表示个人,1表示商家
    :return:
    '''
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    wb_data = requests.get(list_view)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')

    # 如果没有 td.t 就表明页面已经翻到了最后几页
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'): #soup.lect返回的是一个列表
            item_link = link.get('href').split('?')[0] #使用问号?将返回地址分开取?号前面的部分
            tongcheng_url_list.insert_one({'url': item_link}) #插入数据库中
            print(item_link)
    else:
        pass

# 爬虫2: 爬取详情页数据
def get_item_info(url):
    '''
    爬取详情页的数据信息
    :param url: 网址
    :return:
    '''
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # soup.find返回tag列表eg:[<title>The Dormouse's story</title>]
    no_longer_exsit = '404' in soup.find('script',type='text/javascript').get('src').split('/')
    if no_longer_exsit:
        pass
    else:
        titles = soup.select('div.col_sub.mainTitle > h1')[0].text #soup.select返回的是一个列表
        times = soup.select('ul.mtit_con_left.fl > li.time')[0].text
        prices = soup.select('div.su_con > span.price.c_f50')[0].text
        #下面这句表示如果在soup中找到了span标签且其class属性为c_25d的话就填写areas的值,否则为空
        areas = list(soup.select('.c_25d a'))[-1].text if soup.find_all('span','c_25d') else None
        # 插入数据库
        tongcheng_item_info.insert_one({'title': titles, 'price': prices, 'time': times, 'area': areas, 'url': url})
        print({'title': titles, 'price': prices, 'time': times, 'area': areas, 'url': url})


# get_item_info('http://bj.58.com/shouji/27938628086735x.shtml')
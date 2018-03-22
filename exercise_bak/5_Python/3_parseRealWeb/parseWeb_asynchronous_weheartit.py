from bs4 import BeautifulSoup
import requests
import urllib.request
import time

url = 'http://weheartit.com/?page=2&before=268024244'
# urls = ['http://weheartit.com/?page={}&before={}'.format(str(i),str(j)) for i,j in zip(range(1,10,1),range(1,100,20))]
path = '/Users/meixuhong/aaaaa/'

# proxies = {"http": "113.17.169.18:808"}
# 此网站会有针对 ip 的反爬取，可以采用代理的方式

# wb_data = requests.get(url,proxies=proxies)
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

def get_page(url,data=None):
    img_urls = []
    wb_data = requests.get(url)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')
    images = soup.select('div.entry-preview > a.js-entry-detail-link > img')
    for i in images:
        img_urls.append(i.get('src'))
    print((len(img_urls)),' images should be downlaoded!\n=====\n')
    print(img_urls,sep='\n********\n')
    return img_urls

'''
Download the images by 'urllib.request.urlretrieve'
Copy a network object denoted by a URL to a local file
'''
def dl_image(url):
    #使用urllib.request.urlretrieve下载files, 使用url.split('/')将url通过斜杠分割成列表
    urllib.request.urlretrieve(url,path + url.split('/')[-2] + url.split('/')[-1])
    print('Done')

#
for url in get_page(url):
    dl_image(url)



from bs4 import BeautifulSoup
import requests

'''
url = 'https://cn.tripadvisor.com/Tourism-g298184-Tokyo_Tokyo_Prefecture_Kanto-Vacations.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

titles = soup.select('div div > a.hotel.name')
images = soup.select('img[width="400"]')
# cates = soup.select('div.p13n_reasoning_v2')
# print(titles,images,cates,sep='\n***********\n')

for title,image in zip(titles,images):
    data = {
        'title': title.get_text(),
        'img': image.get('src'),
        # 'cate': list(cate.stripped_strings)
    }
    print(data)
###上面这段代码获取的img全为一个地址,是因为网页做了JS控制进行反爬取,所以下面将使用harders与cookies进行抓取数据
'''

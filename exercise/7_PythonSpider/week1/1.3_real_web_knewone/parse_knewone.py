from bs4 import BeautifulSoup
import requests
import time

url = ['https://knewone.com/?page={}'.format(str(i)) for i in range(1,11,1)]

def get_web_info(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')

    titles = soup.select('section.content > h4 > a')
    images = soup.select('a.cover-inner > img')
    links =  soup.select('section.content > h4 > a')

    for title,image,link in zip(titles,images,links):
        data = {
            'title':title.get('title'),
            'image':image.get('src'),
            'link':'https://knewone.com/'+link.get('href')
        }
        print(data)

for single_url in url:
    get_web_info(single_url)
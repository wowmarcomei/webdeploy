from bs4 import BeautifulSoup
import requests
import time

url = 'https://knewone.com/things?page='

def get_page(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    images = soup.select('a.cover-inner > img')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')

    for image, title, link in zip(images,titles,links):
        data={
            'image': image.get('src'),
            'title': title.get('title'),
            'link': link.get('href')
        }
        print(data,sep='\n=======================\n')

def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(4)

get_more_pages(1,10)
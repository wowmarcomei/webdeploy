from bs4 import BeautifulSoup

with open('/Users/meixuhong/workstation/exercise/7_PythonSpider/week1/1.2_local_web_parse_exercise/index.html','r',encoding='utf-8') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    rates = Soup.find_all()
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')

    print(titles,prices,reviews,rates,images,sep='\n=============\n\n\n')

for title,price,review,image in zip(titles,prices,reviews,images):
    print(title.get_text(),price.get_text(),str(review.get_text().split(' ')[0]),image.get('src'),sep='-->')

from bs4 import BeautifulSoup

info = []

# 注: soup.select返回结果为列表, 可以使用nth-of-type(n)来选择列表元素,如下面的rates列表
with open('/Users/meixuhong/workstation/exercise/7_PythonSpider/week1/1.2_local_web_parse_exercise/index.html','r',encoding='utf-8') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    rates = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')

# print(Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p'))
# print(Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)'))


for title,price,review,image,rate in zip(titles,prices,reviews,images,rates):
    # print(title.get_text(),price.get_text(),str(review.get_text().split(' ')[0]),image.get('src'),len(rate.find_all('span',class_='glyphicon glyphicon-star')),sep='-->')
    data = {
        'title':title.get_text(),
        'price':price.get_text(),
        'review':review.get_text().split(' ')[0],
        'image':image.get('src'),
        'rates':len(rate.find_all('span',class_='glyphicon glyphicon-star'))
    }
    print(data)
    info.append(data)

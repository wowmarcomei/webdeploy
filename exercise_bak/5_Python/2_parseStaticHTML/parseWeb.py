from bs4 import BeautifulSoup

path = './web/index.html'
info = []  #存储解析数据列表

with open(path,'r',encoding='utf8') as file:  #加入解析编码为utf8,否则报错
    Soup = BeautifulSoup(file.read(),'lxml')
    # 注意各个元素之间务必使用空格,否则报错:'Unsupported or invalid CSS selector: "%s"' % token)
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    descs = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > p')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    # print(images,titles,prices,descs,stars,reviews,sep='\n************\n\n')

for image, title, price, desc, star, review in zip(images,titles,prices,descs,stars,reviews):
    data = {
        'iamge': image.get('src'),
        'title': title.get_text(),
        'price': price.get_text(),
        'desc': desc.get_text(),
        'star': len(star.find_all("span", class_ = "glyphicon glyphicon-star")), #按BeautifulSoup使用find_all函数支持CSS搜索
        'review': review.get_text()
    }
    info.append(data)
    print(info)

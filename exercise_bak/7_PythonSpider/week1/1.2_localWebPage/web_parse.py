from bs4 import BeautifulSoup

info = []

with open('/Users/meixuhong/workstation/exercise/7_PythonSpider/week1/1.2_localWebPage/web/new_index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    images = Soup.select('body > div.main-content > ul > li > img')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    # print(titles,images,rates,descs,cates,sep='\n=================\n')

    for title,image,rate,desc,cate in zip(titles,images,rates,descs,cates):
        data = {
            'title':title.get_text(),
            'image':image.get('src'),
            'rate':rate.get_text(),
            'desc':desc.get_text(),
            'cate': list(cate.stripped_strings)
        }
        print(data)
        info.append(data)

    for i in info:
        if float(i['rate']) >= 4.0:
            print(i['title'],i['cate'])

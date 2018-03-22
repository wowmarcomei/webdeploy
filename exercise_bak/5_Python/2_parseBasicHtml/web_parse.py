from bs4 import BeautifulSoup

# 定义一个列表info,将数据筛选的数据放置在列表中,便于查找数据
info = []

with open('./index.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    # print(images,titles,descs,rates,sep='\n-----------------\n\n')

# for image in images:
#     print(image.get('src'))   #获取标签属性
# print('===============\n')
# for title in titles:
#     print(title.get_text())   #获取文本
# print('===============\n')
# for desc in descs:
#     print(desc.get_text())    #获取文本
# print('===============\n')
# for rate in rates:
#     print(rate.get_text())    #获取文本

#使用zip函数循环,将数据放置在字典中
for image,title,desc,cate,rate in zip(images,titles,descs,cates,rates):
    data = {
        'image': image.get('src'),
        'title': title.get_text(),
        'desc': desc.get_text(),
        'cate': list(cate.stripped_strings),
        'rate': rate.get_text()
    }
    # print(data)
    info.append(data)
    # print(info)
    # print("\n==========================================\n")

#赛选出所有评分大于3.5分的文章
for i in info:
    if float(i['rate'])>3.5:
        print(i['title'],i['cate'],i['desc'],sep='====')
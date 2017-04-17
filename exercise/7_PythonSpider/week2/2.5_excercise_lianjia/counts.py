import time
from page_parse import sheet_area,sheet_item

while True:
    # 每隔5秒查询一次数据库中有多少条数据
    # print('url: {}'.format(sheet_area.find().count()))
    print('url: {}'.format(sheet_item.find().count()))

    time.sleep(2)
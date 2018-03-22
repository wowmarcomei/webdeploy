import time
from page_parse import sheet_url

while True:
    # 每隔5秒查询一次数据库中有多少条数据
    print(sheet_url.find().count())
    time.sleep(5)
from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
tongcheng = client['tongcheng']
tongcheng_url_list = tongcheng['tongcheng_url_list']
tongcheng_item_info = tongcheng['tongcheng_item_info']

# 爬虫1
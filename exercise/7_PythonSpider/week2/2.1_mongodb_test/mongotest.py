from pymongo import MongoClient

host = 'localhost'
port = 27017

# 创建一个数据库connection
client = MongoClient(host,port)
# 创建一个数据库,名为Test1
db = client['Test1']
# 给数据库添加一个表,名为sheet
sheet = db['sheet']

for item in sheet.find({'words':{'$lt':5}}):
    print(item)
    # sheet.remove(item)

'''
path = '/Users/meixuhong/workstation/exercise/5_Python/4_parseWebMongodb/walden.txt'
with open(path,'r') as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        data = {
            'index': index,
            'line': line,
            'words': len(line.split())
        }
        sheet.insert_one(data)
'''
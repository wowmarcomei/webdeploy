import pymongo

host = 'localhost'
port = 27017

client = pymongo.MongoClient(host,port)
walden = client['walden'] #创建一个数据库walden
sheet_tab = walden['sheet_tab'] #创建一个数据库表,可以理解为excel的tab页面

path = './walden.txt'

def writeFileIntoMongo():
    with open(path,'r') as f:
        lines = f.readlines()
        '''
        # readlines()函数返回值为一个列表,列表的每个元素为读取的每一行
        # eg:['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n']
        '''
        for index, line in enumerate(lines):
            '''
            #enumerate(list):返回一个枚举列表
            #eg:[(1,'line1\n'),(2,'line2\n'),(3,'line3\n'),(4,'line4\n'),(5,'line5\n')]
            '''
            data = {
                'index': index,
                'line': line,
                'words': len(line.split())
            }
            # print(data)
            sheet_tab.insert_one(data)

def query_mongodb():
    '''
    查询数据库
    :return:
    '''
    for item in sheet_tab.find():
        print(item)

def select_mongodb():
    '''
    筛选出所有words=0的行
    注: $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=。（l表示less g表示greater e表示equal n表示not  ）
    :return:
    '''
    for item in sheet_tab.find({'words':{'$ne':0}}):
        print(item)

select_mongodb()



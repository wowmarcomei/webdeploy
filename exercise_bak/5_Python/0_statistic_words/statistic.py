import re

path = './test.txt'

def statisticWords(path):
    with open(path,'r') as file:
        # 获取文本内容
        content = file.read()
        # 使用正则表达式去掉空格等标点符号
        words = re.split(r"[\s\,\;\:\-\!\?\"\.]+",content)

        # 对获取的文本内容进行去重,使用序列set
        word = set(words)

        # 使用count进行统计,并将其存入字典
        words_dicts = {word: words.count(word) for word in words}

        # 对字典进行排序,根据value进行排序
        newDicts = sorted(words_dicts.items(),key=lambda x:x[1], reverse = True)

        for key, value in newDicts:
            print("{} - {} times".format(key,value))


statisticWords(path)

import re
import os
import sys
import io
import hachoir
from hachoir import core
from hachoir import metadata
from hachoir import parser
from hachoir import stream
from hachoir import subfile


# print(help(hachoir)) #查询模块具有哪些package

path = '/Users/meixuhong/workstation/exercise/python/videosAndImages/'
fileType = ['jpg','png','mov']
fileName = path + 'pic6' + '.' + fileType[0]

def getFileTime(originFile,myList,myChar='Creation date',timePosition=8):
    """定义函数,在列表中查询特定字符串,如果找到则返回

    :param originFile:从原始文件中查找,用于输出异常时的文件名
    :param myList:对该列表进行查询
    :param myChar:查询列表字符
    :param timePosition:重新命名下划线的位置
    :return fileFinalTime:文件创建原始时间
    """
    for i in range(1,len(myList)+1):
        #如果字符串在列表中,则提取数字部分,即为文件创建时间
        if myChar in myList[i-1]:
            fileTime = re.sub(r"\D",'',myList[i-1])    #使用正则表达式将列表中的非数字元素剔除
            a=list(fileTime)                           #将文件创建时间字符串转为列表list
            a.insert(timePosition,'_')                 #将列表插入下划线分割date与time
            fileFinalTime = "".join(a)                 #重新将列表转为字符串

            # print("The time is at: {} of the metadata, and the creation time is {}".format(i,a))
            # print(fileName)

            return fileFinalTime
    print("Unable to get the creation time of {}\n".format(originFile))


def decodeMyFiles(file,filetype='mov'):
    """解析音频或者照片文件,

    :param file: 解析文件
    :param filetype: 文件类型
    :return: 解析文件的创建时间
    """
    parserFile = parser.createParser(file) #解析文件
    if not parserFile:
        print("Unable to parse file!\n")
        exit(1)

    try:
        metadataDecode = metadata.extractMetadata(parserFile)  # 获取文件的metadata
    except ValueError:
        print('Metadata extraction error.')
        metadataDecode = None

    if not metadataDecode:
        print("Unable to extract metadata.")
        exit(1)

    # metadataDecode = metadata.extractMetadata(parserFile) #获取文件的metadata
    myList = metadataDecode.exportPlaintext(line_prefix="") # 将文件的metadata转换为list,且将前缀设置为空
    # print("meta length is:{}, and the meta data is:{}".format(len(myList), myList))
    return getFileTime(file,myList)

# print(decodeMyFiles(fileName,'jpg'))

def renameMyFiles(file,type):
    name = decodeMyFiles(file,type)
    if not name:
        print("Unable to rename {}.******".format(file))
        exit(1)
    try:
        newName = name + '.' + type
        os.rename(file,newName)
        print('OH,YES-------newName is: {}'.format(newName))
    except ValueError:
        print("Unable to rename {}......".format(file))

renameMyFiles(fileName,fileType[0])



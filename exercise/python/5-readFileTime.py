
from PIL import Image
from PIL.ExifTags import TAGS

img = ['pic1.jpg','pic3.jpg']
vid = '1.mov'
def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    print(ret)
    print("***************************")
    print(ret['DateTimeOriginal'])
    return ret

for i in range(0,len(img)):
    get_exif(img[i])



# import shutil
# import os
# import stat
# import time
# # import exif
# from PIL import Image
# from PIL.ExifTags import TAGS
#
# def getDate(filename):
#     try:
#         fd = open(filename, 'rb')
#     except:
#         raise "unopen file[%s]\\n" % filename
#     # data = exif.process_file( fd )
#     data = Image.open(fd)._getexif()
#
#     #     i = Image.open(fn)
#     #     info = i._getexif()
#     #     for tag, value in info.items():
#     #         decoded = TAGS.get(tag, tag)
#     #         ret[decoded] = value
#     #     print(ret)
#     #     print("***************************")
#     #     print(ret['DateTimeOriginal'])
#
#     if data:
#         print(data)
#         # 获取图像的 拍摄日期
#     try:
#         t = data['EXIF DateTimeOriginal']
#         #转换成 yyyy-mm-dd 的格式
#         return str(t).replace(":","-")[:10]
#     except:
#         pass
#     #如果没有取得 exif ，则用图像的创建日期，作为拍摄日期
#     state = os.stat(filename)
#     return time.strftime("%Y-%m-%d", time.localtime(state[-2]))
#
# def showFileProperties(path):
#     '''显示文件的属性。包括路径、大小、创建日期、最后修改时间，最后访问时间'''
#     import time,os
#     #遍历目录下的所有文件
#     for root,dirs,files in os.walk(path,True):
#         dirs[:] = []
#         print("位置：" + root)
#         for filename in files:
#             filename = os.path.join(root, filename)
#             #如果文件名是 'jpg','png' 就处理，否则不处理
#             f,e = os.path.splitext(filename)
#             if e.lower() not in ('.jpg','.png'):
#                 continue
#             info = "文件名: " + filename + " "
#             #文件的拍摄日期
#             t = getDate( filename )
#             info = info + "拍摄时间：" + t + " "
#         pwd = root + t
#         dst = pwd + filename
#         #按照图片的拍摄日期创建目录，把每个图片放到相应的目录中去
#         if not os.path.exists(pwd ):
#             os.mkdir(pwd)
#             print(info, dst)
#             #用 copy2 会保留图片的原始属性
#             shutil.copy2(filename, dst)
#         os.remove(filename)
#
# if __name__ == "__main__":
#     path = "."
#     showFileProperties(path)
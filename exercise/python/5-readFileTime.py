#
# # from PIL import Image, ExifTags
# #
# # im = Image.open('marcomei.jpeg')
# # img = Image.open('20120929185.jpg')
# #
# # # exif = { ExifTags.TAGS[k]: v for k, v in im._getexif().items() if k in ExifTags.TAGS }
# #
# # print(img.exif)
# # # print(exif)
#
# from PIL import Image
# from PIL.ExifTags import TAGS
# import pprint
# import time
# import datetime
# import os
# import sys
# def get_exif(fn):
#     ret = {}
#     i = Image.open(fn)
#     info = i._getexif()
#
#     for tag, value in info.items():
#         decoded = TAGS.get(tag, tag)
#         ret[decoded] = value
#     return ret
#
# def set_modify_time(_filename):
#     exif_info = get_exif(_filename);
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(exif_info)
#     print(exif_info['DateTime'])
#
# #Get EXIF Creation Date
# exif_date,exif_time  = exif_info['DateTime'].split(' ')
# print exif_date,exif_time
# (y,mm,d) = exif_date.split(‘:’)
# (h,min,s) = exif_time.split(‘:’)
# date_list = (y,mm,d,h,min,s)
# print date_list

from PIL import Image
from PIL.ExifTags import TAGS

img = ['pic1.jpg','pic3.jpg']

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
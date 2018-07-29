import requests
import re
import json
from urllib import error

def get_one_page(url):
    headers = {
    'Cookie': 'uuid_n_v=v1; uuid=6266F950913511E8BAE959978C7B0D0473005491BEDE4F03918D808909FBCD63; _csrf=ac998ee17cc0a0a19ead8ae7bad340ccd342180e2588ba8b326ee6d6b4deac25; _lxsdk_cuid=164d92c0d5a25-0e046d8f7973c-16386952-100200-164d92c0d5bc8; _lxsdk=6266F950913511E8BAE959978C7B0D0473005491BEDE4F03918D808909FBCD63; __mta=152329862.1532651901646.1532653173231.1532653961468.14; _lxsdk_s=164d92c0d5c-908-59-aa6%7C%7C56',
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        return response.text
    except error.HTTPError as err:
        print(err.reason, err.code, err.headers, sep='\n')
        return None
    except urllib.error.URLError as err:
        print(err.reason)
        return None

def parse_one_page(html):
    reg = r'<dd>.*?board-index.*?">(.*?)</i>.*?title="(.*?)".*?data-src="(.*?)".*?movie-item-info.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
    results = re.findall(reg,html,re.S)
    # print(results)
    for item in results:
        yield {
            '排名': item[0],
            '电影': item[1],
            '海报链接': item[2],
            # 添加条件判断语句，增加程序的健壮性，只有当item[3]长度大于3时才从第三个开始获取
            '演员': item[3].strip()[3:] if len(item[3])>3 else '',
            # 添加条件判断语句，增加程序的健壮性，只有当item[4]长度大于5时才能获取上映时间
            '上映时间': item[4].strip()[5:15] if len(item[4]) > 5 else '',
            # 通过正则表达式获取括号()里的字符串，且添加条件判断语句只有匹配到了才获取其中的字符串，
            '上映地点': re.findall(r'\((.*?)\)',item[4],re.S)[0] if len(re.findall(r'\((.*?)\)',item[4],re.S))>0 else '',
            # 将原有的字符串变成数字,将评分前半段去掉点号，小数位除以10
            '猫眼评分': int(item[5].strip('.'))+int(item[6])/10
        }

def write_to_json(content):
    #content 参数就是一部电影的提取结果，是一个字典。
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset*10)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)

if __name__ == '__main__':
    for page in range(10):
        main(page)

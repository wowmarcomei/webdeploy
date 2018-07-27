import requests
import re
import json

def get_one_page(url):
    headers = {
    'Cookie': 'uuid_n_v=v1; uuid=6266F950913511E8BAE959978C7B0D0473005491BEDE4F03918D808909FBCD63; _csrf=ac998ee17cc0a0a19ead8ae7bad340ccd342180e2588ba8b326ee6d6b4deac25; _lxsdk_cuid=164d92c0d5a25-0e046d8f7973c-16386952-100200-164d92c0d5bc8; _lxsdk=6266F950913511E8BAE959978C7B0D0473005491BEDE4F03918D808909FBCD63; __mta=152329862.1532651901646.1532653173231.1532653961468.14; _lxsdk_s=164d92c0d5c-908-59-aa6%7C%7C56',
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    reg = r'<dd>.*?board-index.*?">(.*?)</i>.*?data-src="(.*?)".*?movie-item-info.*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?nteger">(.*?)</i>.*?fraction">(.*?)</i>'
    pattern = re.compile(reg,re.S)

    items = re.findall(pattern, html)
    print(items)
    for item in items:
        yield {
            '排名': item[0],
            '图片链接': item[1],
            '标题': item[2].strip(),  #strip()函数会删除空白字符，包括\r,\t,\n,空格
            '演员': item[3].strip()[3:] if len(item[3]) > 3 else '',
            '上映时间': item[4].strip()[5:15] if len(item[4]) > 5 else '',
            '上映地点': item[4].strip()[16:] if len(item[4]) > 16 else '',
            '评分': item[5].strip() + item[6].strip()
        }
def write_to_json(content):
    #content 参数就是一部电影的提取结果，是一个字典。
    # with open('result.txt', 'a') as f:
    #     print(type(json.dumps(content)))
    #     f.write(json.dumps(content, ensure_ascii=False,).encode('utf-8'))
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'http://www.maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    items = parse_one_page(html)
    for item in items:
        print(item)
        write_to_json(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
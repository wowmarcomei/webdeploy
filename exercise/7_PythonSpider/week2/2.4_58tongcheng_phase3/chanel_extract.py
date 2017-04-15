from bs4 import BeautifulSoup
import requests

url_start = 'http://bj.58.com/sale.shtml'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Cookie':'id58=c5/nn1jG1nt7740tOqjDAg==; bj58_id58s="SFkzaFJHS0R5UjNSNDc0Mg=="; als=0; myfeet_tooltip=end; bdshare_firstime=1491265900161; bj58_new_uv=2; final_history=26520838295997%2C29602192246606%2C26088204291258; _ga=GA1.2.1479444230.1491872757; sz=20174117375; 58home=sz; commontopbar_city=4%7C%u6DF1%u5733%7Csz; commonTopbar_myfeet_tooltip=end; city=bj; 58tj_uuid=341a5926-7769-47a6-a2eb-d054038f094c; new_session=0; new_uv=3; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.google.com.mm%252F; f=n'
}

proxies = {'https':'https://35.164.104.8:3128'}

def get_channel_urls(url):
    wb_data = requests.get(url,headers =headers,proxies=proxies)
    soup = BeautifulSoup(wb_data.text,'lxml')

    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        url_list = 'http://bj.58.com'+link.get('href')
        print(url_list)

# get_channel_urls(url_start)

channel_url_list = '''
    http://bj.58.com/shouji/
    http://bj.58.com/tongxunyw/
    http://bj.58.com/danche/
    http://bj.58.com/fzixingche/
    http://bj.58.com/diandongche/
    http://bj.58.com/sanlunche/
    http://bj.58.com/peijianzhuangbei/
    http://bj.58.com/diannao/
    http://bj.58.com/bijiben/
    http://bj.58.com/pbdn/
    http://bj.58.com/diannaopeijian/
    http://bj.58.com/zhoubianshebei/
    http://bj.58.com/shuma/
    http://bj.58.com/shumaxiangji/
    http://bj.58.com/mpsanmpsi/
    http://bj.58.com/youxiji/
    http://bj.58.com/jiadian/
    http://bj.58.com/dianshiji/
    http://bj.58.com/ershoukongtiao/
    http://bj.58.com/xiyiji/
    http://bj.58.com/bingxiang/
    http://bj.58.com/binggui/
    http://bj.58.com/chuang/
    http://bj.58.com/ershoujiaju/
    http://bj.58.com/bangongshebei/
    http://bj.58.com/diannaohaocai/
    http://bj.58.com/bangongjiaju/
    http://bj.58.com/ershoushebei/
    http://bj.58.com/yingyou/
    http://bj.58.com/yingeryongpin/
    http://bj.58.com/muyingweiyang/
    http://bj.58.com/muyingtongchuang/
    http://bj.58.com/yunfuyongpin/
    http://bj.58.com/fushi/
    http://bj.58.com/nanzhuang/
    http://bj.58.com/fsxiemao/
    http://bj.58.com/xiangbao/
    http://bj.58.com/meirong/
    http://bj.58.com/yishu/
    http://bj.58.com/shufahuihua/
    http://bj.58.com/zhubaoshipin/
    http://bj.58.com/yuqi/
    http://bj.58.com/tushu/
    http://bj.58.com/tushubook/
    http://bj.58.com/wenti/
    http://bj.58.com/yundongfushi/
    http://bj.58.com/jianshenqixie/
    http://bj.58.com/huju/
    http://bj.58.com/qiulei/
    http://bj.58.com/yueqi/
    http://bj.58.com/chengren/
    http://bj.58.com/nvyongpin/
    http://bj.58.com/qinglvqingqu/
    http://bj.58.com/qingquneiyi/
    http://bj.58.com/chengren/
    http://bj.58.com/xiaoyuan/
    http://bj.58.com/ershouqiugou/
    http://bj.58.com/tiaozao/
'''
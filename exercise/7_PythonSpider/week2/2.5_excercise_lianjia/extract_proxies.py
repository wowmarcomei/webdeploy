from bs4 import BeautifulSoup
import requests
import time
import re
import random

base_url = 'http://www.us-proxy.org/'

#
#
# UA = random.choice(agent_list)
# headers = {
#     'User-Agent': UA,
#     'Cookie':'__cfduid=d9b84d562c17e7c312f1f92d5a5d9438b1491177799; _ga=GA1.2.1542643058.1491177804; __atuvc=18%7C14%2C4%7C15%2C6%7C16; __atuvs=58f34389a06466b7002'
# }
#
# # iplist = []
#
# def get_ip_list(url=base_url):
#     wb_data = requests.get(url,headers=headers)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#
#     ips = soup.select('tbody > tr > td:nth-of-type(1)')
#     ports = soup.select('tbody > tr > td:nth-of-type(2)')
#     protocols = soup.select('tbody > tr > td:nth-of-type(7)')
#     validities = soup.select('tbody > tr > td:nth-of-type(8)')
#
#     for ip,port,protocol,validity in zip(ips,ports,protocols,validities):
#             data = {
#                 'ip': ip.get_text(),
#                 'port': port.get_text(),
#                 'protocol': 'Https' if protocol.get_text() == 'yes' else 'Http',
#                 'validity': validity.get_text()
#             }
#             iplist.append({'{}'.format(data['protocol']):'{}://{}:{}'.format(data['protocol'],data['ip'],data['port'])})
#             print(data)
#
#     print(iplist)
#     print('共有{}个ip'.format(len(iplist)))
#
#     # 返回前20个IP list
#     return iplist[:20]
#
# get_ip_list()
#
# proxies = random.choice(iplist)
# print(proxies)

class Proxies:
    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

        self.ip_list = []
        self.ip_temp = []

        UA = random.choice(self.user_agent_list)
        self.headers = {
            'User-Agent': UA,
        }

        wb_data = requests.get(base_url, headers=self.headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')

        ips = soup.select('tbody > tr > td:nth-of-type(1)')
        ports = soup.select('tbody > tr > td:nth-of-type(2)')
        protocols = soup.select('tbody > tr > td:nth-of-type(7)')
        validities = soup.select('tbody > tr > td:nth-of-type(8)')

        for ip, port, protocol, validity in zip(ips, ports, protocols, validities):
            data = {
                'ip': ip.get_text(),
                'port': port.get_text(),
                'protocol': 'Https' if protocol.get_text() == 'yes' else 'Http',
                'validity': validity.get_text()
            }
            self.ip_temp.append(
                {'{}'.format(data['protocol']): '{}://{}:{}'.format(data['protocol'], data['ip'], data['port'])})
            print(data)

        print('共有{}个ip'.format(len(self.ip_temp)))

        # 获取前20个IP list
        self.ip_list = self.ip_temp[:20]

test = Proxies()
print(test.ip_list)



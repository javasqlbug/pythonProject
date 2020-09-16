# -*- coding: UTF-8 -*-
#参考自http://c.biancheng.net/view/2011.html
import requests        #导入requests包
from bs4 import    BeautifulSoup
import re
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

secret = "city-82e3843ce5024d5706dd18b18a9d9d984268ef95"

user = "public-rand"

socks5 = "socks5h://{user}:{secret}@{ip}:65221".\
 format(user=user, secret=secret, ip="socks.gongxiangyun.qihoo.net")

proxies = {
    'http': socks5,
    'https': socks5
}

file_name = './xingzhengquhua.txt'
url='https://xingzhengquhua.51240.com/120100000000__xingzhengquhua/'
#strhtml=requests.get(url)
strhtml=requests.get(url, proxies=proxies, timeout=10)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main_content > table > tr > td > table > tr')
print(data)

for item in data[3:]:
    result={
        'title': re.findall('\D+', item.get_text()),
        'ID': re.findall('\d+', item.get_text())
    }
    print(result)
    with open(file_name, 'a') as file_obj:
        #file_obj.write(str(result.get('ID')) + ',' + str(result.get('title')) + '\n')
        #file_obj.write(",".join(result) + '\n')
        file_obj.write(str(result['ID'][0]) + ',' + str(result['title'][0]) + ',,4' + '\n')

        #file_obj.write('\r\n')

    url = 'https://xingzhengquhua.51240.com/' + str(re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
    print(url)
    time.sleep(0.1)
    #strhtml = requests.get(url)
    strhtml = requests.get(url, proxies=proxies, timeout=10)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#main_content > table > tr > td > table > tr')
    print(data[3:])

    for item in data[3:]:
        result = {
            'title': re.findall('\D+', item.get_text()),
            'ID': re.findall('\d+', item.get_text())
        }
        print(result)
        with open(file_name, 'a') as file_obj:
            file_obj.write(str(result['ID'][0]) + ',' + str(result['title'][0]) + ',,5' + '\n')

        # 区级
        url = 'https://xingzhengquhua.51240.com/' + str(re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
        print(url)
        time.sleep(0.1)
        #strhtml = requests.get(url)
        strhtml = requests.get(url, proxies=proxies, timeout=10)
        soup = BeautifulSoup(strhtml.text, 'lxml')
        data = soup.select('#main_content > table > tr > td > table > tr')
        print(data[3:])

        for item in data[3:]:
            result = {
                'title': re.findall('\D+', item.get_text()),
                'ID': str(re.findall('\d+', item.get_text()))[2:14],
                'type': str(re.findall('\d+', item.get_text()))[14:17]
            }
            print(result)
            with open(file_name, 'a') as file_obj:
                file_obj.write(result['ID'] + ',' + str(result['title'][0]) + ',' + result['type'] + ',6' + '\n')

print('程序执行结束')
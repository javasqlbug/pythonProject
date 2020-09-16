#参考自http://c.biancheng.net/view/2011.html
import requests        #导入requests包
from bs4 import    BeautifulSoup
import re
import time

url='https://xingzhengquhua.51240.com/'
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main_content > table > tr > td > table > tr')
print(data)

for item in data[2:-1]:
    time.sleep(3)
    result={
        'title': re.findall('\D+', item.get_text()),
        'ID': re.findall('\d+', item.get_text())
    }
    print(result)

    # 市级
    url = 'https://xingzhengquhua.51240.com/' + str(re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
    print(url)
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#main_content > table > tr > td > table > tr')
    print(data[3:])

    for item in data[3:]:
        result = {
            'title': re.findall('\D+', item.get_text()),
            'ID': re.findall('\d+', item.get_text())
        }
        print(result)

        # 区级
        url = 'https://xingzhengquhua.51240.com/' + str(re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
        print(url)
        strhtml = requests.get(url)
        soup = BeautifulSoup(strhtml.text, 'lxml')
        data = soup.select('#main_content > table > tr > td > table > tr')
        print(data[3:])

        for item in data[3:]:
            result = {
                'title': re.findall('\D+', item.get_text()),
                'ID': re.findall('\d+', item.get_text())
            }
            print(result)

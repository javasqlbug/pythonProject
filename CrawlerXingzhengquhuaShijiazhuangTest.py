#参考自http://c.biancheng.net/view/2011.html
import requests        #导入requests包
from bs4 import    BeautifulSoup
import re
import time

url='https://xingzhengquhua.51240.com/130101000000__xingzhengquhua/'
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main_content > table > tr > td > table > tr')
print(data)

for item in data[3:]:
    time.sleep(0.1)
    result={
        'title': re.findall('\D+', item.get_text()),
        'ID': re.findall('\d+', item.get_text())
    }
    print(result)

    for item in data[3:]:
        time.sleep(0.1)
        result = {
            'title': re.findall('\D+', item.get_text()),
            'ID': re.findall('\d+', item.get_text())
        }
        print(result)

print('程序执行结束')
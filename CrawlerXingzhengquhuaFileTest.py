#!/usr/bin/python
# -*- coding: UTF-8 -*-
#参考自http://c.biancheng.net/view/2011.html
import requests        #导入requests包
from bs4 import    BeautifulSoup
import re
import time

file_name = 'D:\\test\\xingzhengquhua\\xingzhengquhua.txt'
url='https://xingzhengquhua.51240.com/'
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main_content > table > tr > td > table > tr')
print(data)

for item in data[2:-1]:
    time.sleep(0.1)
    result={
        'title': re.findall('\D+', item.get_text()),
        'ID': re.findall('\d+', item.get_text())
    }
    print(result)
    with open(file_name, 'a') as file_obj:
        #file_obj.write(str(result.get('ID')) + ',' + str(result.get('title')) + '\n')
        #file_obj.write(",".join(result) + '\n')
        file_obj.write(str(result['ID'][0]) + ',' + str(result['title'][0]) + ',,1' + '\n')

        #file_obj.write('\r\n')

    # 市级
    url = 'https://xingzhengquhua.51240.com/' + str(re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
    print(url)
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#main_content > table > tr > td > table > tr')
    print(data[3:])

    for item in data[3:]:
        time.sleep(0.1)
        result = {
            'title': re.findall('\D+', item.get_text()),
            'ID': re.findall('\d+', item.get_text())
        }
        print(result)
        with open(file_name, 'a') as file_obj:
            file_obj.write(str(result['ID'][0]) + ',' + str(result['title'][0]) + ',,2' + '\n')

        # 区级
        url = 'https://xingzhengquhua.51240.com/' + str(re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
        print(url)
        strhtml = requests.get(url)
        soup = BeautifulSoup(strhtml.text, 'lxml')
        data = soup.select('#main_content > table > tr > td > table > tr')
        print(data[3:])

        for item in data[3:]:
            time.sleep(0.1)
            result = {
                'title': re.findall('\D+', item.get_text()),
                'ID': re.findall('\d+', item.get_text())
            }
            print(result)
            with open(file_name, 'a') as file_obj:
                file_obj.write(str(result['ID'][0]) + ',' + str(result['title'][0]) + ',,3' + '\n')

            # 街道级
            url = 'https://xingzhengquhua.51240.com/' + str(re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
            print(url)
            strhtml = requests.get(url)
            soup = BeautifulSoup(strhtml.text, 'lxml')
            data = soup.select('#main_content > table > tr > td > table > tr')
            print(data[3:])

            for item in data[3:]:
                time.sleep(0.1)
                result = {
                    'title': re.findall('\D+', item.get_text()),
                    'ID': re.findall('\d+', item.get_text())
                }
                print(result)
                with open(file_name, 'a') as file_obj:
                    file_obj.write(str(result['ID'][0]) + ',' + str(result['title'][0]) + ',,4' + '\n')

                # 居委会级
                url = 'https://xingzhengquhua.51240.com/' + str(
                    re.findall('\d+', item.get_text())[0]) + '__xingzhengquhua/'
                print(url)
                strhtml = requests.get(url)
                soup = BeautifulSoup(strhtml.text, 'lxml')
                data = soup.select('#main_content > table > tr > td > table > tr')
                print(data[3:])

                for item in data[3:]:
                    time.sleep(0.1)
                    result = {
                        'title': re.findall('\D+', item.get_text()),
                        'ID': str(re.findall('\d+', item.get_text()))[2:14],
                        'type': str(re.findall('\d+', item.get_text()))[14:17]
                    }
                    print(result)
                    with open(file_name, 'a') as file_obj:
                        file_obj.write(result['ID'] + ',' + str(result['title'][0]) + ',' + result['type'] + ',5' + '\n')


print('程序执行结束')
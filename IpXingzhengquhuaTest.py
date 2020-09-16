# -*- coding: utf-8 -*-

import requests
import time

secret = "city-82e3843ce5024d5706dd18b18a9d9d984268ef95"

user = "public-rand"

socks5 = "socks5h://{user}:{secret}@{ip}:65221".\
 format(user=user, secret=secret, ip="socks.gongxiangyun.qihoo.net")

proxies = {
    'http': socks5,
    'https': socks5
}

r = requests.get("https://xingzhengquhua.51240.com/", proxies=proxies, timeout=10)

for line in r.iter_lines(decode_unicode=True):
    if line:
        print(line)

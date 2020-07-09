from bs4 import BeautifulSoup as bs
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
import time
import random

proxy_ips = ['51.15.227.220:3128', '81.162.56.154:8081', '221.180.170.104:8080'] # 代理伺服器查詢: http://cn-proxy.com/
ip = random.choice(proxy_ips)
headerList = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
              "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"]
userAgent = random.choice(headerList)
header = {'User-Agent':userAgent}

for idx in (1, 2):
    url = f'https://food.optfantasy.com/explore/%E5%8F%B0%E5%8C%97%E5%B8%82/list?page={idx}'
    r = requests.get(url, verify=False, headers=header, proxies={'http': 'http://' + ip})
    time.sleep(random.randint(1, 10))
    if r.status_code != 200:
       raise Exception("Error")
    soup = bs(r.content, 'lxml')

    for item in soup.find_all("div", "restaurant-info"):
        title = item.find('div', 'title').a.get_text()
        star = item.find('div', 'text').get_text()
        address = item.find('div', 'address-row').get_text()
        link = item.find('a')
        pic = item.find('img')
        category = item.find('div', 'category-row').get_text()
        if (item.find('div', 'avg-price')):
            price = item.find('div', 'avg-price').get_text()
        else:
            price = "未知"

        print('店名：', title,
              '\n评分：', star,
              '\n地址：', address,
              '\n均消：', price.replace("· 均消 ", ""),
              '\n分类:',category.replace("附近餐廳", ""),
              '\n链接：','https://food.optfantasy.com/'+link['href'],
              '\n图片链接：', pic['src'])
        print('\n')
# coding:utf-8
from urllib import request
import requests
import json

from bs4 import BeautifulSoup


def mkdir(path):
    import os
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False


page = request.urlopen('https://tech.meituan.com/archives')

htmlcode = page.read().decode("utf-8")
soup = BeautifulSoup(htmlcode, 'lxml')
articles = soup.select('.post-title')
list = []
for article in articles:
    atag = article.find_all('a')[0]
    atag['href'] = 'https://tech.meituan.com' + atag['href']
    list.append(atag)

head = '<!DOCTYPE html><html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>Title</title></head><body>'
body = ''
for atag in list:
    body += str(atag) + '<br>'
foot = '</body></html>'

html = head + body + foot

file_path = 'd:\\meituan'
mkdir(file_path)


def write(html, file):
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    params = {
        "content": html
    }
    response = requests.post('http://127.0.0.1:9200/meituan/blog', headers=headers, data=json.dumps(params))
    print(response.content)
    # f = open(file, "w", encoding='utf8')
    # f.write(html)
    # f.close()


write(html, file_path + '\meituan.html')


def write_content(url):
    page = request.urlopen(url)
    html = page.read().decode("utf-8")
    url = url.replace("https://tech.meituan.com/", "").replace("/", "_")
    write(html, file_path + '\\' + url)


# write_content('https://tech.meituan.com/fe_security_csrf.html')

for atag in list:
    write_content(str(atag['href']))

#coding:utf-8
from urllib import request
from bs4 import BeautifulSoup

page = request.urlopen('https://tech.meituan.com/archives')

htmlcode = page.read().decode("utf-8")
soup = BeautifulSoup(htmlcode,'lxml')
articles = soup.findAll('article')
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
f = open("d:\\meituan.html", "w",encoding= 'utf8')
f.write(html)
f.close()




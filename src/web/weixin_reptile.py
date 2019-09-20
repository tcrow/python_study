# # coding:utf-8
import http.cookiejar
import requests
import re
from urllib import request
import json

from bs4 import BeautifulSoup

cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
handler = request.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = request.build_opener(handler)  # 通过handler来构建opener
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Host': 'mp.weixin.qq.com',
    'Connection': 'keep-alive',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': ' 1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Cookie': '',
}
url = ''
r = request.Request(url=url, headers=headers, method="GET")
response = opener.open(r)

htmlcode = response.read().decode()
soup = BeautifulSoup(htmlcode, 'lxml')
# soup = BeautifulSoup(htmlcode, "html.parser")

pattern = re.compile(r"wx.cgiData.mass_data'(.*?)';$", re.MULTILINE | re.DOTALL)

scripts = soup.find_all("script")

for script in scripts:
    if 'wx.cgiData.mass_data' in script.text:
        text = script.text.replace(' ', '')
        text = text[text.index('wx.cgiData.mass_data=')+21:]
        text = text[:text.index('\n') - 1]
        j = json.loads(text)
        # print(text.index('wx.cgiData.mass_data='))
        # print(text.index('wx.cgiData.mass_data='))
        for send in j["sent_list"]:
            title = send['appmsg_info'][0]['title']
            content_url = send['appmsg_info'][0]['content_url']
            page = request.urlopen(content_url)
            content = page.read().decode("utf-8")
            headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
            params = {
                "name": 'shufang ' + title,
                "content": content
            }
            response = requests.post('http://10.0.0.39:9200/meituan/blog', headers=headers, data=json.dumps(params))
            print(response.content)


# print(htmlcode)
# print(soup.text)
# print(scripts)

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")

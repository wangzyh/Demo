import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return ""

url = 'http://search.dangdang.com/?key=python&act=input'
html = getHTMLText(url)


pic_url = re.findall("img data-original='(.*?)' src",html)
pic_url2 = re.findall("<img src='(.*?)' alt",html)
pic_url.extend(pic_url2)

i = 1
for ur in pic_url:
    try:
        pics = requests.get(ur)
    except:
        continue

    fp = open('D:\\Demo\\picture\\' + str(i) + '.jpg', 'wb')  #输入存放图片路径
    fp.write(pics.content) #将图片内容写进目录文件中
    fp.close()
    i = i + 1
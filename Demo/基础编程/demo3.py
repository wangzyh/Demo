# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urlencode

'''
data = {
        'offset': 0,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
}
url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
#print(url)
reponse = requests.get(url)
html = reponse.text
data = json.loads(html)
if data and 'data' in data.keys():
    for item in data.get('data'):
        yield item.get('article_url')
'''

# 正则表达式
'''
import os
import re
f = os.popen('tasklist /nh', 'r')
for eachLine in f:
    print(re.findall(r'(.*?)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)', eachLine.rstrip()))  # ([\w.]+(?: [\w.]+)*)
f.close()
'''
# 用于正则表达式练习的数据生成器
# ! /usr/bin/env python3

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(maxsize)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))

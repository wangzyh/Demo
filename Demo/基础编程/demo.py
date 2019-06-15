'''
def yanghui():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]

n = 0
for t in yanghui():
    print(t)
    n = n + 1
    if n == 9:
        break

from functools import reduce
def f(x,y):
    return(x*10+y)
print(reduce(f,([1,2,3,4,5])))
'''
'''
import math
def quadratic(a,b,c):
    A = b*b-4*a*c
    if A>0:
        x1 = (-b+math.sqrt(A))/(2*a)
        x2 = (-b-math.sqrt(A))/(2*a)
        return (x1,x2)
    elif A==0:
        x = -b/(2*a)
        return x
    else:
        return ('none')


r = quadratic(2,4,2)
print(r)

import requests
data = {'name':'Monkey',
'age':12}
r = requests.get("http://httpbin.org/get",params=data)
print(r.text)
#保存一张图片
import requests
r = requests.get('http://images.ioliu.cn/bing/RioGrandeCottonwood_PT-BR10685052962_1920x1080.jpg')
print(r.status_code)
with open('D:/GrandeRiver.jpg','wb') as f:
    f.write(r.content)
    f.close()
#将一张图片POST给一个网站
import requests
files = {'file':open('D:/GrandeRiver.jpg','rb')}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)

#维持会话
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

#证书验证
import requests
#消除警告
from requests.packages import urllib3
urllib3.disable_warnings()
r = requests.get('https://www.12306.cn',verify=False)
print(r.status_code)
'''
#import re

#content = "Hello 1234567 World_This is a Regex Demo"
#result = re.match('Hello.*Demo$',content)
#result = re.match('^Hello\s(\d+)\s(\d+)\sWorld.*Demo$',content)
#result = re.match('He.*(\d+).*Demo$',content)
#result = re.match('He.*?(\d+).*Demo$',content)
#content = '''Hello 1234567 World_This
#is a Regex Demo'''
#result = re.match('He.*?(\d+).*?Demo$',content,re.S)
'''
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo',content)

print(result)
print(result.group(1))
print(result.span())
'''
import requests
import re

results = requests.get('https://book.douban.com/').text

result = re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>',results,re.S)
print(result)

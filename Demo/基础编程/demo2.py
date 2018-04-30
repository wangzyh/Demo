import requests
import re

results = requests.get('https://book.douban.com/').text

result = re.findall('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',results,re.S)
#print(result)
for i in result:
  url,name,author,date = i
  author = re.sub('\s','',author)
  date = re.sub('\s','',date)
  print(url,name,author,date)


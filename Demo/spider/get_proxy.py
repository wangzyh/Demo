import requests
from lxml import etree

url = "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_53028746831a489299c9bf83dad156cd"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
dlurl = [
    'https://www.xicidaili.com/wt/',  # 国内http
    'https://www.xicidaili.com/wn/',  # 国内https
    'https://www.xicidaili.com/nt/',  # 国内普通
    'https://www.xicidaili.com/nn/'  # 国内高匿
]


# 获取西刺代,理IP页面数据
def gethtml(url):
    porxy = []
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    ehtml = etree.HTML(r.text)
    ip = ehtml.xpath('//*[@class="odd"]/td[2]/text()')
    port = ehtml.xpath('//*[@class="odd"]/td[3]/text()')
    j = 0
    for i in ip:
        porxy.append(i + ':' + port[j])
        j += 1
    ip = ehtml.xpath('//*[@class=""]/td[2]/text()')
    port = ehtml.xpath('//*[@class=""]/td[3]/text()')
    j = 0
    for i in ip:
        porxy.append(i + ':' + port[j])
        j += 1
    return porxy


# 检查代,理是否可用
def chkproxy(ipport, timeout):
    proxies = {"http": "http://" + ipport}
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            print(proxies)
            return True
    except OSError:
        pass


def exec(url, pagenum, timeout):
    f = open('.\\ProxyIP.txt', mode='w+')
    for i in range(1, pagenum + 1):
        print('开始获取第' + str(i) + '页代,理IP数据...')
        porxy = gethtml(url + str(i))
        j = 0
        print('开始检查第' + str(i) + '页代,理IP...')
        for i in porxy:
            if chkproxy(i, timeout) == True:
                f.write(i + '\n')
            j += 1
    print('over')


if __name__ == '__main__':
    exec(dlurl[0], 3, 0.3)

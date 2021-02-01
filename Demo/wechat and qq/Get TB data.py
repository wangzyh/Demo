import os
import time
import logging
import requests
import re
from selenium import webdriver
from queue import Queue
import win32gui
import win32con
import win32clipboard as w
import urllib3
from selenium.webdriver.chrome.options import Options

from qq_post import QQSendMessage

url_kumaoke_all_data = 'http://www.kumaoke.com/tao/index.php?r=p&type=2&cid=2&u=696035'
url_kumaoke_two_data = 'http://www.kumaoke.com/tao/index.php?r=p&type=1&cid=2&u=696035'

logging.basicConfig(level=logging.DEBUG)
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(r'../chromedriver.exe', chrome_options=chrome_options)
logging.getLogger("requests").setLevel(logging.WARNING)

class Post_data:
    def __init__(self, name, urls):
        self.urls = urls
        self.name = name
        self.saved = []
        self.q = []
        self.data_file = 'TB_data.txt'
        self.data_path = os.path.join(os.getcwd(), self.data_file)
        self.all_data = []
        self.qq = QQSendMessage()

        # if not os.path.exists(data_path):
        #     os.remove(data_path)

    def save_data_and_post_msg(self):
        d = self.q[0]
        if d not in self.all_data and d:
            logging.info(d)
            self.send_message(d)
            self.q.pop(0)
            self.all_data.append(d)
            with open(self.data_path, 'w') as f:
                f.write(d)

    def post_message(self, data):
        # qq.setImage(data[1] if 'http' in data[1] else 'http:' + data[1])
        time.sleep(1)
        self.qq.setText(data)
        time.sleep(1)
        self.qq.searchByUser(self.name)
        time.sleep(1)
        self.qq.sendByUser(self.name)

    def get_url_data(self, url):
        """
        :param url:
        :return:
        """
        text = requests.get(url).text
        urls = re.findall(r'<a href="/tao/index.php\?r=(.*?)nav_wrap=p&(.*?)"', text)
        images = re.findall(r'<Image class="Image" src="(.*?)" ', text)
        for i in range(len(images)):
            logging.info(f'正在抓取第{i}个页面信息')
            url = f'http://www.kumaoke.com/tao/index.php?r={urls[i][0]}nav_wrap=p&{urls[i][1]}'
            driver.get(url)
            driver.find_element_by_class_name('share').click()
            time.sleep(5)
            try:
                driver.find_element_by_xpath('//*[@id="layui-layer2"]/div/div/div[1]/a[2]').click()
            except Exception as e:
                logging.error(str(e))
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="layui-layer2"]/div/div/div[1]/a[2]').click()
            time.sleep(2)
            data = driver.find_element_by_xpath('//*[@id="codeText"]').text
            if not data:
                continue
            self.q.append(data)
            self.save_data_and_post_msg()

    def send_message(self, msg):
        # 窗口名字，就是备注名
        name = self.name
        # 将测试消息复制到剪切板中
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
        w.CloseClipboard()
        # 获取窗口句柄
        handle = win32gui.FindWindow(None, name)
        # 填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        # 回车发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    def run(self):

        for url in self.urls:
            logging.info(f'开始爬取{url}数据')
            self.get_url_data(url)


if __name__ == '__main__':
    p = Post_data(name='1test', urls=[url_kumaoke_all_data, url_kumaoke_two_data])
    p.run()

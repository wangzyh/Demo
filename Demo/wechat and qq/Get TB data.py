import os
import time
import logging
import requests
import re
from selenium import webdriver
from multiprocessing import Process, Queue

from qq_post import QQSendMessage

url_kumaoke_all_data = 'http://www.kumaoke.com/tao/index.php?r=p&type=2&cid=2&u=696035'
url_kumaoke_two_data = 'http://www.kumaoke.com/tao/index.php?r=p&type=1&cid=2&u=696035'

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Chrome(r'../chromedriver.exe')


class Post_data:
    def __init__(self, name, urls):
        self.urls = urls
        self.name = name
        self.saved = []
        self.q = Queue(maxsize=0)
        self.data_file = 'TB_data.txt'
        self.data_path = os.path.join(os.getcwd(), self.data_file)
        self.all_data = []
        self.qq = QQSendMessage()

        # if not os.path.exists(data_path):
        #     os.remove(data_path)

    def save_data_and_post_msg(self):
        while True:
            d = self.q.get()
            if d not in self.all_data:
                logging.info(d)
                self.post_message(d)
                self.all_data.append(d)
                with open(self.data_path) as f:
                    f.write(d)

    def post_message(self, data):
        self.qq.searchByUser(self.name)
        # qq.setImage(data[1] if 'http' in data[1] else 'http:' + data[1])
        self.qq.sendByUser(self.name)
        time.sleep(0.5)
        self.qq.setText(data)
        self.qq.searchByUser(self.name)
        self.qq.sendByUser(self.name)

    def get_url_data(self, url):
        """
        :param url:
        :return:
        """
        text = requests.get(url).text
        urls = re.findall(r'<a href="/tao/index.php\?r=(.*?)nav_wrap=p&(.*?)"', text)
        images = re.findall(r'<img class="img" src="(.*?)" ', text)
        for i in range(len(images)):
            logging.info(f'正在抓取第{i}个页面信息')
            url = f'http://www.kumaoke.com/tao/index.php?r={urls[i][0]}nav_wrap=p&{urls[i][1]}'
            driver.get(url)
            driver.find_element_by_class_name('share').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="layui-layer2"]/div/div/div[1]/a[2]').click()
            data = driver.find_element_by_xpath('//*[@id="codeText"]').text
            self.q.put(data)

    def run(self):
        p1 = Process(target=self.save_data_and_post_msg, args=())
        p1.start()

        for url in self.urls:
            logging.info(f'开始爬取{url}数据')
            self.get_url_data(url)


if __name__ == '__main__':
    p = Post_data(name='1test', urls=[url_kumaoke_all_data, url_kumaoke_two_data])
    p.run()

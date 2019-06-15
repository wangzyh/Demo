import json
import re
import os
from hashlib import md5
import pymongo
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests.exceptions import RequestException
from config import *
from multiprocessing import Pool

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def get_page_index(offset, keyword):
    data = {'offset': offset, 'format': 'json', 'keyword': keyword, 'autoload': 'true', 'count': '20', 'cur_tab': 3}
    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("Request failed")
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("Request detail page failed", url)
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    images_pattern = re.compile('gallery: (.*?),\s', re.S)
    result = re.search(images_pattern, html)
    if result:
        # print(result.group(1))
        data = json.loads(result.group(1))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images: download_image(image)
            return {"title": title, "url": url, "images": images}


def write_to_file(result):
    with open('jiepai.txt', 'a', encoding='utf-8') as f:
        f.write(result)
        f.close()


def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('save to MongoDB successful', result)
        return True
    return False


def download_image(url):
    print("正在下载:", url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print("Request image failed", url)
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):
        # print(url)

        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            if result: save_to_mongo(result)
            # save_to_mongo(result)
            # write_to_file(str(result))


if __name__ == "__main__":
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
    pool = Pool()
    pool.map(main, groups)

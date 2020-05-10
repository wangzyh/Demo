import os
import time
import requests
from selenium import webdriver

jd_url = 'https://www.jd.com/'


class JD_pict:
    def __init__(self, key):
        self.key = key
        # set proxy
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--proxy-server=http://219.159.38.199:56210")
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)

    def search(self):
        self.driver.get(jd_url)
        time.sleep(1)

        self.driver.maximize_window()
        time.sleep(1)

        self.driver.find_element_by_tag_name('input').send_keys(key)
        time.sleep(1)

        self.driver.find_element_by_class_name('form').find_element_by_tag_name('button').click()
        time.sleep(5)

        # Sliding and turning pages
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        time.sleep(0.2)

        # get page number
        page_number = self.driver.find_element_by_class_name('p-skip').find_element_by_tag_name('b').text

        for index in range(int(page_number)):
            for i in range(10):
                # Sliding and turning pages
                js = f"var q=document.documentElement.scrollTop={i * 800}"
                self.driver.execute_script(js)
                time.sleep(0.2)

            # Get title and image
            ul = self.driver.find_element_by_id('J_goodsList')
            elements = ul.find_elements_by_tag_name('li')
            for element in elements:
                element.find_element_by_class_name('p-img').click()
                time.sleep(1)
                self.get_image_and_title()

            # next page
            self.driver.find_element_by_class_name('pn-next').click()

    def get_image_and_title(self):
        first_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != first_handle:
                self.driver.switch_to_window(handle)
                time.sleep(1)

        img = self.driver.find_element_by_id('spec-n1').find_elements_by_tag_name('img')

        title = img[0].parent.title
        img_url = img[0].get_attribute('src')
        time.sleep(1)

        self.save_file(title, img_url)
        time.sleep(1)

        # close web
        self.driver.close()
        self.driver.switch_to_window(first_handle)

    def save_file(self, title, img_url):
        if not os.path.exists(f'D:\\Demo\\picture\\{self.key}'):
            os.mkdir(f'D:\\Demo\\picture\\{self.key}')
        data = requests.get(img_url)
        title = title.replace('【摘要 书评 试读】- 京东图书', '')
        path = os.path.join(f'D:\\Demo\\picture\\{self.key}\\', str(title)+'.jpg')
        try:
            with open(path, 'wb') as f:
                f.write(data.content)
        except Exception as e:
            print(e)
            pass

    def logout(self, driver):
        driver.quit()


if __name__ == '__main__':
    key = 'R语言'
    jd = JD_pict(key)
    jd.search()

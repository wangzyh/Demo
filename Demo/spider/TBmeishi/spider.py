from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def search():
    browser.get('https://www.taobao.com')
    # 输入框，EC是选择条件
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")))
    # 在输入框中输入
    input.send_keys('美食')
    submit.click()
    # 按钮
    xiaoliang = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_relative > div.sort-row > div > ul > '                                                             'li:nth-child(3) > a')))
    # 点击按钮
    xiaoliang.click()


def main():
    search()


if __name__ == '__main__':
    main()

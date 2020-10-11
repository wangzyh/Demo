# encoding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()


driver.maximize_window()
driver.get('https://www.qichacha.com/user_login')
time.sleep(2)
while True:
    try:
        normal = driver.find_element_by_id('normalLogin')
        normal.click()
        time.sleep(2)

        # # get name and passwd
        # driver.find_element_by_id('nameNormal').send_keys('15601861028')
        # time.sleep(2)
        # driver.find_element_by_id('pwdNormal').send_keys('wzy114906')

        source = driver.find_element_by_id('nc_1_n1z')
        lang = driver.find_element_by_class_name('nc-lang-cnt')
        lens = lang.size['width']
        ac = ActionChains(driver)

        ac.click_and_hold(source)
        while lens > 0:
            l = lens/5
            ac.move_by_offset(l, 0).perform()
            lens -= l
            # time.sleep(0.1)
        time.sleep(0.3)
        ac.release()
        text = driver.find_element_by_id('nc_2__scale_text').text
        # 目前只碰到3种情况：成功（请在在下方输入验证码,请点击图）；无响应（请按住滑块拖动)；失败（哎呀，失败了，请刷新）
        if text.text.startswith(u'验证通过'):
            print('成功滑动')

            # login
            driver.find_element_by_class_name('login-btn').click()
            time.sleep(2)
        if text.text.startswith(u'请点击'):
            print('成功滑动')
            break
        if text.text.startswith(u'请按住'):
            continue

    except Exception as e:
        # 这里定位失败后的刷新按钮，重新加载滑块模块
        driver.refresh()
        time.sleep(5)
        print(e)
    # 退出浏览器，如果浏览器打开多个窗口，可以使用driver.close()关闭当前窗口而不是关闭浏览器
driver.quit()

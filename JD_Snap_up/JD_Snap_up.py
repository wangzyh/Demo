import os
import random
import time
import cv2
import shutil
import numpy as np

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located as loads
from selenium.webdriver.support.ui import WebDriverWait

jd_url = 'https://www.jd.com/'
login_url = 'https://passport.jd.com/new/login.aspx'


class JD:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.driver = webdriver.Chrome('bin/chromedriver.exe')
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(jd_url)
        self.cwd = os.getcwd()
        self.temp = os.path.join(self.cwd, 'temp')
        if os.path.exists(self.temp):
            shutil.rmtree(self.temp)
        os.mkdir(self.temp)

    def login(self):
        self.driver.get(login_url)
        time.sleep(1)

        # region login page
        account_login = WebDriverWait(self.driver, 10).until(
            loads((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]')))
        account_login.click()
        time.sleep(1)

        user = WebDriverWait(self.driver, 10).until(
            loads((By.XPATH, '//*[@id="loginname"]'))
        )
        user.send_keys(self.user)
        time.sleep(1)

        passwd = WebDriverWait(self.driver, 10).until(
            loads((By.XPATH, '//*[@id="nloginpwd"]'))
        )
        passwd.send_keys(self.passwd)
        time.sleep(1)

        login_btn = WebDriverWait(self.driver, 10).until(
            loads((By.XPATH, '//*[@id="loginsubmit"]'))
        )
        login_btn.click()
        # endregion

        time.sleep(3)
        try:
            self.driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
        except NoSuchElementException:
            jd_id = WebDriverWait(self.driver, 10).until(
                loads((By.XPATH, '//*[@id="ttbar-login"]/div[1]/a'))
            )
            if jd_id.text != '你好，请登录':
                return True
            return False

        # region swipe verification code
        complete_image = WebDriverWait(self.driver, 10).until(
            loads((By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img'))
        )
        with open(os.path.join(self.temp, '1.png'), 'wb') as f:
            f.write(complete_image.screenshot_as_png)
        move_image = WebDriverWait(self.driver, 10).until(
            loads((By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img'))
        )
        with open(os.path.join(self.temp, '2.png'), 'wb') as f:
            f.write(move_image.screenshot_as_png)

        time.sleep(2)
        move_amount = self.swipe_verification_code()
        # endregion

        # move slider
        self.move_slider(move_amount)

    def swipe_verification_code(self):
        t1 = os.path.join(self.temp, '1.png')
        t2 = os.path.join(self.temp, '2.png')
        t3 = os.path.join(self.temp, '3.png')
        t4 = os.path.join(self.temp, '4.png')
        # region load and save gray image
        img1 = cv2.imread(t1, 0)
        cv2.imwrite(t3, img1)

        img2 = cv2.imread(t2, 0)
        cv2.imwrite(t4, img2)
        # endregion

        # match
        img3 = cv2.imread(t3)
        img4 = cv2.imread(t4)

        img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
        img3 = abs(255 - img3)
        cv2.imwrite(t3, img3)

        img3 = cv2.imread(t3)
        result = cv2.matchTemplate(img3, img4, cv2.TM_CCOEFF_NORMED)
        x, y = np.unravel_index(result.argmax(), result.shape)
        return y

    def move_slider(self, move):
        slider = WebDriverWait(self.driver, 10).until(
            loads((By.XPATH, '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]'))
        )
        webdriver.ActionChains(self.driver).click_and_hold(slider).perform()
        for item in self.get_steps(move):
            webdriver.ActionChains(self.driver).move_by_offset(xoffset=item, yoffset=0).perform()
        time.sleep(0.5)
        webdriver.ActionChains(self.driver).release(slider).perform()

    @staticmethod
    def get_steps(move):
        steps = []
        # region speeded up
        # definition: initial speed - v, run time - t, current distance - current
        v = 0
        t = random.randint(2, 3) * 0.1
        current = 0
        # Reach the mid value and start to decelerate
        mid = round(move * random.uniform(5 / 7, 5 / 8))

        while current < move:
            if current < mid:
                a = random.randint(1, 3)
            else:
                a = -random.randint(2, 4)
            v0 = v

            s = v0 * t + 0.5 * a * (t ** 2)
            current += s
            steps.append(round(s))
            v = v0 + a * t
        lee = random.randint(0, 2)
        for i in range(lee):
            steps.append(i*-1)
        return steps
        # endregion

    def logout(self):
        self.driver.quit()


if __name__ == '__main__':
    login_user = '16602196703'
    login_passwd = 'wzy114906'
    jd = JD(login_user, login_passwd)
    jd.login()
    jd.logout()

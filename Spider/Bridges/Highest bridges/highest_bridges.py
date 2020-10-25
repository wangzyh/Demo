import csv
import os
import time
import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located as loads
from selenium.webdriver.support.ui import WebDriverWait

from Spider.setting import CHROME_DRIVER, DATA_FILE

root = 'http://www.highestbridges.com/wiki/index.php?title=List_of_Highest_International_Bridges'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class HighestBridges:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
        self.driver.maximize_window()
        self.csv_file = os.path.join(DATA_FILE, 'Highest Bridges.csv')
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def get_data(self):
        title = ['Rank', 'Name', 'Height (meters / feet)', 'Main Span Length (meters / feet)', 'Completed', 'Location',
                 'Country']
        d = []
        self.csv_write(title)
        for i in range(1):
            url = f'{root}/Page_1'
            self.driver.get(url)

            table = self.driver.find_elements_by_tag_name('tr')
            if len(table) <= 1:
                break
            for t in range(1, len(table)):
                for j in range(7):
                    try:
                        d.append(self.driver.find_element_by_xpath(
                            f'//*[@id="sortable_table_id_0"]/tbody/tr[{t + 1}]/td[{j + 2}]').text.decode('gbk'))
                    except NoSuchElementException:
                        break
                self.csv_write(d)
                d = []

    def csv_write(self, data):
        logger.info(data)
        with open(self.csv_file, 'a', newline='') as f:
            f_csv = csv.writer(f)
            try:
                f_csv.writerow(data)
            except UnicodeEncodeError:
                print(data)

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    hb = HighestBridges()
    hb.get_data()
    hb.quit()

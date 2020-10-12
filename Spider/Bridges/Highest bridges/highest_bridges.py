import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located as loads
from selenium.webdriver.support.ui import WebDriverWait

from Spider.setting import CHROME_DRIVER, DATA_FILE

root = 'http://www.highestbridges.com/wiki/index.php?title=List_of_Highest_International_Bridges'


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
        self.csv_write(title)
        for i in range(1):
            url = f'{root}/Page_1'
            self.driver.get(url)

            table = self.driver.find_elements_by_tag_name('tr')
            if len(table) <= 1:
                break
            for t in range(1, len(table)):
                for i in range(t):
                    data = []
                    for j in range(7):
                        data.append(self.driver.find_element_by_xpath(
                            f'//*[@id="sortable_table_id_0"]/tbody/tr[{i + 1}]/td[{j + 2}]').text)

                self.csv_write(data)

    def csv_write(self, data):
        with open(self.csv_file, 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(data)

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    hb = HighestBridges()
    hb.get_data()
    hb.quit()

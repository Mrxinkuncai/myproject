from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestUIAuto:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    def test_case(self):

        self.driver.find_element(By.XPATH,'/html/body/section/div/div[2]/div[3]/div/div/ul/li[1]').click()
        # def wait(x):
        #     # print(len(self.driver.find_element(By.XPATH,'/html/body/section/div/div[2]/div[5]/div[2]/div/div/div[2]/table/thead/tr/th[3]')))
        #     return len(self.driver.find_elements(By.XPATH,'/html/body/section/div/div[2]/div[3]/div/div/ul/li[4]')) >=1

        # expected_conditions.element_to_be_clickable(By.XPATH,"/html/body/section/div/div[2]/div[3]/div/div/ul/li[4]")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="ember37"]')))
        self.driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[3]/div/div/ul/li[2]').click()

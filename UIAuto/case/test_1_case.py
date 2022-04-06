import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
class TestUIAuto:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()
    def test_baidu(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element(By.XPATH,'//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID,"stfile").send_keys(r'E:\coding\myproject\UIAuto\data\Snipaste_2022-03-20_15-47-00.png')
        sleep(5)
    def test_te(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag=self.driver.find_element(By.ID,'draggable')
        drop=self.driver.find_element(By.ID,'droppable')
        action=ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(2)
        print("点击确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID,'submitBTN').click()
        sleep(3)

if __name__ == '__main__':
  TestUIAuto().test_baidu()
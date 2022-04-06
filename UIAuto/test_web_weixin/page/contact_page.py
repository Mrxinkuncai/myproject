from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from UIAuto.test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list=(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member=(By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    def goto_add_member(self):
        # 解决循环导入问题
        from UIAuto.test_web_weixin.page.add_member_page import AddMember
        """
        添加成员操作
        :return:
        """
        #添加显示等待保证按钮可以点击
        # WebDriverWait(self.driver,9).until(expected_conditions.visibility_of_element_located(self._location_goto_add_member))
        # sleep(3)
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)
    def get_member(self):
        """
        获取成员列表，用来做断言
        :return:
        """
        # self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        #把对象的数据提取出来

        WebDriverWait(self.driver,9).until(expected_conditions.visibility_of_all_elements_located(self._location_member_list))
        # sleep(3)
        member_list=[i.text for i in self.finds(*self._location_member_list)]
        print(member_list)
        return member_list
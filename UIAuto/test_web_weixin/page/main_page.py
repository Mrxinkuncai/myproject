from selenium.webdriver.common.by import By

from UIAuto.test_web_weixin.page.add_member_page import AddMember
from UIAuto.test_web_weixin.page.base_page import BasePage
from UIAuto.test_web_weixin.page.contact_page import ContactPage
from selenium import webdriver


#编写页面所具有的功能
class MainPage(BasePage):
    _location_goto_member=(By.CSS_SELECTOR,".ww_indexImg_AddMember")
    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        #解元组操作，把元组内的元素拆分作为不同的参数传入
        self.find(*self._location_goto_member).click()
        return AddMember(self.driver)
    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(by=By.ID,value="menu_contacts").click()
        return ContactPage(self.driver)
    def back_main(self):

        self.find(By.ID,"menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel']").click()
from selenium.webdriver.common.by import By

from UIAuto.test_web_weixin.page.base_page import BasePage
from UIAuto.test_web_weixin.page.contact_page import ContactPage


class AddMember(BasePage):
    _location_username=(By.ID, "username")
    _location_acctid=(By.ID,"memberAdd_acctid")
    _location_Add_phone=(By.ID,"memberAdd_phone")
    def add_member(self):
        """
        添加成员操作
        :return:
        """
        self.find(*self._location_username).send_keys("test2")
        self.find(*self._location_acctid).send_keys("test2")
        # self.driver.find_element(By.ID,"memberAdd_biz_mail").send_keys("test1")
        self.find(*self._location_Add_phone).send_keys("18012345673")
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return ContactPage(self.driver)


    def add_member_fail(self,acctid,phone):
        """
        添加成员失败操作
        :return:
        """
        self.driver.find_element(*self._location_username).send_keys("test2")
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        # self.driver.find_element(By.ID,"memberAdd_biz_mail").send_keys("test1")
        self.driver.find_element(*self._location_Add_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()
        # error_message=self.driver.find_element(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # phone_error_message=self.driver.find_element(By.CSS_SELECTOR,".ww_telInput_zipCode.js_countryCode_dropdown.ww_btnWithMenu .ww_telInput_mainNumber").text
        # print(error_message)
        # error_list=[error_message,phone_error_message]
        res=self.finds(By.CSS_SELECTOR,".ww_inputWithTips_tips")
        error_list=[i.text for i in res]
        return error_list
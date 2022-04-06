import pytest

from UIAuto.test_web_weixin.page.main_page import MainPage

#编写业务测试用例
class TestAddMember:
    def setup_class(self):
        self.main=MainPage()
    def test_add_member(self):
        """
        添加成员测试用例
        :return:
        """
        # 1、跳转添加成员页面 2、添加成员 3.自动跳转到通讯录页面
        res=self.main.goto_add_member().add_member().get_member()
        assert "test2" in res
    @pytest.mark.parametrize("accid,phone,expect_res",[("test2","18012345679","该帐号已被“test2”占有"),
                                                       ("test3","18012345678","该帐号已被“test2”占有")])
    def test_add_member_fail(self,accid,phone,expect_res):
        res=self.main.goto_add_member().add_member_fail(accid,phone)
        assert expect_res in res

    def test_add_member_by_contact(self):
        """
        通过通讯录页面添加成员
        :return:
        """
        res=self.main.goto_contact().goto_add_member().add_member().get_member()
        assert "test2" in res


    def teardowm(self):
        self.main.back_main()
    # def teardown_class(self):
    #     self.main.quit()
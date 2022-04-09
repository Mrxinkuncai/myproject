import pytest

from API.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact=Contact()
        self.userid = "test4"
        self.name = "test4"

    @pytest.mark.parametrize("corpid, corpsecret, result",[("xxx",None,40013),(None,"xxx",40001),(None ,None ,0 )])
    def test_token(self,corpid,corpsecret,result):
        r=self.contact.get_token(corpid,corpsecret)
        print(r)
        assert r.get("errcode") == result
    def test_create(self):

        self.contact.add_member(userid=self.userid,name=self.name,department=[1],mobile="12312341235",alias="test5")
        try:
            find_result=self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(userid=self.userid)
        assert find_result["name"]==self.name


    def test_update(self):
        self.contact.add_member(userid=self.userid,name=self.name,department=[1],mobile="12312341235",alias="test5")
        change_mobile="18012345678"
        self.contact.update_member(self.userid,self.name,[1],change_mobile)
        try:
            find_result=self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(userid=self.userid)
        assert find_result["mobile"]==change_mobile

    def test_delete(self):
        pass
    def test_find(self):
       r= self.contact.find_member("test2")
       print(r)
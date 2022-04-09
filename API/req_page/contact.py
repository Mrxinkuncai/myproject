import requests

from API.req_page.base import Base


class Contact(Base):
    # def __init__(self):


    # def get_token(self,corpid=None,corpsecret=None):
    #     if corpid is None:
    #         corpid=self.corpid
    #     if corpsecret is None:
    #         corpsecret=self.corpsecret
    #     params={"corpid":corpid,"corpsecret":corpsecret}
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    #     r = requests.get(url=url, params=params)
    #     token=r.json().get('access_token')
    #     # print(token)
    #     return r.json()
    def find_member(self,userid):
        # print(self.token)

        params={"userid":userid}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.s.get(url=url,params=params)
        # print(r.json())
        return r.json()
    def add_member(self, userid, name, department, mobile, **kwargs):
        # params={"access_token":self.token}
        data={
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile
        }
        data.update(kwargs)

        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        r = self.s.post(url=url,json=data,verify=False)
        # print(r.json())
        return r.json()
    def update_member(self,userid:str,name:str,department:list,mobile:str,**kwargs):
        # params = {"access_token": self.token}
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile
        }
        data.update(kwargs)
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        r = self.s.post(url=url, json=data, verify=False)
        # print(r.json())
        return r.json()
    def delete_member(self,userid):
        params = {"userid":userid}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = self.s.get(url=url,params=params, verify=False)
        # print(r.json())
        return r.json()
import requests
from requests import Session


class Base:
    def __init__(self):
        self.s=Session()
        self.corpid = "ww0097a194aa0b6600"
        self.corpsecret = "rgeM_-jcCxs9shkFrZUbAWUYdeZxtOY-73SkJoTqUWY"
        # self.token = self.get_token().get('access_token')
        self.s.params['access_token'] = self.get_token().get('access_token')

    def get_token(self,corpid=None,corpsecret=None):
        if corpid is None:
            corpid=self.corpid
        if corpsecret is None:
            corpsecret=self.corpsecret
        params={"corpid":corpid,"corpsecret":corpsecret}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url=url, params=params)
        token=r.json().get('access_token')
        # print(token)
        return r.json()
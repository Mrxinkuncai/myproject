import pytest
import requests

def test_contact():
    pass

def get_token():
    ID="ww0097a194aa0b6600"
    SECRET="rgeM_-jcCxs9shkFrZUbAWUYdeZxtOY-73SkJoTqUWY"
    url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}"
    r=requests.get(url=url)
    # print(r.json()['access_token'])
    return r.json()['access_token']


def test_get_user():
    USERID="test2"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid={USERID}"
    r = requests.get(url=url)
    print(r.json())
    return r.json()
def test_add_user():
    data={
        "userid": "zhangsan",
        "name": "张三",
        "department": [1],
        "mobile": "+86 13112314456"
    }

    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}"
    r = requests.post(url=url,json=data,verify=False)
    print(r.json())
    return r.json()
def test_update_user():
    data = {
        "userid": "zhangsan",
        "name": "张三12",
        "department": [1],
        "mobile": "+86 13112314457"
    }

    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    r = requests.post(url=url, json=data, verify=False)
    print(r.json())
    return r.json()
def test_delete_user():
    USERID="zhangsan"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid={USERID}"
    r = requests.get(url=url, verify=False)
    print(r.json())
    return r.json()

@pytest.mark.parametrize("left,right",[(2,6),(3,8),(4,5)])
def test_generate(left,right,pre=1):
    #边界值的生成
    result=[]
    lefts=[left-pre,left,left+pre]
    rights=[right-pre,right,right+pre]
    mid=(left+right)//2
    result += lefts
    result.append(mid)
    result +=rights
    print(set(result))
    return set(result)
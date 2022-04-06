from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase1:
    def test_demo(self):
        opt=webdriver.ChromeOptions()
        opt.debugger_address="localhost:9222"
        driver=webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element(By.ID,"menu_contacts").click()
        print(driver.get_cookies())


    def test_cookie(self):
        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688855153343963'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970326146977304'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688855153343963'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '9591946512295565'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a717646'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '01cSEOU2BdflZDhJfsJqAF0ZCQeRj2PWjMoVFifK3-UNuC08Jez_d5oCsMFatbwLZotF8C-l5fJbr9Mf2c5-GwDtNlfKtoxGX0WohpNnk7BCEinVz8My1E2OKQWtuf__T7sZkFM3hz9WOcImuGxKMAIW8yj6k34KpmcLOLIdh0XLvM5ncpPozvOyJwMj1Y7ko_Mn6VGVV5u-X6qvkSEsZIHtyK05cVa5MEXSGwesP8wSCfY2G2d2DlCU2W0zhWD4G45VZarZe8F0Gl_iEVog3w'}, {'domain': '.work.weixin.qq.com', 'expiry': 1650940835, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'nOeMm1zgVhX6hW7lw0QTEGVOdGE6Hur4bVEpOWcxPI_CoIfHjuYOY-nj227srUoG'}, {'domain': '.work.weixin.qq.com', 'expiry': 1677999732, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element(By.ID, "menu_contacts").click()
        sleep(5)
        driver.quit()
def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "localhost:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    cookie=driver.get_cookies()
    print(cookie)
    with open("./UIAuto/test_web_weixin/testcases/data.yaml",'w',encoding="UTF-8") as f:
        yaml.dump(cookie,f)
def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("UIAuto/test_web_weixin/testcases/data.yaml", encoding="UTF-8") as f:
        yaml_data=yaml.safe_load(f)
        for cookie in yaml_data:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    sleep(5)
    driver.quit()
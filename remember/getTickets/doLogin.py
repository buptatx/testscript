#! -*- coding:utf-8 -*-

import json
import requests
import urllib3

from PIL import Image

"""
该模块用于12306登录
"""


def my_raw_input(info):
    return raw_input(unicode(info, 'utf-8').encode('gbk'))


class DoLogin():
    def __init__(self):
        urllib3.disable_warnings()
        self.headers = {}
        self.create_headers()
        self.session = requests.session()
        self.verify_image_path = "./img.jpg"

    def create_headers(self):
        self.headers["Accept-Language"] = "zh-CN,zh;q=0.9,en;q=0.8"
        self.headers["Cache-Control"] = "no-cache"
        self.headers["Connection"] = "keep-alive"
        self.headers["Host"] = "kyfw.12306.cn"
        self.headers["Pragma"] = "no-cache"
        self.headers["Referer"] = "https://kyfw.12306.cn/otn/login/init"
        self.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

    def get_verify_img(self):
        url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
        response = self.session.get(url=url, headers=self.headers, verify=False)

        with open(self.verify_image_path, "wb") as imf:
            imf.write(response.content)

        try:
            im = Image.open(self.verify_image_path)
            im.show()
            im.close()
        except:
            print u'请输入验证码'

    def do_verify(self, solution):
        soList = solution.split(",")

        verSol = ['35,35','105,35','175,35','245,35','35,105','105,105','175,105','245,105']
        verlist = []

        for item in soList:
            verlist.append(verSol[int(item) - 1])

        verStr = ",".join(verlist)
        checkUrl = "https://kyfw.12306.cn/passport/captcha/captcha-check"
        req_data = {}
        req_data["login_site"] = 'E'
        req_data["rand"] = 'sjrand'
        req_data["answer"] = verStr

        cont = self.session.post(url=checkUrl, data=req_data, headers=self.headers, verify=False)
        cont_dict = json.loads(cont.content)
        assert "result_code" in cont_dict, u"校验失败"

        return cont_dict["result_code"] == "4"

    def do_login(self):
        uName = my_raw_input("请输入账号:")
        uPwd = my_raw_input('请输入密码:')
        with open("temp_account.txt", "wb+") as af:
            af.write("[acount]{}[pwd]{}".format(uName, uPwd))

        loginUrl = "https://kyfw.12306.cn/passport/web/login"
        req_data = {}
        req_data["username"] = uName
        req_data["password"] = uPwd
        req_data["appid"] = "otn"

        try:
            res = self.session.post(url=loginUrl, data=req_data, headers=self.headers, verify=False)
            assert res.status_code == 200, u"登录响应结果异常"
        except requests.ConnectionError as connect_error:
            print connect_error
        except requests.ConnectTimeout as connect_timeout_error:
            print connect_timeout_error
        except requests.HTTPError as http_error:
            print http_error
        except requests.Timeout as timeout_error:
            print timeout_error

        res_dict = json.loads(res.content)
        assert "result_message" in res_dict, u"登录失败"
        if res_dict["result_message"]:
            print u"登录成功"
            print res.content
        else:
            print u"登录失败"

    def login_entrance(self):
        self.get_verify_img()
        self.check_and_login()

    def check_and_login(self):
        cap_sol = my_raw_input('请输入验证码位置，以","分割[例如2,5]:')

        isVerify = self.do_verify(cap_sol)
        if isVerify:
            print u"图片校验成功"
            self.do_login()
        else:
            print u"图片校验失败"
            self.check_and_login()

if __name__ == "__main__":
    testor = DoLogin()
    testor.login_entrance()
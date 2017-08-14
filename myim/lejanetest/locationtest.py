#!/usr/bin/env python
#!-*- coding:utf-8 -*-


'''
author:zhp@chinabr.net
'''

import hashlib
import httplib2


def md5sign(org_str):
    m = hashlib.md5()
    m.update(org_str)

    res = m.hexdigest()

    return res


def checkYoubaoFeedBack():
    request_url = 'http://lecanbotest.sifude.cn/lejaneapi/lejane/user/sospd/youbao/call/v1?'
    #request_url = 'http://192.168.8.152:8080/lejaneapi/lejane/user/sospd/youbao/call/v1?'

    request_params = {}
    request_params["mobile"] = "13161269249"
    request_params["srvNo"] = "1703170020000035"
    request_params["key"] = "123456"

    org_str = "mobile={}&srvNo={}&key={}".format(request_params["mobile"],
                                                 request_params["srvNo"],
                                                 request_params["key"])
    print "[data for md5sign]:{}".format(org_str)

    sign_str = md5sign(org_str)
    request_str = "mobile={}&srvNo={}&sign={}".format(request_params["mobile"],
                                                      request_params["srvNo"],
                                                      sign_str)

    request_param = request_url + request_str
    print "[request params]:{}".format(request_param)

    httphandle = httplib2.Http()
    response, content = httphandle.request(request_param)

    print "[response content]:{}".format(content)


if __name__ == "__main__":
    checkYoubaoFeedBack()
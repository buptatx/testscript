#! /usr/bin/env python

import datetime
import httpRequest
import time


if __name__ == "__main__":
    test_env = "qa"

    # set http post-request url
    if test_env == "qa":
        # for qa-env
        test_url = "http://statisttest.sifude.cn/zeroone/usr/oper/push/v2.5.1"
    elif test_env == "online":
        # for online-env
        test_url = "http://statist.sifude.com/zeroone/usr/oper/push/v2.5.1"

    # set http post-request header
    test_header = {}
    test_header["Content-Type"] = "application/json"
    test_header["Accept"] = "application/json"
    test_header["Connection"] = "Keep-Alive"
    test_header["Accept-Encoding"] = "gzip"
    test_header["Cache-Control"] = "no-cache"
    test_header["User-Agent"] = "Android 5.1,Safety-Qa,qatest201702101,"\
        "TestDate_{}".format(datetime.datetime.now().strftime('%y%m%d_%H%M%S'))

    # set http post-request body
    test_device = {}
    test_device["ac"] = "wifi"
    test_device["act"] = "wifi"
    test_device["ak"] = "a97da629b098b75c294dffdc3e463904"
    test_device["akv"] = "2.6.1"
    test_device["akc"] = "81"
    test_device["car"] = "CHINA MOBILE"
    test_device["chan"] = "n_qa"
    test_device["cty"] = "CN"
    test_device["cpu"] = "mt6735"
    test_device["did"] = "qatest201702101"
    test_device["dm"] = "Safety-Qa"
    test_device["uid"] = "lejian_24056"
    test_device["lang"] = "cn"
    test_device["mc"] = "54:1f:f6:98:10:e7"
    test_device["osv"] = "6.0"
    test_device["plat"] = "1"
    test_device["reso"] = "720*1280"
    test_device["smid"] = "b95c012cdcf11"
    test_device["tz"] = "8"

    # set test statistic data
    test_extra = {}
    test_extra["lng"] = 113.670626
    test_extra["lat"] = 34.774565

    test_item = {}
    test_item["func"] = "100237"
    test_item["ot"] = int(round(time.time() * 1000))
    test_item["extra"] = test_extra

    test_data = []
    test_data.append(test_item)

    test_body = {}
    test_body["device"] = test_device
    test_body["datas"] = test_data

    # trigger http post-request
    test_entity = httpRequest.HttpRequest()
    test_entity.createJsonRequest(test_url, test_header, test_body)
    test_entity.sendRequest()

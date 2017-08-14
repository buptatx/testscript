#!/usr/bin/env python
#!-*- coding:utf-8 -*-


'''
author:zhp@chinabr.net
'''


import httpRequest
import time


def getTimestamp():
    timestamp = str((int)(time.time()*1000))

    return timestamp


def uploadUsrdata():
    request_url = 'http://lecanbotest.sifude.cn/lejaneapi/lejane/usrdata/upload/v2.4.1'

    curTimeStamp = getTimestamp()

    httpheader = {}
    httpheader["Content-Type"] = "application/json"

    httpbody = []
    request_params = {}
    request_params["checkTick"] = curTimeStamp
    request_params["checkTime"] = ""
    request_params["dataValue"] = "1000"
    request_params["membId"] = "327"
    request_params["dataType"] = "step"
    httpbody.append(request_params)

    lejaneSend = httpRequest.HttpRequest()
    lejaneSend.createJsonRequest(request_url, httpheader, httpbody)

    res = lejaneSend.sendRequest()
    print "[response content]:{}".format(res)


if __name__ == "__main__":
    uploadUsrdata()
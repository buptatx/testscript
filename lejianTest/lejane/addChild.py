#coding=utf-8

"""
author : zhangpeng
"""

import httpRequest

def main():
    request_url = "http://192.168.8.212:15002/lejaneapp/lejane/family/add/v1"

    httpheader = {}
    httpheader["Content-Type"] = "application/json"

    httpbody = []
    child = {}

    child["membId"] = 241
    child["membPhone"] = "15202124923"
    child["childPhone"] = "15810537243"
    child["contactName"] = "毕云涛"
    httpbody.append(child.copy())

    child["membId"] = 241
    child["membPhone"] = "15202124923"
    child["childPhone"] = "1234567891231456457986562213"
    child["contactName"] = "1234567891231456457986562213"
    httpbody.append(child.copy())

    lejaneSend = httpRequest.HttpRequest()
    lejaneSend.createJsonRequest(request_url, httpheader, httpbody)

    res = lejaneSend.sendRequest()
    print res

if __name__ == "__main__":
    main()
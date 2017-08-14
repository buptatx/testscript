#coding=utf-8

"""
script for delete pics from server
"""

import httpRequest
import queryChildPhone


def main():
    myQueryer = queryChildPhone.MySqlExecuter("192.168.8.213", "sifude", "sifude@2015", "posteritytest")
    pathList = myQueryer.queryPicsPath(24, 5034)

    request_url = "http://192.168.8.212:15002/lejaneposterity/pic/delete/v1"

    httpheader = {}
    httpheader["Content-Type"] = "application/x-www-form-urlencoded"

    for path in pathList:
        httpbody = {}
        httpbody["filePath"] = path

        lejaneSend = httpRequest.HttpRequest()
        lejaneSend.createRequest(request_url, httpheader, httpbody)

        res = lejaneSend.sendRequest()
        print res


if __name__ == "__main__":
    main()
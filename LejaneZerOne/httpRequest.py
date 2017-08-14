#coding=utf-8

"""
this class used for send http-post request
and response analyse
author:zhangpeng
"""

import json
import urllib
import urllib2
import sys

class HttpRequest():
    """
    this class is used for http-request and response-analyse
    """
    def __init__(self):
        self.httpClient = None
        self.params  = {}
        self.destUrl = ""
        self.httpReq = None

    def setUrl(self, server):
        """
        :param server:  server base url
        :return: None
        """
        self.destUrl = server

    def setParams(self, params):
        """
        :param params: set http-post body data
        :return: None
        """
        self.params = urllib.urlencode(params)

    def createRequest(self, request_url, hheader, hbody):
        """
        create a http request object by urllib2
        :return:None
        """
        self.setUrl(request_url)
        self.setParams(hbody)
        self.httpReq = urllib2.Request(self.destUrl, self.params)
        if len(hheader) != 0:
            self.addHeader(hheader)

    def createJsonRequest(self, request_url, hheader, hbody):
        """
        create a http request object by urllib2
        :return:None
        """
        self.setUrl(request_url)
        self.httpReq = urllib2.Request(self.destUrl, json.dumps(hbody))
        if len(hheader) != 0:
            self.addHeader(hheader)

    def addHeader(self, headerdict):
        """
        add extend headers for http request
        :param headerdict: dict of extend header with header-attribute and header-value
        :return:None
        """
        for mkey in headerdict:
            self.httpReq.add_header(mkey, headerdict[mkey])

    def sendRequest(self):
        """
        main entrance of this class
        :return: None
        """
        try:
            response = urllib2.urlopen(self.httpReq)
            res_data = response.read()
        except Exception as e:
            print "catch error" + str(e)
            return str(e)

        return res_data


def main():
    request_url = "http://192.168.8.212:15002/lejaneapp/lejane/usr/detail/v1"

    httpheader = {}
    httpheader["Content-Type"] = "application/x-www-form-urlencoded"

    httpbody = {}
    httpbody["membId"] = 214

    lejaneSend = HttpRequest()
    lejaneSend.createRequest(request_url, httpheader, httpbody)

    res = lejaneSend.sendRequest()
    if res is None:
        return -1
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
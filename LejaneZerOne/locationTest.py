#! /usr/bin/env python

import datetime
import httpRequest
import time


if __name__ == "__main__":
    test_env = "qa"

    # set http post-request url
    if test_env == "qa":
        # for qa-env
        test_url = "http://192.168.8.206:803/lejaneapi/lejane/location/add/v1"
    elif test_env == "online":
        # for online-env
        test_url = "http://192.168.8.206:803/lejaneapi/lejane/location/add/v1"

    # set http post-request header
    test_header = {}
    test_header["Content-Type"] = "application/x-www-form-urlencoded"
    test_header["Connection"] = "Keep-Alive"
    test_header["Accept-Encoding"] = "gzip"
    test_header["Cache-Control"] = "no-cache"
    test_header["User-Agent"] = "Android 5.1,Safety-Qa,qatest201702101,"\
        "TestDate_{}".format(datetime.datetime.now().strftime('%y%m%d_%H%M%S'))

    # set http post-request body
    test_body = {}
    test_body["lnkId"] = 18865
    test_body["latitude"] = 39.933563
    test_body["longitude"] = 116.468851

    # trigger http post-request
    test_entity = httpRequest.HttpRequest()
    test_entity.createRequest(test_url, test_header, test_body)
    test_entity.sendRequest()

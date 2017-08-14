#coding=utf-8

"""
this class used for upload pics to server
and response analyse
author:zhangpeng
"""

import datetime
import json
import sys
import requests

class PhotoHttpRequest():
    """
    this class is used for http-request and response-analyse
    """
    def upLoadPhoto(self, destUrl, mheader, mbody, mfile):
        """
        :param destUrl: upload url
        :param mheader: post header with token for indentifing
        :param mbody: childId and uploadtimestamp
        :param mfile: photodata
        :return:
        """
        try:
            response = requests.post(destUrl, headers=mheader,
                                     data=mbody,
                                     files=mfile)
            res_data = response.text
        except Exception as e:
            print "[catch error]：" + str(e)
            return str(e)

        return res_data


def main():
    request_url = "http://192.168.8.212:15002/lejaneposterity/pic/upload/v1"
    #request_url = "http://192.168.8.212:15002/lejaneposterity/pic/lejane/upload/v1"

    httpheader = {}
    httpheader["token"] = "d41d8cd98f00b204e9800998ecf8427e"

    httpbody = {}
    httpbody["childId"] = 10
    #httpbody["membId"] = 43
    httpbody["uploadTime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    photoHandle = open(r".\photos\bys.jpg", "rb")
    photoFile = {"file" : photoHandle}

    photoSender = PhotoHttpRequest()
    res = photoSender.upLoadPhoto(request_url, httpheader, httpbody, photoFile)

    print res

    photoHandle.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
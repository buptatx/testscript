#!/usr/bin/env python
#! -*- coding=utf-8 -*-

"""
author zhp@chinabr.net
"""

import createxcel
import os
import urllib2
import wxwebparser
import wxvideowebparser


class WYSpider:
    def __init__(self, purl):
        """
        :param purl:source url
        """
        self.purl = purl
        self.result = []

    def output_purl(self):
        """
        output source url to stdout
        :return:
        """
        print "[purl]{}".format(self.purl)

    def get_purl_webpage(self, weburl):
        """
        download source url code
        :return: source url code
        """
        request = urllib2.Request(weburl)
        response = urllib2.urlopen(request)

        return response.read()

    def get_first_layer(self):
        """
        parse webpage and return label:title:href
        :return: list of wx disease with elements label:title:href
        """
        code = self.get_purl_webpage(self.purl)

        myparser = wxwebparser.WXWebParser()
        myparser.feed(code)

        return myparser.get_content()

    def get_second_layer(self, surl):
        webpage = self.get_purl_webpage(surl)

        myparser = wxvideowebparser.WXVideoWebParser()
        myparser.feed(webpage)

        return myparser.get_content()

    def get_result(self):
        """
        main entrance of this class
        do all procedure to parse webpage
        :return: list of webpage parse result label:title:href:doctor:video
        """
        first_layer = self.get_first_layer()
        for item in first_layer:
            surl = "".join([self.purl, item["href"][1:]])

            second_layer = self.get_second_layer(surl)
            for sitem in second_layer:
                temp = {}
                temp["label"] = item["label"]
                temp["title"] = item["title"]
                temp["href"] = surl

                temp["doctor"] = sitem["doctor"]
                #for doctor image
                temp["docimage"] = sitem["docimage"]
                temp["videoname"] = sitem["title"]
                temp["videohref"] = sitem["href"]

                self.result.append(temp)

        return self.result


def save_file(content):
    """
    :param content:save content 
    :return: null
    """
    if os.path.exists("result\\toky.txt"):
        os.remove("result\\toky.txt")

    with open("result\\toky.txt", "a+") as fhandle:
        for temp in content:
            line = "[label]{}[title]{}[href]{}[doctor]{}[docimage]{}[videoname]{}[videohref]{}\n".format(temp["label"],
            temp["title"], temp["href"], temp["doctor"], temp["docimage"], temp["videoname"], temp["videohref"])
            fhandle.write(line)

    createxcel.save_as_excel(content)


if __name__ == "__main__":
    purl = "http://www.mvyxws.com/"

    mywx = WYSpider(purl)
    result = mywx.get_result()

    save_file(result)
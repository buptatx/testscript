#!/usr/bin/env python
#! -*- coding=utf-8 -*-

"""
author zhp@chinabr.net
this script is used for testing wx second layer parse
"""

import urllib2
import wxvideowebparser


if __name__ == "__main__":
    surl = "http://www.mvyxws.com/index.php/vod/disease?cid=267"

    req = urllib2.Request(surl)
    res = urllib2.urlopen(req)

    webpage = res.read()

    wxvideoparser = wxvideowebparser.WXVideoWebParser()
    wxvideoparser.feed(webpage)

    wxvideoparser.print_content()


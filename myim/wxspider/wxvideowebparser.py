#!/usr/bin/env python
#!-*- coding=utf-8 -*-

"""
author zhp@chinabr.net
"""

from sgmllib import SGMLParser


class WXVideoWebParser(SGMLParser):
    """
    this class is used for parse wx second layer
    get doctor name and video href
    """
    def reset(self):
        SGMLParser.reset(self)
        self.content = []
        self.doctor = ""
        self.docimage = ""
        self.url_prefix = "http://www.mvyxws.com/"
        self.catch_ul_flag = False
        self.catch_ul_a_flag = False
        self.catch_h2_flag = False
        self.catch_h2_a_flag = False
        self.catch_h2_span_flag = False
        self.catch_div_flag = False
        self.catch_div_img_flag = False

    def start_h2(self, attr):
        if not self.catch_h2_flag:
            for k, v in attr:
                if k == "class" and v == "listtit":
                    self.catch_h2_flag = True
                    return

    def end_h2(self):
        if self.catch_h2_flag:
            self.catch_h2_flag = False

    def start_a(self, attr):
        if self.catch_h2_flag:
            self.catch_h2_a_flag = True
            return

        if self.catch_ul_flag:
            self.catch_ul_a_flag = True

            temp = {}
            temp["doctor"] = self.doctor
            temp["docimage"] = self.docimage

            for k, v in attr:
                if k == "href":
                    temp["href"] = "".join([self.url_prefix, v[1:]])

                if k == "title":
                    temp["title"] = v

            self.content.append(temp)

    def end_a(self):
        if self.catch_h2_a_flag:
            self.catch_h2_a_flag = False

        if self.catch_ul_a_flag:
            self.catch_ul_a_flag = False

    def start_span(self, attr):
        if self.catch_h2_flag:
            self.catch_h2_span_flag = True

    def end_span(self):
        if self.catch_h2_span_flag:
            self.catch_h2_span_flag = False

    def start_ul(self, attr):
        if not self.catch_ul_flag:
            for k, v in attr:
                if k == "class" and v == "jb-list":
                    self.catch_ul_flag = True
                    return

    def end_ul(self):
        if self.catch_ul_flag:
            self.catch_ul_flag = False

    def start_div(self, attr):
        if not self.catch_div_flag:
            for k,v in attr:
                if k == "class" and v == "tx":
                    self.catch_div_flag = True
                    return

    def end_div(self):
        if self.catch_div_flag:
            self.catch_div_flag = False

    def start_img(self, attr):
        if self.catch_div_flag:
            self.catch_div_img_flag = True

            for k, v in attr:
                if k == "src":
                    self.docimage = "".join([self.url_prefix, v[1:]])

    def end_img(self):
        if self.catch_div_img_flag:
            self.catch_div_img_flag = False

    def handle_data(self, data):
        if self.catch_h2_a_flag:
            self.doctor = data

        if self.catch_h2_span_flag:
            self.doctor += data

    def get_content(self):
        return self.content

    def print_content(self):
        for item in self.content:
            print "[doctor]{}[docimage]{}[title]{}[videohref]{}".format(
                item["doctor"], item["docimage"], item["title"], item["href"])
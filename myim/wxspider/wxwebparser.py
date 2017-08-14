#!/usr/bin/env python
#!-*- coding:utf-8 -*-

"""
author zhp@chinabr.net
"""

from sgmllib import SGMLParser


class WXWebParser(SGMLParser):
    """
    this class used for parse wx web source
    """
    def reset(self):
        SGMLParser.reset(self)
        self.catch_dev_flag = False
        self.catch_dev_a_flag = False
        self.catch_dev_h2_flag = False
        self.depth = 0
        self.content = []
        self.current_disease_label = ""

    def start_div(self, attrs):
        if not self.catch_dev_flag:
            for k,v in attrs:
                if k == 'class' and v == 'category':
                    self.catch_dev_flag = True
                    return
        else:
            self.depth += 1

    def end_div(self):
        if self.depth == 0:
            self.catch_dev_flag = False
            self.current_disease_label = ""
        if self.catch_dev_flag:
            self.depth -= 1

    def start_a(self, attr):
        if not self.catch_dev_flag:
            return
        self.catch_dev_a_flag = True

        temp = {}
        temp["label"] = self.current_disease_label
        for k, v in attr:
            if k == 'href':
                temp["href"] = v
            if k == 'title':
                temp["title"] = v

        self.content.append(temp)

    def end_a(self):
        if self.catch_dev_a_flag:
            self.catch_dev_a_flag = False

    def start_h2(self, attr):
        if not self.catch_dev_flag:
            return
        if not self.catch_dev_h2_flag:
            self.catch_dev_h2_flag = True

    def end_h2(self):
        if self.catch_dev_h2_flag:
            self.catch_dev_h2_flag = False

    def handle_data(self, text):
        if self.catch_dev_h2_flag:
            self.current_disease_label = text

    def print_content(self):
        for item in self.content:
            print "[label]{}[title]{}[href]{}".format(item["label"], item["title"], item["href"])

    def get_content(self):
        return self.content
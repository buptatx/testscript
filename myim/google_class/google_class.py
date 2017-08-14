#!/usr/bin/env python
#!-*- coding=utf-8 -*-

'''
author : zhp@chinabr.net
'''

import re
import sys

def test_args():
    for i in range(len(sys.argv)):
        print "[{}] {}".format(i, sys.argv[i])


def Find(pat, text):
    match = re.search(pat, text)

    if match:
        print match.group()
    else:
        print "not found"


def test_re():
    mpattern = r"[\w.]+@[\w.]+"
    mtext = "fuck x xx xxx x zhang.peng@gmail.com"
    Find(mpattern, mtext)


if __name__ == "__main__":
    #test_args()
    test_re()
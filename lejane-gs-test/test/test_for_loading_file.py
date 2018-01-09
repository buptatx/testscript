#！ -*- coding:utf-8 -*-

import sys


def getContent(path):
    with open(path, "rb") as mf:
        for line in mf:
            print line.strip()


if __name__ == "__main__":
    filename = sys.argv[1]
    getContent(filename)
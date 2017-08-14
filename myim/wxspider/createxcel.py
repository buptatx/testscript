#!/usr/bin/env python
#! -*- coding=utf-8 -*-

"""
this script is used for create excel and save input content
author zhp@chinabr.net
"""

import xlwt


def get_content():
    content = []
    content.append({"label":"zp", "title":"bbb", "href":"ccc",
                    "doctor":"ddd", "videoname":"eee", "videohref":"fff1"})
    content.append({"label":"mhy", "title":"bbb", "href":"ccc",
                    "doctor":"ddd", "videoname":"eee", "videohref":"fff2"})
    content.append({"label":"wky", "title":"bbb", "href":"ccc",
                    "doctor":"ddd", "videoname":"eee", "videohref":"fff3"})
    content.append({"label":"wr", "title":"bbb", "href":"ccc",
                    "doctor":"ddd", "videoname":"eee", "videohref":"fff4"})

    print content
    return content


def save_as_excel(content):
    myexcel = xlwt.Workbook(encoding="utf-8")
    myws = myexcel.add_sheet("微医节目表")

    myws.write(0, 0, "疾病科目")
    myws.write(0, 1, "具体疾病")
    myws.write(0, 2, "页面链接")
    myws.write(0, 3, "医生")
    myws.write(0, 4, "医生头像")
    myws.write(0, 5, "视频名称")
    myws.write(0, 6, "视频链接")

    data_index = 1
    for item in content:
        myws.write(data_index, 0, item["label"])
        myws.write(data_index, 1, item["title"])
        myws.write(data_index, 2, item["href"])
        myws.write(data_index, 3, item["doctor"])
        myws.write(data_index, 4, item["docimage"])
        myws.write(data_index, 5, item["videoname"])
        myws.write(data_index, 6, item["videohref"])
        data_index += 1

    myexcel.save('result\\ws4ky.xls')


if __name__ == "__main__":
    content = get_content()
    save_as_excel(content)
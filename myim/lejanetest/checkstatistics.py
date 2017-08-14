#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
author: zhangpeng@chinabr.net
'''


import json
import time


def convert_timestamp(timestr):
    tmp = time.localtime(float(timestr)/1000)

    return time.strftime("%Y-%m-%d %H:%M:%S", tmp)


def get_req_data(filename):
    with open(filename, "r") as mhandle:
        content = mhandle.read().strip("")

    return content


def get_func_list_from_request(req):
    req_dict = json.loads(req)
    req_data = req_dict["datas"]

    req_func_list = []
    for item in req_data:
        temp = {}
        temp["ot"] = convert_timestamp(item["ot"])
        temp["func"] = item["func"]
        req_func_list.append(temp)

    return req_func_list


def get_statistics_log(path):
    content = []

    with open(path, "r") as mhandle:
        for line in mhandle:
            content.append(line)

    return content


def get_func_list_from_log(content):
    func_list = []

    for item in content:
        temp = json.loads(item)
        func_list.append({"func" : temp["pi_func"], "ot" : temp["pi_ot"]})

    return func_list


def compare_func_list(req_list, record_list):
    if len(record_list) != len(req_list):
        print "length not equal"
        return

    for idx in range(len(req_list)):
        temp_req = req_list[idx]
        temp_record = record_list[idx]

        if temp_req['ot'] != temp_record['ot']:
            print "ot not equal {} {}".format(temp_req['ot'], temp_record['ot'])
        if temp_req['func'] != temp_record['func']:
            if "." in temp_req['func']:
                print "func not equal {} {}".format(temp_req['func'], temp_record['func'])
            else:
                temp_int_req = (int)(temp_req['func'])
                if temp_int_req < 24:
                    temp_req['func'] = '1001' + temp_req['func']
                    if temp_req['func'] != temp_record['func']:
                        print "func not equal {} {}".format(temp_req['func'], temp_record['func'])

    print "func:ot list in req and record are equal"


if __name__ == "__main__":
    req_file = "./data/zp.0505.req.log"
    req = get_req_data(req_file)

    func_list = get_func_list_from_request(req)
    print func_list

    path = "./data/zp.0505.record.log"
    content = get_statistics_log(path)
    uploaded_func_list = get_func_list_from_log(content)
    print uploaded_func_list

    compare_func_list(func_list, uploaded_func_list)




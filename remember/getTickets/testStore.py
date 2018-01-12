#! -*- coding:utf-8 -*-

import doLogin
def analyse_single_result(res):
    res_list = res.split("|")
    idx = 1
    for item in res_list:
        print "[{}] {}".format(idx, item)
        idx += 1

def test_raw_input():
    start_time = doLogin.my_raw_input("请输入出发时间（例：2018-01-10）：")
    start_station = doLogin.my_raw_input("请输入起始站：").decode("gbk")
    end_station = doLogin.my_raw_input("请输入终点站：").decode("gbk")

    print start_time
    print start_station
    print end_station


def my_raw_input(info):
    return raw_input(unicode(info,'utf-8').encode('gbk'))

if __name__ == "__main__":
    # res = "|预订|24000K430108|K4301|BXP|CQW|BXP|HAF|02:08|08:57|06:49|N|Tvb9bTIKePelcqvMR4TwN62beaaCV7m4GsuPwMSiYYcdiMPDXAOZqmyq4t0%3D|20180210|3|PC|01|05|0|0||||无|||无||无|无|||||10401030|1413|0"
    # analyse_single_result(res)
    test_raw_input()
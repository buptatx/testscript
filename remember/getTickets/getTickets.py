#! -*- coding:utf-8 -*-

import doLogin
import GetStationCode
import showMeTickets


def getTickets():
    customer = doLogin.DoLogin()
    isLogin, custom_session = customer.login_entrance()

    if not isLogin:
        exit(-1)

    s_time, s_station, e_station = get_ticket_info()
    query = showMeTickets.ShowMeTickets(custom_session)
    query.query_ticket(s_time, s_station, e_station)


def get_ticket_info():
    start_time = doLogin.my_raw_input("请输入出发时间（例：2018-01-10）：")
    start_station = doLogin.my_raw_input("请输入起始站：").decode("gbk").encode("utf-8")
    end_station = doLogin.my_raw_input("请输入终点站：").decode("gbk").encode("utf-8")

    station_code = GetStationCode.GetStationCode()
    start_station_code = station_code.getStationCode(start_station)
    end_station_code = station_code.getStationCode(end_station)

    print start_time, start_station_code, end_station_code
    return start_time, start_station_code, end_station_code


if __name__ == "__main__":
    getTickets()
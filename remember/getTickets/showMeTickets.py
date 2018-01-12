#! -*- coding:utf-8 -*-

import json
import requests


class ShowMeTickets():
    def __init__(self, sDate, fStation, tStation):
        self.query_ticket_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ"
        self.train_date = sDate
        self.start_station = fStation
        self.end_station = tStation

    def query_ticket(self):
        #生成查询url
        query_list = []
        query_list.append("?leftTicketDTO.train_date={}".format(self.train_date))
        query_list.append("leftTicketDTO.from_station={}".format(self.start_station))
        query_list.append("leftTicketDTO.to_station={}".format(self.end_station))
        query_list.append("purpose_codes=ADULT")

        query_str = self.query_ticket_url + "&".join(query_list)
        print query_str

        res = requests.get(query_str)
        res.encoding="utf-8"
        res_json = res.json()
        self.analyse_ticket_query_result(res_json)

    def analyse_ticket_query_result(self, res_json):
        assert res_json["status"] is True, u"查询车票信息失败"
        assert res_json["httpstatus"] == 200, u"查询车票HTTP请求失败"
        assert "result" in res_json["data"], u"result字段缺失"
        for item in res_json["data"]["result"]:
            print item



if __name__ == "__main__":
    test = ShowMeTickets("2018-02-10", "BJP", "HFF")
    test.query_ticket()
#! -*- coding:utf-8 -*-

import requests


class ShowMeTickets():
    def __init__(self, session):
        self.query_ticket_url = "https://kyfw.12306.cn/otn/leftTicket/queryZ"
        self.session = session

    def query_ticket(self, train_date, start_station, end_station):
        #生成查询url
        query_list = []
        query_list.append("?leftTicketDTO.train_date={}".format(train_date))
        query_list.append("leftTicketDTO.from_station={}".format(start_station))
        query_list.append("leftTicketDTO.to_station={}".format(end_station))
        query_list.append("purpose_codes=ADULT")

        query_str = self.query_ticket_url + "&".join(query_list)
        print query_str

        try:
            res = self.session.get(query_str)
        except requests.ConnectionError as connect_error:
            print connect_error
        except requests.ConnectTimeout as connect_timeout_error:
            print connect_timeout_error
        except requests.HTTPError as http_error:
            print http_error
        except requests.Timeout as timeout_error:
            print timeout_error

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
    session = requests.session()
    test = ShowMeTickets(session)
    test.query_ticket("2018-02-10", "BJP", "HFF")
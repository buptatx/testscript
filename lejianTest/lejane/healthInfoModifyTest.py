#coding=utf-8

"""
this module is used for query of member health info
author:zhangpeng
"""

import httpRequest
import json
import time
import unittest

class MembHealthModifyTestCase(unittest.TestCase):
    """
    test class for modify of member health info
    """
    def setUp(self):
        self.lejaneTest = httpRequest.HttpRequest()
        self.request_url = "http://192.168.8.212:15002/lejaneapp/lejane/usr/archives/edit/v1"
        self.defaultMembId = 256

    def tearDown(self):
        pass

    def infoQuery(self, membId, checkflag=1):
        """
        query base info of member with special membId
        :param membId:
        :return:result dict
        """
        # get org data
        org_data = httpRequest.HttpRequest()
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = membId

        query_url = "http://192.168.8.212:15002/lejaneapp/lejane/usr/archives/v1"
        org_data.createRequest(query_url, httpheader, httpbody)

        res = org_data.sendRequest()
        print "[org_data]{r}".format(r=res)

        if checkflag:
            # check data correction
            org_data_json = json.loads(res)
            self.assertIn("result", org_data_json, "结果数据中没有result字段")
            self.assertIn("membId", org_data_json["result"], "结果数据中不存在会员ID")
            self.assertEqual(membId, org_data_json["result"]["membId"], "查询数据会员Id关联错误")

            return org_data_json["result"]
        else:
            org_data_json = json.loads(res, encoding="UTF-8", ensure_ascii=False)

            return org_data_json

    def compareFormatTime(self, oldtime, newtime):
        """
        check update time refreshed
        :param oldtime: org baseinfo updatetime
        :param newtime: current baseinfo updatetime
        :return:True if newtime is larger than oldtime
        False if not
        """
        oldt = time.mktime(time.strptime(oldtime, "%Y-%m-%d %H:%M:%S"))
        newt = time.mktime(time.strptime(newtime, "%Y-%m-%d %H:%M:%S"))
        print oldt,newt
        if float(newt) >= float(oldt):
            return True
        else:
            return False

    def testLevel1_arcHabModify(self):
        """
        test for correct process
        :return:None
        """
        # record org data
        org_base_info = self.infoQuery(self.defaultMembId)
        m_arcId = org_base_info["arcId"]
        m_habId = org_base_info["habId"]

        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["arcId"] = m_arcId
        httpbody["habId"] = m_habId
        httpbody["highPressure"] = 112
        httpbody["lowPressure"] = 78
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 0
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 2
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(2, res_json["result"], "更新会员信息失败")
        self.assertEqual("编辑健康档案成功", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in httpbody:
            if isinstance(httpbody[mkey], str):
                self.assertEqual(httpbody[mkey].decode("utf-8"), current_base_info[mkey])
            else:
                self.assertEqual(httpbody[mkey], current_base_info[mkey])

if __name__ == "__main__":
    unittest.main()
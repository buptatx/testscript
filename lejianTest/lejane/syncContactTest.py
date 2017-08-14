#coding=utf-8

"""
this module is used for sync contact
author:zhangpeng
"""

import httpRequest
import json
import mySqlQuery
import unittest

class MembContantSyncTestCase(unittest.TestCase):
    """
    test class for query of member base info
    """
    def setUp(self):
        self.lejaneTest = httpRequest.HttpRequest()
        self.request_url = "http://192.168.8.212:15002/lejaneapp/lejane/contact/sync/v1"
        self.defaultMembId = 239

    def tearDown(self):
        pass

    def testLevel1_sync_oneRecord(self):
        """
        test for correct process
        :return:
        """
        httpheader = {}
        httpheader["Content-Type"] = "application/json"

        httpbody = []
        httpbody.append({"membId": self.defaultMembId, "name": "cnmd", "phone": "15810537242", "type": 0})

        self.lejaneTest.createJsonRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "查询会员信息失败")
        self.assertEqual("同步成功", res_json["description"].encode('utf-8'),
                         "描述信息不符合期望")
        self.assertIn("result", res_json, "结果数据中没有result字段")
        self.assertEqual(1, res_json["result"], "插入数据条目错误")

        query_result = mySqlQuery.membContactQuery(self.defaultMembId)
        self.assertEqual(len(httpbody), len(query_result))

    def testLevel1_sync_Records_withSameName(self):
        """
        test for correct process
        :return:
        """
        httpheader = {}
        httpheader["Content-Type"] = "application/json"

        httpbody = []
        httpbody.append({"membId": self.defaultMembId, "name": "cnm", "phone": "15810537242", "type": 0})
        httpbody.append({"membId": self.defaultMembId, "name": "cnm", "phone": "15810537243", "type": 0})

        self.lejaneTest.createJsonRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "查询会员信息失败")
        self.assertEqual("同步成功", res_json["description"].encode('utf-8'),
                         "描述信息不符合期望")
        self.assertIn("result", res_json, "结果数据中没有result字段")
        self.assertEqual(2, res_json["result"], "插入数据条目错误")

        query_result = mySqlQuery.membContactQuery(self.defaultMembId)
        self.assertEqual(len(httpbody), len(query_result))

    def testLevel3_sync_emptyJsonlist(self):
        """
        test for emptyJson
        :return:
        """
        httpheader = {}
        httpheader["Content-Type"] = "application/json"

        httpbody = []

        self.lejaneTest.createJsonRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "查询会员信息失败")
        self.assertEqual("未同步任何数据", res_json["description"].encode('utf-8'),
                          "描述信息不符合期望")
        self.assertIn("result", res_json, "结果数据中没有result字段")
        self.assertEqual(0, res_json["result"], "结果数据中result不符合期望")


if __name__ == "__main__":
    unittest.main()
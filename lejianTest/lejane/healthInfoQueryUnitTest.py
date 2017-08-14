#coding=utf-8

"""
this module is used for query of member health info
author:zhangpeng
"""

import httpRequest
import json
import unittest

class MembHealthInfoTestCase(unittest.TestCase):
    """
    test class for query of member health info
    """
    def setUp(self):
        self.lejaneTest = httpRequest.HttpRequest()
        self.request_url = "http://192.168.8.212:15002/lejaneapp/lejane/usr/archives/v1"
        #self.request_url = "http://lecanbo.sifude.com/lejaneapp/lejane/usr/archives/v1"
        self.defaultMembId = 239
        #self.defaultMembId = 18243

    def tearDown(self):
        pass

    def testLevel1_healthCheck(self):
        """
        test for correct process
        :return:
        """
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "查询会员信息失败")
        self.assertEqual("查询会员健康档案成功", res_json["description"].encode('utf-8'),
                         "查询成功描述信息不符合期望")
        self.assertIn("result", res_json, "结果数据中没有result字段")
        self.assertIn("membId", res_json["result"], "结果数据中不存在会员ID")
        self.assertEqual(self.defaultMembId, res_json["result"]["membId"], "查询数据会员Id关联错误")

    def testLevel2_stringmembId(self):
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = str(self.defaultMembId)

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "查询会员信息失败")
        self.assertEqual("查询会员健康档案成功", res_json["description"].encode('utf-8'),
                         "查询成功描述信息不符合期望")
        self.assertIn("result", res_json, "结果数据中没有result字段")
        self.assertIn("membId", res_json["result"], "结果数据中不存在会员ID")
        self.assertEqual(self.defaultMembId, res_json["result"]["membId"], "查询数据会员Id关联错误")

    def testLevel2_membId_0(self):
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = 0

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "查询会员信息失败")
        self.assertEqual("查询会员健康档案成功", res_json["description"].encode('utf-8'),
                         "查询成功描述信息不符合期望")
        self.assertIsNone(res_json["result"], "结果数据中result字段非空")

    def testLevel2_membId_9999(self):
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = 9999

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "查询会员信息失败")
        self.assertEqual("查询会员健康档案成功", res_json["description"].encode('utf-8'),
                         "查询成功描述信息不符合期望")
        self.assertIsNone(res_json["result"], "结果数据中result字段非空")

    def testLevel2_floatmembId_214dot01(self):
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = 214.01

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        res_json = json.loads(res)

        # check response
        self.assertIn("status", res_json, "返回结果中不存在status")
        self.assertFalse(res_json["status"], "返回结果中的status不符合期望")
        self.assertIn("description", res_json, "返回结果中不存在description")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'), "错误描述不符合期望")
        self.assertIn("result", res_json, "返回结果中不存在result")

        for item in res_json["result"]:
            if item["parameter"] == "membId":
                self.assertEqual("membId参数输入类型错误", item["errMsg"].encode('utf-8'), "错误描述不符合期望")

    def testLevel3_missmembId(self):
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["memId"] = self.defaultMembId

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print res
        res_json = json.loads(res)

        # check response
        self.assertIn("status", res_json, "返回结果中不存在status")
        self.assertFalse(res_json["status"], "返回结果中的status不符合期望")
        self.assertIn("description", res_json, "返回结果中不存在description")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'), "错误描述不符合期望")
        self.assertIn("result", res_json, "返回结果中不存在result")

        for item in res_json["result"]:
            if item["parameter"] == "membId":
                self.assertEqual("不能为null", item["errMsg"].encode('utf-8'), "错误描述不符合期望")

    def testLevel3_emptymembId(self):
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["memId"] = ""

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print res
        res_json = json.loads(res)

        # check response
        self.assertIn("status", res_json, "返回结果中不存在status")
        self.assertFalse(res_json["status"], "返回结果中的status不符合期望")
        self.assertIn("description", res_json, "返回结果中不存在description")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'), "错误描述不符合期望")
        self.assertIn("result", res_json, "返回结果中不存在result")

        for item in res_json["result"]:
            if item["parameter"] == "membId":
                self.assertEqual("不能为null", item["errMsg"].encode('utf-8'), "错误描述不符合期望")


if __name__ == "__main__":
    unittest.main()
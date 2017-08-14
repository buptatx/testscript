#coding=utf-8

"""
this module is used for query of member base info
author:zhangpeng
"""

import httpRequest
import json
import time
import unittest

class MembBaseModifyTestCase(unittest.TestCase):
    """
    test class for modify of member base info
    """
    def setUp(self):
        self.lejaneTest = httpRequest.HttpRequest()
        self.request_url = "http://192.168.8.212:15002/lejaneapp/lejane/usr/update/v1"
        #self.request_url = "http://http://lecanbo.sifude.com//lejaneapp/lejane/usr/update/v1"
        self.defaultMembId = 239

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

        query_url = "http://192.168.8.212:15002/lejaneapp/lejane/usr/detail/v1"
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
            org_data_json = json.loads(res)

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

    def testLevel1_noModify(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)

        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("更新会员基本档案成功", res_json["description"].encode('utf-8'),
                         "更新会员基本档案信息不符合期望")

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in org_base_info:
            if mkey != "updateTime":
                self.assertEqual(org_base_info[mkey], current_base_info[mkey])
            else:
                compare_ret = self.compareFormatTime(org_base_info["updateTime"], current_base_info["updateTime"])
                self.assertTrue(compare_ret, "更新时间异常")

    def testLevel1_allModify(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)
        org_sex = org_base_info["sex"]

        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["head"] = "1.jpg"
        httpbody["name"] = "测试鹏"
        httpbody["birthday"] = "2016-04-27"
        httpbody["height"] = 160.01
        httpbody["weight"] = 101.2
        if org_sex:
            httpbody["sex"] = 0
        else:
            httpbody["sex"] = 1
        httpbody["address"] = "河南省濮阳市中原油田测井公司"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("更新会员基本档案成功", res_json["description"].encode('utf-8'),
                         "更新会员基本档案信息不符合期望")

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        self.assertEqual(httpbody["membId"], current_base_info["membId"], "会员ID错误")
        self.assertEqual(httpbody["name"], current_base_info["name"].encode("utf-8"), "姓名更新错误")
        self.assertEqual(httpbody["head"], current_base_info["head"], "头像更新错误")
        self.assertEqual(httpbody["birthday"], current_base_info["birthday"], "生日更新错误")
        self.assertEqual(httpbody["height"], current_base_info["height"], "身高更新错误")
        self.assertEqual(httpbody["weight"], current_base_info["weight"], "体重更新错误")
        self.assertEqual(httpbody["sex"], current_base_info["sex"], "性别更新错误")
        self.assertEqual(httpbody["address"], current_base_info["address"].encode("utf-8"),
                         "地址更新错误")

        #compare_ret = self.compareFormatTime(start_time, current_base_info["updateTime"])
        #self.assertTrue(compare_ret, "更新时间错误")

    def testLevel1_address_length100(self):
        """
        test for address with length 100
        :return:None
        """
        # record org data
        org_base_info = self.infoQuery(self.defaultMembId)
        org_sex = org_base_info["sex"]

        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        if org_sex:
            httpbody["sex"] = 0
        else:
            httpbody["sex"] = 1
        httpbody["address"] = "我住在中华人民共和国我住在中华人民共和国我住在中华人民共和国" \
                              "我住在中华人民共和国我住在中华人民共和国我住在中华人民共和国" \
                              "我住在中华人民共和国我住在中华人民共和国我住在中华人民共和国" \
                              "我住在中华人民共和国"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)
        start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("更新会员基本档案成功", res_json["description"].encode('utf-8'),
                         "更新会员基本档案信息不符合期望")

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        self.assertEqual(httpbody["membId"], current_base_info["membId"], "会员ID错误")
        self.assertEqual(httpbody["sex"], current_base_info["sex"], "性别更新错误")
        self.assertEqual(httpbody["address"], current_base_info["address"].encode("utf-8"),
                         "地址更新错误")

    def testLevel1_onlymodifyname(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)

        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["name"] = "李二狗"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("更新会员基本档案成功", res_json["description"].encode('utf-8'),
                         "更新会员基本档案信息不符合期望")

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in org_base_info:
            if mkey != "updateTime":
                if mkey == "name":
                    self.assertEqual(httpbody["name"], current_base_info[mkey].encode("utf-8"), "姓名更新错误")
                else:
                    self.assertEqual(org_base_info[mkey], current_base_info[mkey])
            else:
                compare_ret = self.compareFormatTime(org_base_info["updateTime"], current_base_info["updateTime"])
                self.assertTrue(compare_ret, "更新时间异常")

    def testLevel1_onlymodifyhead(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)

        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["head"] = "2.jpg"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("更新会员基本档案成功", res_json["description"].encode('utf-8'),
                         "更新会员基本档案信息不符合期望")

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in org_base_info:
            if mkey != "updateTime":
                if mkey == "head":
                    self.assertEqual(httpbody["head"], current_base_info[mkey], "头像更新错误")
                else:
                    self.assertEqual(org_base_info[mkey], current_base_info[mkey])
            else:
                compare_ret = self.compareFormatTime(org_base_info["updateTime"], current_base_info["updateTime"])
                self.assertTrue(compare_ret, "更新时间异常")

    def testLevel1_modifyheadandname(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)

        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["head"] = "3.jpg"
        httpbody["name"] = "铁蛋"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("更新会员基本档案成功", res_json["description"].encode('utf-8'),
                         "更新会员基本档案信息不符合期望")

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in org_base_info:
            if mkey != "updateTime":
                if mkey == "head":
                    self.assertEqual(httpbody["head"], current_base_info[mkey], "头像更新错误")
                elif mkey == "name":
                    self.assertEqual(httpbody["name"], current_base_info[mkey].encode("utf-8"), "姓名更新错误")
                else:
                    self.assertEqual(org_base_info[mkey], current_base_info[mkey])
            else:
                compare_ret = self.compareFormatTime(org_base_info["updateTime"], current_base_info["updateTime"])
                self.assertTrue(compare_ret, "更新时间异常")

    def testLevel3_emptymembId(self):
        """
        test for empty value membId
        :return:None
        """
        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = ""
        httpbody["head"] = "3.jpg"
        httpbody["name"] = "铁蛋"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        #check response
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))

    def testLevel3_membId_0(self):
        """
        test for zero membId
        :return:None
        """
        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = 0
        httpbody["head"] = "0.jpg"
        httpbody["name"] = "铁蛋零"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        #check response
        self.assertEqual(0, res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertTrue(res_json["status"], "执行状态不符合期望：{}".format(res))

        # record current data
        current_base_info = self.infoQuery(0, 0)
        self.assertIsNone(current_base_info["result"], "查询结果不符合期望")
        self.assertTrue(current_base_info["status"], "查询结果失败")

    def testLevel3_membId_9999(self):
        """
        test for 9999 membId
        :return:None
        """
        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = 9999
        httpbody["head"] = "9999.jpg"
        httpbody["name"] = "铁蛋九"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        #check response
        self.assertEqual(0, res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertTrue(res_json["status"], "执行状态不符合期望：{}".format(res))

        # record current data
        current_base_info = self.infoQuery(9999, 0)
        self.assertTrue(current_base_info["status"], "查询结果失败")
        self.assertIsNone(current_base_info["result"], "查询结果不符合期望")

    def testLevel3_membId_miss(self):
        """
        test for no membId
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["head"] = "9999.jpg"
        httpbody["name"] = "铁蛋九"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("1005", res_json["code"], "错误码错误")
        self.assertEqual("缺少参数membId", res_json["description"].encode("utf-8"), "错误描述不符合期望")

    def testLevel3_name_9999(self):
        """
        test for name with value 9999
        :return:None
        """
        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["name"] = "9999"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        #check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "name":
                self.assertEqual("请输入2~4个汉字",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["name"], current_base_info["name"].encode("utf-8"), "查询结果失败")

    def testLevel3_name_onechar(self):
        """
        test for name with character
        :return:None
        """
        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["name"] = "刘"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "name":
                self.assertEqual("请输入2~4个汉字",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["name"], current_base_info["name"].encode("utf-8"), "查询结果失败")

    def testLevel3_name_fivechars(self):
        """
        test for name with five chars
        :return:None
        """
        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["name"] = "刘关张刘关"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "name":
                self.assertEqual("请输入2~4个汉字",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["name"], current_base_info["name"].encode("utf-8"), "查询结果失败")

    def testLevel3_name_charengnum(self):
        """
        test for name with char and eng and num
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["name"] = "刘1a2"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "name":
                self.assertEqual("请输入2~4个汉字",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["name"], current_base_info["name"].encode("utf-8"), "查询结果失败")

    def testLevel3_height_longfloat(self):
        """
        test for height with long float
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["height"] = 174.111

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "height":
                self.assertEqual("数字的值超出了允许范围(只允许在3位整数和2位小数范围内)",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["height"], current_base_info["height"], "查询结果失败")

    def testLevel3_weight_longfloat(self):
        """
        test for weight with long float
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["weight"] = 174.111

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "weight":
                self.assertEqual("数字的值超出了允许范围(只允许在3位整数和2位小数范围内)",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["weight"], current_base_info["weight"], "查询结果失败")

    def testLevel3_height_string(self):
        """
        test for string type height
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["height"] = "height"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "height":
                self.assertEqual("height参数输入类型错误",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["height"], current_base_info["height"], "查询结果失败")

    def testLevel3_weight_string(self):
        """
        test for string type weight
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["weight"] = "weight"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "weight":
                self.assertEqual("weight参数输入类型错误",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["weight"], current_base_info["weight"], "查询结果失败")

    def testLevel3_sex_2(self):
        """
        test for sex with value 2
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["sex"] = 2

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "sex":
                self.assertEqual("只能输入0或1(0 否 1 是)",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["sex"], current_base_info["sex"], "查询结果失败")

    def testLevel3_sex_string(self):
        """
        test for string type sex
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["sex"] = "sex"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "sex":
                self.assertEqual("sex参数输入类型错误",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["sex"], current_base_info["sex"], "查询结果失败")

    def testLevel3_name_num(self):
        """
        test for integer name
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["name"] = self.defaultMembId

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "name":
                self.assertEqual("请输入2~4个汉字",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["name"], current_base_info["name"], "查询结果失败")

    def testLevel3_membId_float(self):
        """
        test for float type membId
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = 3.1415926
        httpbody["name"] = "张日天"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        # check response
        self.assertIsNotNone(res_json["result"], "执行结果不符合期望：{}".format(res))
        self.assertFalse(res_json["status"], "执行状态不符合期望：{}".format(res))
        self.assertEqual("参数输入不合法", res_json["description"].encode("utf-8"))

        for item in res_json["result"]:
            if item["parameter"] == "membId":
                self.assertEqual("membId参数输入类型错误",
                                 item["errMsg"].encode("utf-8"))

        # record current data
        current_base_info = self.infoQuery(self.defaultMembId)
        self.assertNotEqual(httpbody["name"], current_base_info["name"].encode("utf-8"), "查询结果失败")

if __name__ == "__main__":
    unittest.main()
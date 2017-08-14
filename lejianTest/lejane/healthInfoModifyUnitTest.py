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

    def testLevel1_noModify(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)
        m_arcId = org_base_info["arcId"]
        m_habId = org_base_info["habId"]

        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["arcId"] = m_arcId
        httpbody["habId"] = m_habId

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(0, res_json["result"], "更新会员信息失败")
        self.assertNotIn("code", res_json, "返回结果不符合预期")
        self.assertEqual("更新0条数据", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in org_base_info:
            self.assertEqual(org_base_info[mkey], current_base_info[mkey])

    def testLevel1_arcModify(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)
        m_arcId = org_base_info["arcId"]
        #m_habId = org_base_info["habId"]

        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["arcId"] = m_arcId
        #httpbody["habId"] = m_habId
        httpbody["highPressure"] = 120
        httpbody["lowPressure"] = 100
        httpbody["booldFat"] = "血脂正常"
        httpbody["booldSugar"] = "血糖正常"
        httpbody["digestion"] = "消化不良"
        httpbody["urine"] = "便中带血"
        httpbody["sleep"] = "多梦"
        httpbody["tongue"] = "舌苔发白"
        httpbody["limbsTemp"] = "冬季指尖发凉"


        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("编辑健康档案成功", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in httpbody:
            if isinstance(httpbody[mkey], str):
                self.assertEqual(httpbody[mkey].decode("utf-8"), current_base_info[mkey])
            else:
                self.assertEqual(httpbody[mkey], current_base_info[mkey])

    def testLevel1_habModify(self):
        """
        test for correct process
        :return:None
        """
        #record org data
        org_base_info = self.infoQuery(self.defaultMembId)
        #m_arcId = org_base_info["arcId"]
        m_habId = org_base_info["habId"]

        #update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        #httpbody["arcId"] = m_arcId
        httpbody["habId"] = m_habId
        httpbody["isSmoke"] = 1
        httpbody["isDrink"] = 1
        httpbody["sleepHabbit"] = 1
        httpbody["isMidnight"] = 1
        httpbody["isNap"] = 1
        httpbody["isEatWell"] = 0
        httpbody["eatDescription"] = "湘潭小炒肉、苏州东坡肉、长沙红烧肉"
        httpbody["isMove"] = 1
        httpbody["moveDescription"] = "篮球"


        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        #check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertTrue(res_json["status"], "更新会员信息失败")
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("编辑健康档案成功", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in httpbody:
            if isinstance(httpbody[mkey], str):
                self.assertEqual(httpbody[mkey].decode("utf-8"), current_base_info[mkey])
            else:
                self.assertEqual(httpbody[mkey], current_base_info[mkey])

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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
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

    def testLevel1_arcHabModify_double(self):
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
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

        #again
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

    def testLevel3_Modify_abnormalpressure(self):
        """
        test for highPressure lower than lowPressure
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
        httpbody["highPressure"] = 78
        httpbody["lowPressure"] = 120
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数hightPressure的值必须大于参数lowPressure的值",
                         res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")
        self.assertEqual("2002", res_json["code"])

    def testLevel3_booldFat_lengthover20(self):
        """
        test for length of bloodFat over 20
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高血脂高血脂高血脂高血脂高血脂高血脂高血脂高血脂高血脂高"
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIn("result", res_json, "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "booldFat":
                self.assertEqual("字数在20字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_booldSugar_lengthover20(self):
        """
        test for bloodSugar length over 20
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高血糖高血糖高血糖高血糖高血糖高血糖高血糖高血糖高血糖高"
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "booldSugar":
                self.assertEqual("字数在20字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_digestion_lengthover20(self):
        """
        test for digestion length over 20
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差消化差消化差消化差消化差消化差消化差消化差消化差消化差消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "digestion":
                self.assertEqual("字数在20字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_urine_lengthover20(self):
        """
        test for urine length over 20
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天拉一天拉一天拉一天拉一天拉一天拉一天拉一天拉一天拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "urine":
                self.assertEqual("字数在20字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_sleep_lengthover20(self):
        """
        test for sleep length over 20
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来起不来起不来起不来起不来起不来起不来起不来起不来起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "sleep":
                self.assertEqual("字数在20字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_tongue_lengthover20(self):
        """
        test for tongue length over 20
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白发白发白发白发白发白发白发白发白发白发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "tongue":
                self.assertEqual("字数在20字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_limbsTemp_lengthover20(self):
        """
        test for limbsTemp length over 20
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热热热热热热热热热热热热热热热热热热热热热热热热热热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "limbsTemp":
                self.assertEqual("字数在20字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_isSmoke_2(self):
        """
        test for isSmoke set 2
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 2
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "isSmoke":
                self.assertEqual("只能输入0或1(0 否 1 是)",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_isDrink_2(self):
        """
        test for setting isDrink 2
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 2
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "isDrink":
                self.assertEqual("只能输入0或1(0 否 1 是)",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_sleepHabbit_2(self):
        """
        test for setting sleepHabbit 2
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂高"
        httpbody["booldSugar"] = "血糖高"
        httpbody["digestion"] = "消化差"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 2
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "sleepHabbit":
                self.assertEqual("只能输入0或1(0 否 1 是)",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_isMidnight_2(self):
        """
        test for setting isMidnight 2
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
        httpbody["lowPressure"] = 80
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
        httpbody["isMidnight"] = 2
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "isMidnight":
                self.assertEqual("只能输入0或1(0 否 1 是)",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_isNap_2(self):
        """
        test for setting isNap 2
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
        httpbody["lowPressure"] = 80
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
        httpbody["isNap"] = 2
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "isNap":
                self.assertEqual("只能输入0或1(0 否 1 是)",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_isEatWell_2(self):
        """
        test for setting isEatWell 2
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
        httpbody["lowPressure"] = 80
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
        httpbody["isEatWell"] = 2
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "isEatWell":
                self.assertEqual("只能输入0或1(0 否 1 是)",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_eatDescription_lengthover_100(self):
        """
        test for setting eatDescription length over 100
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
        httpbody["lowPressure"] = 80
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖"
        print httpbody["eatDescription"]
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "eatDescription":
                self.assertEqual("字数在100字以内",
                                 item["errMsg"].encode("utf-8"))

    def testLevel1_eatDescription_length_100(self):
        """
        test for setting eatDescription with 100 lenght
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
        httpbody["lowPressure"] = 80
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊" \
                                     "糖醋里脊糖醋里脊糖醋里脊糖醋里脊糖醋里脊"
        print httpbody["eatDescription"]
        httpbody["isMove"] = 0
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

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in httpbody:
            if isinstance(httpbody[mkey], str):
                self.assertEqual(httpbody[mkey].decode("utf-8"), current_base_info[mkey])
            else:
                self.assertEqual(httpbody[mkey], current_base_info[mkey])

    def testLevel3_isMove_4(self):
        """
        test for setting isMove 4
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
        httpbody["lowPressure"] = 80
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
        httpbody["isMove"] = 4
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "isMove":
                self.assertEqual("只能输入0 1 2 3;0 天天锻炼 1 经常 2 偶尔 3 很少",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_moveDescription_lengthover_100(self):
        """
        test for setting moveDescription length over 100
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
        httpbody["lowPressure"] = 80
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
        httpbody["isMove"] = 4
        httpbody["moveDescription"] = "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水" \
                                      "划"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "moveDescription":
                self.assertEqual("字数在100字以内",
                                 item["errMsg"].encode("utf-8"))
            if item["parameter"] == "isMove":
                self.assertEqual("只能输入0 1 2 3;0 天天锻炼 1 经常 2 偶尔 3 很少",
                                 item["errMsg"].encode("utf-8"))

    def testLevel1_moveDescription_length_100(self):
        """
        test for setting moveDescription with 100 lenght
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
        httpbody["lowPressure"] = 80
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        print httpbody["eatDescription"]
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水" \
                                      "划水划水划水划水划水划水划水划水划水划水"

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

    def testLevel3_highPressure_lengthover_3(self):
        """
        test for setting highPressure length over 3
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
        httpbody["highPressure"] = 1121
        httpbody["lowPressure"] = 80
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

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "highPressure":
                self.assertEqual("数字的值超出了允许范围(只允许在3位整数和0位小数范围内)",
                                 item["errMsg"].encode("utf-8"), "错误提示不符期望")

    def testLevel3_lowPressure_lengthover_3(self):
        """
        test for setting lowPressure length over 3
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
        httpbody["highPressure"] = 1121
        httpbody["lowPressure"] = 1111
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

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertEqual(0, res_json["result"], "更新会员信息失败")
        self.assertEqual("编辑健康档案失败", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

    def testLevel3_arcId_65535(self):
        """
        test for setting arcId 65535
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
        httpbody["arcId"] = 65535
        httpbody["habId"] = m_habId
        httpbody["highPressure"] = 112
        httpbody["lowPressure"] = 80
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
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("编辑健康档案成功", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

    def testLevel3_habId_65535(self):
        """
        test for setting habId 65535
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
        httpbody["habId"] = 65535
        httpbody["highPressure"] = 112
        httpbody["lowPressure"] = 80
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
        self.assertEqual(1, res_json["result"], "更新会员信息失败")
        self.assertEqual("编辑健康档案成功", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

    def testLevel3_arcId_habId_65535(self):
        """
        test for setting arcId and habId 65535
        :return:None
        """
        # update request
        httpheader = {}
        httpheader["Content-Type"] = "application/x-www-form-urlencoded"

        httpbody = {}
        httpbody["membId"] = self.defaultMembId
        httpbody["arcId"] = 65535
        httpbody["habId"] = 65535
        httpbody["highPressure"] = 112
        httpbody["lowPressure"] = 80
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
        self.assertEqual(0, res_json["result"], "更新会员信息失败")
        self.assertEqual("更新0条数据", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")
        self.assertNotIn("code", res_json, "响应数据结构错误")

    def testLevel1_without_highPressure(self):
        """
        test for update health data without highPressure
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
        httpbody["lowPressure"] = 80
        httpbody["booldFat"] = "血脂正常"
        httpbody["booldSugar"] = "血糖正常"
        httpbody["digestion"] = "消化可以的"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 1
        httpbody["isDrink"] = 0
        httpbody["sleepHabbit"] = 1
        httpbody["isMidnight"] = 0
        httpbody["isNap"] = 1
        httpbody["isEatWell"] = 0
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 1
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

        #record current data
        current_base_info = self.infoQuery(self.defaultMembId)

        for mkey in httpbody:
            if isinstance(httpbody[mkey], str):
                self.assertEqual(httpbody[mkey], current_base_info[mkey].encode('utf-8'))
            else:
                self.assertEqual(httpbody[mkey], current_base_info[mkey])

    def testLevel1_without_lowPressure(self):
        """
        test for update health data without lowPressure
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
        httpbody["highPressure"] = 130
        httpbody["booldFat"] = "血脂正常的"
        httpbody["booldSugar"] = "血糖正常的"
        httpbody["digestion"] = "消化可以"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 0
        httpbody["isDrink"] = 1
        httpbody["sleepHabbit"] = 0
        httpbody["isMidnight"] = 1
        httpbody["isNap"] = 0
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 1
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

    def testLevel1_without_booldFat(self):
        """
        test for update health data without booldFat
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
        httpbody["highPressure"] = 130
        httpbody["lowPressure"] = 100
        httpbody["booldSugar"] = "血糖健康"
        httpbody["digestion"] = "消化可以"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 1
        httpbody["isDrink"] = 1
        httpbody["sleepHabbit"] = 1
        httpbody["isMidnight"] = 1
        httpbody["isNap"] = 1
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 1
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

    def testLevel1_without_booldSugar(self):
        """
        test for update health data without booldSugar
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
        httpbody["highPressure"] = 130
        httpbody["lowPressure"] = 100
        httpbody["booldFat"] = "血脂健康"
        httpbody["digestion"] = "消化可以"
        httpbody["urine"] = "拉一天"
        httpbody["sleep"] = "起不来"
        httpbody["tongue"] = "发白"
        httpbody["limbsTemp"] = "热热热"
        httpbody["isSmoke"] = 1
        httpbody["isDrink"] = 1
        httpbody["sleepHabbit"] = 1
        httpbody["isMidnight"] = 1
        httpbody["isNap"] = 1
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 1
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

    def testLevel3_without_membId(self):
        """
        test for request without membId
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
        httpbody["arcId"] = m_arcId
        httpbody["habId"] = m_habId
        httpbody["highPressure"] = 120
        httpbody["lowPressure"] = 100
        httpbody["booldFat"] = "血脂正常"
        httpbody["booldSugar"] = "血糖正常"
        httpbody["digestion"] = "消化不良"
        httpbody["urine"] = "便中带血"
        httpbody["sleep"] = "多梦"
        httpbody["tongue"] = "舌苔发白"
        httpbody["limbsTemp"] = "冬季指尖发凉"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertIsNotNone(res_json["result"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "membId":
                self.assertEqual("不能为null",
                                 item["errMsg"].encode("utf-8"))

    def testLevel3_float_membId(self):
        """
        test for membId with float type
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
        httpbody["membId"] = 6.15
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
        httpbody["isEatWell"] = 1
        httpbody["eatDescription"] = "糖醋里脊"
        httpbody["isMove"] = 0
        httpbody["moveDescription"] = "划水"

        self.lejaneTest.createRequest(self.request_url, httpheader, httpbody)

        res = self.lejaneTest.sendRequest()

        # check response
        print "[res]{r}".format(r=res)
        res_json = json.loads(res)

        self.assertFalse(res_json["status"], "更新会员信息失败")
        self.assertEqual("参数输入不合法", res_json["description"].encode('utf-8'),
                         "编辑健康档案信息不符合期望")

        for item in res_json["result"]:
            if item["parameter"] == "membId":
                self.assertEqual("membId参数输入类型错误",
                                 item["errMsg"].encode("utf-8"))


if __name__ == "__main__":
    unittest.main()
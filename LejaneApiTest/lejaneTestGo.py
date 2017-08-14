#coding=utf-8

"""
this module is used for lejane interface function test
author:zhangpeng
"""

import baseInfoModifyUnitTest
import baseInfoQueryUnitTest
import healthInfoQueryUnitTest
import healthInfoModifyUnitTest
import syncContactTest
import unittest

def suite():
    baseinfo_query_suite = unittest.TestSuite()
    baseinfo_query_suite.addTest(baseInfoQueryUnitTest.MembBaseInfoTestCase("testLevel1_baseCheck"))
    baseinfo_query_suite.addTest(baseInfoQueryUnitTest.MembBaseInfoTestCase("testLevel2_stringmembId"))
    baseinfo_query_suite.addTest(baseInfoQueryUnitTest.MembBaseInfoTestCase("testLevel2_membId_0"))
    baseinfo_query_suite.addTest(baseInfoQueryUnitTest.MembBaseInfoTestCase("testLevel2_membId_9999"))
    baseinfo_query_suite.addTest(baseInfoQueryUnitTest.MembBaseInfoTestCase("testLevel2_floatmembId_214dot01"))
    baseinfo_query_suite.addTest(baseInfoQueryUnitTest.MembBaseInfoTestCase("testLevel3_missmembId"))
    baseinfo_query_suite.addTest(baseInfoQueryUnitTest.MembBaseInfoTestCase("testLevel3_emptymembId"))

    healthinfo_query_suite = unittest.TestSuite()
    healthinfo_query_suite.addTest(healthInfoQueryUnitTest.MembHealthInfoTestCase("testLevel1_healthCheck"))
    healthinfo_query_suite.addTest(healthInfoQueryUnitTest.MembHealthInfoTestCase("testLevel2_stringmembId"))
    healthinfo_query_suite.addTest(healthInfoQueryUnitTest.MembHealthInfoTestCase("testLevel2_membId_0"))
    healthinfo_query_suite.addTest(healthInfoQueryUnitTest.MembHealthInfoTestCase("testLevel2_membId_9999"))
    healthinfo_query_suite.addTest(healthInfoQueryUnitTest.MembHealthInfoTestCase("testLevel2_floatmembId_214dot01"))
    healthinfo_query_suite.addTest(healthInfoQueryUnitTest.MembHealthInfoTestCase("testLevel3_missmembId"))
    healthinfo_query_suite.addTest(healthInfoQueryUnitTest.MembHealthInfoTestCase("testLevel3_emptymembId"))

    baseinfo_modify_suite = unittest.TestSuite()
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel1_noModify"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel1_allModify"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel1_onlymodifyname"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel1_onlymodifyhead"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel1_modifyheadandname"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_emptymembId"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_membId_0"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_membId_9999"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_membId_miss"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_name_9999"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_name_onechar"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_name_fivechars"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_name_charengnum"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_height_longfloat"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_weight_longfloat"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_height_string"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_weight_string"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_sex_2"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_sex_string"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_name_num"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel3_membId_float"))
    baseinfo_modify_suite.addTest(baseInfoModifyUnitTest.MembBaseModifyTestCase("testLevel1_address_length100"))

    healthinfo_modify_suite = unittest.TestSuite()
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel1_noModify"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel1_arcModify"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel1_habModify"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel1_arcHabModify"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_arcHabModify_double"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
       "testLevel3_Modify_abnormalpressure"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
       "testLevel3_booldFat_lengthover20"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_booldSugar_lengthover20"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_digestion_lengthover20"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_urine_lengthover20"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_sleep_lengthover20"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_tongue_lengthover20"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_limbsTemp_lengthover20"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel3_isSmoke_2"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel3_isDrink_2"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel3_sleepHabbit_2"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel3_isMidnight_2"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel3_isNap_2"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel3_isEatWell_2"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_eatDescription_lengthover_100"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_eatDescription_length_100"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase("testLevel3_isMove_4"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_moveDescription_lengthover_100"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_moveDescription_length_100"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_highPressure_lengthover_3"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_moveDescription_length_100"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_arcId_65535"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_habId_65535"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_arcId_habId_65535"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_without_highPressure"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_without_lowPressure"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_without_booldFat"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel1_without_booldSugar"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_without_membId"))
    healthinfo_modify_suite.addTest(healthInfoModifyUnitTest.MembHealthModifyTestCase(
        "testLevel3_float_membId"))

    sync_contact_suite = unittest.TestSuite()
    sync_contact_suite.addTest(syncContactTest.MembContantSyncTestCase("testLevel3_sync_emptyJsonlist"))
    sync_contact_suite.addTest(syncContactTest.MembContantSyncTestCase("testLevel1_sync_oneRecord"))
    sync_contact_suite.addTest(syncContactTest.MembContantSyncTestCase(
        "testLevel1_sync_Records_withSameName"))


    test_all = unittest.TestSuite([
                                    baseinfo_query_suite,
                                    healthinfo_query_suite,
                                    baseinfo_modify_suite,
                                    healthinfo_modify_suite,
                                    sync_contact_suite
                                   ])

    return test_all


if __name__ == "__main__":
    myTestRunner = unittest.TextTestRunner()
    myTestRunner.run(suite())


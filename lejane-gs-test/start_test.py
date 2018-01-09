# -*- coding:utf-8 -*-

import time
import unittest

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutoTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '7.0'  # 设备系统版本
        desired_caps['deviceName'] = 'Philips X598'  # 设备名称
        desired_caps['appPackage'] = 'com.safety.act'  # APP包名
        desired_caps['appActivity'] = 'com.safety.act.MainPagerAct'  # APP启动activity
        # 模拟键盘输入
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def swipeLeft(self, t=500):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        self.driver.swipe(x1, y1, x2, y1, t)

    def get_gs_services_xpath(self, index):
        """获取国寿服务的xpath路径"""
        path_list = []
        path_list.append("//android.support.v4.view.ViewPager")
        path_list.append("/android.widget.RelativeLayout")
        path_list.append("/android.widget.ScrollView")
        path_list.append("/android.widget.LinearLayout")
        path_list.append("/android.widget.LinearLayout")
        path_list.append("/android.support.v7.widget.RecyclerView")
        path_list.append("/android.widget.RelativeLayout[@index={}]".format(index))

        return "".join(path_list)

    def get_loop_times(self):
        return 10

    def gs_service_loop_in_out(self, gsXpath):
        """循环进入返回国寿服务"""
        for i in range(0, self.get_loop_times()):
            print "[round {}]".format(i + 1)
            gsElement = self.driver.find_element_by_xpath(gsXpath)
            gsElement.click()

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.webkit.WebView')))
            self.driver.keyevent(4)
            time.sleep(3)

    def loop_run_gs_services(self, gsindex):
        """
        抽取测试用例中循环部分
        :param gsindex:
        :return:
        """
        print "[gs service id]{}".format(gsindex)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'iv_weather_icon')))
        self.swipeLeft()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'ly_recom_gs_arrow_down')))
        self.driver.find_element_by_id('ly_recom_gs_arrow_down').click()

        sgs_path = self.get_gs_services_xpath(gsindex)
        self.gs_service_loop_in_out(sgs_path)

    def test_case_Right_DoctorPhone(self):
        """
        右翻页点击国寿服务电话医生
        :return:
        """
        self.loop_run_gs_services(0)

    def test_case_Right_Guahao(self):
        """
        右翻页点击国寿服务自助挂号
        :return:
        """
        self.loop_run_gs_services(1)

    def test_case_Right_Jiuhu(self):
        """
        右翻页点击国寿服务急症救护
        :return:
        """
        self.loop_run_gs_services(2)

    def test_case_Right_Pinggu(self):
        """
        右翻页点击国寿服务健康风险评估
        :return:
        """
        self.loop_run_gs_services(3)

    def test_case_Right_Wenzhen(self):
        """
        右翻页点击国寿服务电话轻问诊
        :return:
        """
        self.loop_run_gs_services(4)

    def test_case_Right_Zhuanjia(self):
        """
        右翻页点击国寿服务找专家
        :return:
        """
        self.loop_run_gs_services(5)

    def test_case_Right_Jiuyi(self):
        """
        右翻页点击国寿服务境外就医
        :return:
        """
        self.loop_run_gs_services(6)

    def test_case_Right_Zice(self):
        """
        右翻页点击国寿服务健康自测
        :return:
        """
        self.loop_run_gs_services(7)

    def test_case_Right_Dangan(self):
        """
        右翻页点击国寿服务健康档案
        :return:
        """
        self.loop_run_gs_services(8)

    def test_case_Right_ServiceHistory(self):
        """
        右翻页点击国寿服务服务历史查询
        :return:
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'iv_weather_icon')))
        self.swipeLeft()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'ly_recom_gs_arrow_down')))
        self.driver.find_element_by_id('ly_recom_gs_arrow_down').click()

        for i in range(0, self.get_loop_times()):
            print "[round {}]".format(i + 1)
            self.driver.find_element_by_id("com.safety.act:id/ly_service_history").click()

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.webkit.WebView')))
            self.driver.keyevent(4)
            time.sleep(3)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AutoTest("test_case_Right_ServiceHistory"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
#!/usr/bin/env pyhon
# -*- coding=utf-8 -*-

import os
import time
import unittest

from appium import webdriver as awd


'''Return abs path relative to this file and not cwd'''
PATH = lambda p : os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'TCL 750'
        desired_caps['platformVersion'] = '6.0'

        desired_caps['app'] = PATH('D:\\Appnium-apk\\Lejane_v2.7.2_20170811T1055_p_on_philips_x598_en.apk')
        desired_caps['appPackage'] = 'com.safety.act'
        desired_caps['appActivity'] = 'com.safety.act.MainPagerAct'

        print "\n[APP PATH]{}".format(desired_caps['app'])
        self.driver = awd.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    # 获取屏幕宽和高
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 向左滑动
    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向右滑动
    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.1)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.9)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    def test_tap_xiaojian(self):
        self.driver.wait_activity("com.safety.act.MainPagerAct", 8)
        self.driver.tap([(500, 1500)], 1000)
        time.sleep(1)
        self.driver.tap([(500, 1500)], 1000)

        #for bug#5302
        time.sleep(1)
        self.driver.tap([(800, 1200)], 1000)

        time.sleep(3)
        self.driver.find_element_by_id("iv_xiaojian_icon").click()

        time.sleep(1.5)
        self.assertIsNotNone(self.driver.find_element_by_id('tv_login_numberidentify_failed_login'))
        self.driver.find_element_by_id('et_login_numberidentify_failed_phonenumber').send_keys("18301071270")
        time.sleep(0.5)
        self.driver.find_element_by_id('et_login_numberidentify_failed_authcode').send_keys('1111')
        self.driver.find_element_by_id('tv_login_numberidentify_failed_login').click()

        login_success = self.driver.find_element_by_id('tv_login_success_complete')
        self.assertIsNotNone(login_success)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
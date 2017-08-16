#!/usr/bin/env pyhon
# -*- coding=utf-8 -*-

import os
import time
import unittest

from appium import webdriver as awd

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Philips X598'
desired_caps['platformVersion'] = '7.0'

desired_caps['app'] = PATH('D:\\Appnium-apk\\Lejane_v2.7.2_20170811T1055_p_on_philips_x598_en.apk')
desired_caps['appPackage'] = 'com.safety.act'
desired_caps['appActivity'] = 'com.safety.act.MainPagerAct'

print desired_caps['app']

driver = awd.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id('adfasdf').click()
driver.quit()
#! -*- coding:utf-8 -*-

import Commontools.redistool
import Commontools.mySqlQuery
import Commontools.httpRequest

import unittest


class GSDHYSTestSuite(unittest.TestCase):
    def setUp(self):
        print("set Up")

    def tearDown(self):
        print("Tear Down")

    def test_caseOne(self):
        print("TestCase One")

    def test_caseTwo(self):
        print("TestCase Two")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(GSDHYSTestSuite("*caseTwo"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
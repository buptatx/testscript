# -*- coding:utf-8 -*-

import os
import sys
import time


class LejaneStressTest(object):
    def __init__(self):
        self.config_dict = {}
        self.getWorkConfig()

    def getWorkConfig(self):
        """
        用于读取monkey测试的config配置
        :return:config_dict
        """
        with open("./.config", "r") as fh:
            for line in fh:
                temp_list = line.strip().split(": ")
                if len(temp_list) != 2:
                    print "config error"
                    return

                if "phone" == temp_list[0]:
                    self.config_dict["phone"] = temp_list[1]
                elif "execount"  == temp_list[0]:
                    self.config_dict["execount"] = temp_list[1]
                elif "monkeyclickcount" == temp_list[0]:
                    self.config_dict["monkeyclickcount"] = temp_list[1]

        # set default params
        if "execount" not in self.config_dict:
            self.config_dict["execount"] = 1
        if "monkeyclickcount" not in self.config_dict:
            self.config_dict["monkeyclickcount"] = 10

        return

    def getAPKFullPath(self):
        """
        获取APK的全路径名
        :return:apkFullPath
        """
        apkFullPath = ""

        #获取当前文件路径及测试应用名称
        workpath = sys.path[0] + os.sep + "apk"

        for root, dirs, files in os.walk(workpath):
            #返回匹配到的第一个apk后缀的文件的全路径
            for name in files:
                if "apk" in name:
                    apkFullPath = workpath + os.sep + name
                    return apkFullPath
        return apkFullPath

    def installApk(self):
        """
        安装被测试应用包
        :return:
        """
        phoneAddr = self.config_dict.get("phone")
        print "start installing apk"

        apkFullPath = self.getAPKFullPath()

        if phoneAddr:
            installPhoneApk = "adb -s {} install -r {}".format(
                phoneAddr, apkFullPath)

            print "[adb cmd] {}".format(installPhoneApk)
            os.popen(installPhoneApk)

            print "install apk completed"

    def killTestAPP(self):
        """
        强制停止被测试的应用程序
        :return:
        """
        forceStopApp = "adb -s {} shell am force-stop com.safety.act".format(
            self.config_dict["phone"])
        print "[adb cmd] {}".format(forceStopApp)

        print "force stop lejane app start"
        os.popen(forceStopApp)
        print "force stop lejane app completed"

    def getBugreportFileName(self):
        """
        获取Bugreport文件名
        :return:
        """
        filename = "bugreport_{}.txt".format(int(time.time()))
        return sys.path[0] + os.sep + "bugreport_out" \
            + os.sep + "data" + os.sep + filename

    def createBugreport(self):
        """
        生成测试报告
        :return:
        """
        bugreport_file = self.getBugreportFileName()

        print "create bugreport start"
        bugreport = "adb -s {} shell bugreport > {}".format(
            self.config_dict["phone"], bugreport_file)
        os.popen(bugreport)
        print "create bugreport complete"

        print "chkbugreport start"
        chkbugreport = "java -jar {}\\chkbugreport-0.4-185.jar {}".format(
            sys.path[0], bugreport_file)
        os.popen(chkbugreport)
        print "chkbugreport complete"

    def fullMonkey(self):
        """
        运行monkey测试
        :return:
        """
        #强制停止待测app
        self.killTestAPP()

        openlejane = "adb -s {} shell am start com.safety.act/.MainPagerAct".format(
            self.config_dict["phone"])
        print "[adb cmd] {}".format(openlejane)
        os.popen(openlejane)
        
        monkeycmd = "adb -s {} shell monkey -p com.safety.act "\
            "--ignore-timeouts --ignore-crashes "\
            "--pct-touch 35 --pct-syskeys 30 --pct-appswitch 35 "\
            "--throttle 1000 -v -v -v {}".format(
            self.config_dict["phone"], self.config_dict["monkeyclickcount"])
        print "[adb cmd] {}".format(monkeycmd)
        os.popen(monkeycmd)

    def execMonkey(self):
        """
        执行Monkey测试
        :return:
        """
        if len(self.config_dict) != 3:
            print "no sdev in config file"
            return

        self.installApk()

        for i in range(int(self.config_dict["execount"])):
            print "execute monkey, loop={}".format(i + 1)
            self.fullMonkey()
            time.sleep(3)

        self.createBugreport()
        print "monkey test completed"

        raw_input("press anykey to close")

if __name__ == "__main__":
    test = LejaneStressTest()
    test.execMonkey()
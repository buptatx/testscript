# -*- coding:utf-8 -*-

import time


def get_current_timestamp():
    return long(time.time() * 100)


class HdTest:
    def __init__(self):
        pass

    def get_user_choise(self):
        user_info = "请输入您想测试的API_ID:\r\n1.疾病症状搜索\r\n2.症状搜索关联病和症状4" \
                    "\r\n3.根据疾病ID获取疾病检查和科室详情\r\n".decode("utf-8")

        user_choise = int(raw_input(user_info))

        if user_choise != 1 and user_choise !=2 and user_choise != 3:
            print "请重新选择".decode("utf-8")
            self.get_user_choise()
        else:
            print "您选择的API_ID为:%d".decode("utf-8") % user_choise

        return user_choise


if __name__ == "__main__":
    print get_current_timestamp()

    test = HdTest()
    test.get_user_choise()
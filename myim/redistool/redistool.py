#!/usr/bin/env python
#!coding=utf-8


import redis


class MyRedisTool:
    def __init__(self, mhost, mport, myauth):
        self.mredis = redis.Redis(host=mhost, port=mport, password=myauth, db=5)

    def showkeys(self):
        """
        获取redis中现有的全部的key
        :return:null
        """
        mkeys = self.mredis.keys()
        mkeys.sort()
        i = 0
        for item in mkeys:
            print "[{}]{}".format(i, item)
            i += 1

    def setvalue(self, key, value):
        """
        设置redis中特定key的value
        :param key: in 待设置的键
        :param value: out 待设置的键的值
        :return: null
        """
        self.mredis.set(key, value)

    def refresh_sms_ttl(self, phone):
        """
        刷新生存期 默认1800s（30*60s）
        :param phone: 获取验证码的手机的手机号
        :return:null
        """
        self.mredis.setex('sms_code_cache_key_3_{}'.format(phone), 1111, 1800)

    def delete_key(self, key):
        """
        删除单独的key
        :param key: 需要删除的key
        :return: null
        """
        self.mredis.delete(key)

    def batch_delete_keys(self, keyword):
        """
        批量删除
        :param keyword: 正则表达式的关键字
        :return: null
        """
        keys = self.mredis.keys(r"*{}*".format(keyword))
        for item in keys:
            print item
        self.mredis.delete(*keys)

    def get_key(self, key):
        """
        获取特定的key的value
        :param key: 特定的key
        :return:
        """
        value = self.mredis.get(key)
        print "[{}]{}".format(key, value)

    def test(self):
        print self.mredis.dbsize()
        keys = self.mredis.keys(r"*doct*")
        for item in keys:
            print item


if __name__ == "__main__":
    mr = MyRedisTool('192.168.8.213', 6379, 'sfd@2015')
    #mr.showkeys()
    #mr.setvalue('sms_code_cache_key_3_18301071270', 1111)
    #mr.setvalue('sms_code_cache_key_3_15811330069', 1111)
    #mr.setvalue('sms_code_cache_key_5_18301071270', 1111)
    #mr.setvalue('sms_code_cache_key_3_15810537243', 1111)
    #mr.setvalue('sms_code_cache_key_3_13161269249', 1111)
    mr.refresh_sms_ttl('18301071270')
    #mr.get_key('sms_code_cache_key_3_13161269249')
    #mr.delete_key('AnswerDao')
    #mr.test()
    #mr.batch_delete_keys("info")
    #mr.test()
    #mr.refresh_sms_ttl('18301071270')
    #mr.refresh_sms_ttl('13161269249')
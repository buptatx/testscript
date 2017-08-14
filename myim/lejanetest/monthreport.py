#!/usr/bin/env python
#!coding=utf-8


import json
import MySQLdb


class DataReport():
    def __init__(self, host, user, pwd, db):
        self.db_cnt = MySQLdb.connect(host, user, pwd, db, charset='utf8')
        self.cursor = self.db_cnt.cursor()
        self.app = {}
        self.articles = []
        self.articles_count = 0
        self.healthplan = []
        self.healthplan_count = 0
        self.tips = {}
        self.total_tips_count = 0

    def execute_sql(self, msql):
        self.cursor.execute(msql)
        results = self.cursor.fetchall()
        return results

    def get_report_data(self, uid, sdate, edate):
        msql = "select * from tbl_usr_health_data where uid={} AND data_time < {} AND data_time >= {}"\
            .format(uid, edate, sdate)
        results = self.execute_sql(msql)
        return results

    def cal_top_app(self, appcount):
        if len(appcount) == 0:
            return

        for item in appcount:
            if item['key'] in self.app:
                self.app[item['key']] += 1
            else:
                self.app[item['key']] = int(item['value'])

    def get_top_4_apps(self):
        sorted_app_set = sorted(self.app.items(), key=lambda item:item[1], reverse=True)
        print '==========APPCOUNT=========='
        top_len = 4

        if len(sorted_app_set) == 0:
            print 'NO FAVOURITE APP DATA'
            return
        elif len(sorted_app_set) < 4:
            top_len = len(sorted_app_set)

        for i in range(0,top_len):
            print "[TOP{} Favourite APP]{} [Used {} Times]"\
                .format(i + 1, sorted_app_set[i][0], sorted_app_set[i][1])

    def cal_articles(self, articles):
        if len(articles) == 0:
            return

        for item in articles:
            if item == "null":
                continue

            if str(item) not in self.articles:
                self.articles.append(str(item))

            self.articles_count += 1

    def get_articles_info(self):
        print "==========ARTICLES=========="
        if self.articles_count == 0:
            print "NO ARTICLE READ DATA"
            return

        print "[READ COUNTS]{}".format(self.articles_count)
        print "[READ DETAILS]",
        for item in self.articles: print item,
        print ""
        self.get_article_tags()

    def get_article_tags(self):
        db_c = MySQLdb.connect('192.168.8.213', 'lejane', 'lejane2017', 'lejane', charset='utf8')
        cursor = db_c.cursor()
        print self.articles
        mysql = "SELECT tag_id from tbl_article_tag_lnk where info_id in ({})"\
            .format(",".join(self.articles))
        cursor.execute(mysql)
        results = cursor.fetchall()

        temp_dict = {}
        for item in results:
            if item in temp_dict:
                temp_dict[item] += 1
            else:
                temp_dict[item] = 1

        sorted_temp_result = sorted(temp_dict.items(), key=lambda item:item[1], reverse=True)

        top_num = 3
        if len(sorted_temp_result) < 3:
            top_num = len(sorted_temp_result)

        temp_list = []
        for idx in range(0, top_num):
            temp_list.append(str(int(sorted_temp_result[idx][0][0])))

        mysql = "SELECT tag_name from tbl_sys_tag where tag_id in ({})".format(",".join(temp_list))
        cursor.execute(mysql)
        results = cursor.fetchall()

        print "[TOP {} TAGS]".format(top_num),
        temp_tag_list = []
        for item in results:
            temp_tag_list.append(item[0])
            print item[0],
        print ""

        db_c.close()

    def cal_healthplan(self, results):
        if len(results) == 0:
            return

        for item in results:
            if item == "null":
                continue

            if item not in self.healthplan:
                self.healthplan.append(item)

            self.healthplan_count += 1

    def get_healthplan_info(self):
        print "==========HEALTHPLAN=========="
        if self.healthplan_count == 0:
            print "NO HEALTHPLAN PRACTISE DATA"
            return

        print "[HEALTHPLAN PRACTISE COUNTS]{}".format(self.healthplan_count)
        print "[HEALTHPLAN PRACTISE DETAILS]",
        for item in self.healthplan : print item,
        print ""

    def parse_report(self, results):
        usr_data = []

        for item in results:
            usr_data.append(item[3])

        for item in usr_data:
            temp = json.loads(item)
            print temp

            self.cal_healthplan(temp['healthCourse'])
            self.cal_top_app(temp['appCount'])
            self.cal_articles(temp['articles'])
            self.cal_tipcount(temp['weakTipsCount'], temp['forceTipsCount'])
            self.cal_total_tipcount(temp['weakTipsCount'], temp['forceTipsCount'], temp['olaCount'])

        self.get_healthplan_info()
        self.get_top_4_apps()
        self.get_articles_info()
        self.get_tipcount_info()

    def close(self):
        self.db_cnt.close()

    def get_total_steps(self, uid, sdate, edate):
        db_c = MySQLdb.connect('192.168.8.213', 'lejane', 'lejane2017', 'lejane')
        cursor = db_c.cursor()
        mysql = "select SUM(steps) from tbl_user_daily_info where uid={} AND upload_date > {} AND upload_date <= {}".\
            format(uid, sdate, edate)
        cursor.execute(mysql)
        results = cursor.fetchall()
        print "==========TOTALSTEPS=========="
        print "[TOTAL STEPS]{}".format(results[0][0])
        db_c.close()

    def cal_tipcount(self, weaktip, forcetip):
        if len(weaktip) == 0 and len(forcetip) == 0:
            return

        if len(weaktip):
            for item in weaktip:
                cur_weak_key = "weak_%s" % item['key']

                if cur_weak_key not in self.tips.keys():
                    self.tips[cur_weak_key] = int(item['value'])
                else:
                    self.tips[cur_weak_key] = int(self.tips[cur_weak_key]) + int(item['value'])

        if len(forcetip):
            for item in forcetip:
                cur_force_key = "force_%s" % item['key']

                if cur_force_key not in self.tips.keys():
                    self.tips[cur_force_key] = int(item['value'])
                else:
                    self.tips[cur_force_key] = int(item['value']) + int(self.tips[cur_force_key])

        return

    def get_tipcount_info(self):
        print "==========TIPCOUNT=========="
        print "[TOTAL OLA COUNT]{}".format(self.total_tips_count)

        sorted_tips = sorted(self.tips.items(), key=lambda d:d[1], reverse=True)

        if len(sorted_tips) > 3:
            sorted_tips_num = 3
        else:
            sorted_tips_num = len(sorted_tips)

        for i in range(0, sorted_tips_num):
            print "[TOP{}]type{}:count{} ".format(i+1, sorted_tips[i][0], sorted_tips[i][1])
        print ""

    def cal_total_tipcount(self, weaktip, forcetip, olacount):
        if len(weaktip) != 0:
            for item in weaktip:
                self.total_tips_count += int(item["value"])

        if len(forcetip) != 0:
            for item in forcetip:
                self.total_tips_count += int(item["value"])

        self.total_tips_count += int(olacount)

    def do_parse_report(self, uid, sdate, edate):
        results = self.get_report_data(uid, sdate, edate)
        self.get_total_steps(uid, sdate, edate)
        self.parse_report(results)
        self.close()


if __name__ == "__main__":
    mr = DataReport('192.168.8.213', 'sifude', 'sifude@2015', 'zeroonetest')
    #mr.do_parse_report('4001002', '20170601', '20170630')
    mr.do_parse_report('4001001', '20170807', '20170813')
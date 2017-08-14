#coding=utf-8

"""
script for delete member-info from lejane-sql
"""

import MySQLdb

class MySqlExecuter():
    """
    class for execute mysql-script
    """
    def __init__(self, host, uname, upasswd, utable):
        self.myScript = ""
        self.host = host
        self.uname = uname
        self.upasswd = upasswd
        self.utable = utable

    def setMyScript(self, myScript):
        self.myScript = myScript

    def executer(self, myScript):
        db = MySQLdb.connect(self.host, self.uname, self.upasswd, self.utable)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        try:
            # 执行sql语句
            cursor.execute(myScript)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
        # 关闭数据库连接
        db.close()

    def selector(self, myScript):
        db = MySQLdb.connect(self.host, self.uname, self.upasswd, self.utable)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute(myScript)
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()
        print "MemId : %s " % data
        # 关闭数据库连接
        db.close()

        return data

    def getMemId(self, uphone):
        myScriptList = []
        myScriptList.append("select memb_id from tbl_usr_member")
        myScriptList.append("where phone = {} and record_status = 0;".format(uphone))
        myScript = " ".join(myScriptList)

        myMembId = self.selector(myScript)
        return myMembId

    def deleteMember(self, uphone):

        myMembId = self.getMemId(uphone)

        myScriptList = []
        myScriptList.append("delete from tbl_usr_archives where memb_id = %s;" % myMembId)
        myScriptList.append("delete from tbl_usr_call where memb_id = %s;" % myMembId)
        myScriptList.append("delete from tbl_usr_check_problem where memb_id = %s;" % myMembId)
        myScriptList.append("delete from tbl_usr_habbit where memb_id = %s;" % myMembId)
        myScriptList.append("delete from tbl_lnk_usr_app where memb_id = %s;" % myMembId)
        myScriptList.append("delete from tbl_usr_read where memb_id = %s;" % myMembId)
        myScriptList.append("delete from tbl_lnk_member_device where memb_id = %s;" % myMembId)
        myScriptList.append("delete from tbl_usr_card where phone = %s;" % uphone)
        myScriptList.append("delete from tbl_lnk_usr_album where phone = %s;" % myMembId)
        myScriptList.append("delete from tbl_usr_member where memb_id = %s;" % myMembId)

        for item in myScriptList:
            print item
            self.executer(item)


def main():
    #offline
    mydeleter = MySqlExecuter("192.168.8.213", "sifude", "sifude@2015", "lecanbotest")
    #online
    #mydeleter = MySqlExecuter("125.208.26.21", "lecanbo", "lecanbo@2015", "lecanbo")
    #mydeleter.deleteMember("13161269249")
    #mydeleter.deleteMember("15810359712")
    #mydeleter.deleteMember("15811330069")
    #mydeleter.deleteMember("13911486420")
    #mydeleter.deleteMember("13716759158")
    mydeleter.deleteMember("15810537243")
    #mydeleter.deleteMember("15810359651")
    #mydeleter.deleteMember("13011825077")
    #mydeleter.deleteMember("15810359712")
    #mydeleter.deleteMember("13911486420")
    print "hello world"


if __name__ == "__main__":
    main()
#coding=utf-8

"""
script for batch register child into posteritytest tbl_usr_child
"""

import MySQLdb
import datetime

import queryChildPhone

class MySqlInsertExecuter():
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
        except Exception as e:
            print "query failed with {}".format(str(e))
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

    def registerChild(self, phoneList):
        mypasswd = "df10ef8509dc176d733d59549e7dbfaf"

        for item in phoneList:
            print item
            account = item
            phone = item

            myscriptList = []
            myscriptList.append("insert into")
            myscriptList.append("tbl_usr_child (account, phone, password, create_time)")
            myscriptList.append("values ('%s'," % account)
            myscriptList.append("'%s'," % phone)
            myscriptList.append("'%s'," % mypasswd)
            myscriptList.append("'%s')" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            myscript = " ".join(myscriptList)
            print myscript
            self.executer(myscript)


def main():
    #query childPhone
    #offline
    myQueryer = queryChildPhone.MySqlExecuter("192.168.8.213", "sifude", "sifude@2015", "lecanbotest")
    #online
    #myQueryer = MySqlExecuter("125.208.26.21", "lecanbo", "lecanbo@2015", "lecanbo")
    childPhoneList = myQueryer.queryChildPhone(261)

    #offline
    myRegister = MySqlInsertExecuter("192.168.8.213", "sifude", "sifude@2015", "posteritytest")
    #online
    #myRegister = MySqlExecuter("125.208.26.21", "lecanbo", "lecanbo@2015", "lecanbo")
    myRegister.registerChild(childPhoneList)


if __name__ == "__main__":
    main()
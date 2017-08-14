#coding=utf-8

"""
script for batch insert child into lecanbotest tbl_lnk_usr_child
"""

import MySQLdb
import random
import datetime

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

    def randomNumString(self, length):
        """
        return random number string of special length
        :param length: random number string length
        :return: random number string
        """
        numStringList = []

        numStringList.append(str(1))
        for idx in range(0, length-1):
            numStringList.append(str(random.randint(0,9)))

        numString = "".join(numStringList)
        return numString

    def createChild(self, length):

        parentPhone = "15810359651"
        parent_memb_id = 261

        for count in range(0, 5000):
            numberString = self.randomNumString(length)
            phone = numberString
            name = numberString

            myscriptList = []
            myscriptList.append("insert into")
            myscriptList.append("tbl_lnk_usr_child (memb_id, memb_phone, child_phone, contact_name, create_time)")
            myscriptList.append("values (%s," % parent_memb_id)
            myscriptList.append("%s," % parentPhone)
            myscriptList.append("%s," % phone)
            myscriptList.append("%s," % name)
            myscriptList.append("'%s')" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            myscript = " ".join(myscriptList)
            print myscript
            self.executer(myscript)


def main():
    #offline
    myInsert = MySqlExecuter("192.168.8.213", "sifude", "sifude@2015", "lecanbotest")
    #online
    #myInsert = MySqlExecuter("125.208.26.21", "lecanbo", "lecanbo@2015", "lecanbo")
    myInsert.createChild(11)


if __name__ == "__main__":
    main()
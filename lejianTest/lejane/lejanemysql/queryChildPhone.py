#coding=utf-8

"""
script for query childId of special parent
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
        records = []

        try:
            # 执行sql语句
            cursor.execute(myScript)
            results = cursor.fetchall()

            for record in results:
                phone = record[0]
                if len(phone) == 11:
                    records.append(phone)
        except Exception as e:
            print "query failed with {}".format(str(e))

        # 关闭数据库连接
        db.close()

        return records

    def executerPath(self, myScript):
        db = MySQLdb.connect(self.host, self.uname, self.upasswd, self.utable)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        records = []

        try:
            # 执行sql语句
            cursor.execute(myScript)
            results = cursor.fetchall()

            for record in results:
                photopath = record[0]
                records.append(photopath)
        except Exception as e:
            print "query failed with {}".format(str(e))

        # 关闭数据库连接
        db.close()

        return records

    def selector(self, myScript):
        db = MySQLdb.connect(self.host, self.uname, self.upasswd, self.utable, charset="utf8")
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

    def queryChildPhone(self, membId):
        myScript = "select child_phone from tbl_lnk_usr_child where memb_id=%d" % membId

        print myScript
        res = self.executer(myScript)
        return res

    def queryPicsPath(self, mincid, maxcid):
        min_child_id = mincid
        max_child_id = maxcid
        myScriptList= []
        myScriptList.append("select photo_path from tbl_lnk_album_photo")
        myScriptList.append("Join tbl_lnk_child_album on")
        myScriptList.append("tbl_lnk_album_photo.album_id=tbl_lnk_child_album.album_id")
        myScriptList.append("where tbl_lnk_child_album.child_id>=%d" % min_child_id)
        myScriptList.append("and tbl_lnk_child_album.child_id<=%d" % max_child_id)

        myScript = " ".join(myScriptList)
        print myScript
        res = self.executerPath(myScript)
        return res


def main():
    #offline
    #myQueryer = MySqlExecuter("192.168.8.213", "sifude", "sifude@2015", "lecanbotest")
    myQueryer = MySqlExecuter("192.168.8.213", "sifude", "sifude@2015", "posteritytest")
    #online
    #myQueryer = MySqlExecuter("125.208.26.21", "lecanbo", "lecanbo@2015", "lecanbo")
    #res = myQueryer.queryChildPhone(261)
    res = myQueryer.queryPicsPath(24, 5034)

    # with open("childPhone.txt", "w+") as fhandle:
    #     for item in res:
    #         fhandle.write("%s\n" % item)


if __name__ == "__main__":
    main()
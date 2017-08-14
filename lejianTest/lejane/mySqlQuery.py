#coding=utf-8

"""
author :zhangpeng@sifude.com
"""

import MySQLdb

def myQuery(mquery):
    """
    execute mysql query and return result list
    :param mquery: mysql query
    :return: result list
    """
    host = "192.168.8.213"
    user = "sifude"
    passwd = "sifude@2015"
    db = "lecanbotest"

    db_connector = MySQLdb.connect(host, user, passwd, db, charset="utf8")
    cursor = db_connector.cursor()

    item = {}
    records = []

    try:
        cursor.execute(mquery)
        results = cursor.fetchall()

        for record in results:
            item["con_id"] = record[0]
            item["memb_id"] = record[1]
            item["name"] = record[2]
            item["phone"] = record[3]
            item["type"] = record[4]
            item["create_time"] = record[5]
            records.append(item.copy())

    except Exception as e:
        print "query failed with {}".format(str(e))

    cursor.close()
    return records


def membContactQuery(membId):
    """
    query in tbl_usr_contact with special membId
    :param membId: query membID
    :return: result list
    """
    mquery = "select * from tbl_usr_contact where memb_id={}".format(membId)

    ret = myQuery(mquery)
    return ret


def main():
    ret = membContactQuery(214)
    for item in ret:
        print item


if __name__ == "__main__":
    main()
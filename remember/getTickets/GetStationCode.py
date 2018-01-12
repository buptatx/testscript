#! -*- coding:utf-8 -*-

"""
查询城市CODE
"""


class GetStationCode():
    def __init__(self):
        self.station_version = "1.9044"
        self.station_names = self.loadStationNames()
        self.station_dict = {}
        self.getStationDict()

    def loadStationNames(self):
        """
        从station_names文件中获取数据
        :return:station_names中的原数据
        """
        with open("station_names.txt", "rb") as mf:
            content = mf.readline()
        return content.strip()

    def getStationCode(self, cName):
        return self.station_dict[cName]

    def getStationDict(self):
        """
        数据整理成以城市名为key的字典
        :return: null
        """
        tmp_list = self.station_names[1:].split("@")
        for item in tmp_list:
            item_list = item.split("|")
            self.station_dict[item_list[1]] = item_list[2]


if __name__ == "__main__":
    test = GetStationCode()
    print test.getStationCode("北京西")
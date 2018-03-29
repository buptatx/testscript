#! -*- coding:utf-8 -*-

import re
import xlrd
import Levenshtein


def calculate_accuracy(expect, actual):
    """
    计算actual距离expect的编辑距离，计算得到的识别字准确率
    :param expect: 期望识别结果
    :param actual: 实际识别结果
    :return: 准确率= 1-编辑距离/expect的字符串的长度
    """
    distance = Levenshtein.distance(expect, actual)
    distance_rate = float(distance)/len(expect)
    accuracy_rate = 1 - distance_rate
    return accuracy_rate


def number_normalize(original):
    """
    对数字做归一化处理，将阿拉伯数字转化为中国小写
    :param original:
    :return:
    """
    num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    result = original

    for i in range(len(num)):
        if str(i) in original:
            result = re.sub(str(i).decode("utf-8"), num[i].decode("utf-8"), result)
    return result


def data_clean(original):
    """
    数据清理
    :param original:原始字符串
    :return: 符号清理后的字符创
    """
    #将运算符+号转换为中文“加上”
    step_1 = re.sub("\+".decode("utf-8"), "加上".decode("utf-8"), original)
    #将运算符=号转化为中文“等于”
    step_2 = re.sub("=".decode("utf-8"), "等于".decode("utf-8"), step_1)
    #将运算符*号转化为中文“乘以”
    step_3 = re.sub("\*".decode("utf-8"), "乘以".decode("utf-8"), step_2)
    result = re.sub("[\s+\.\!\/_,$%(\"\']+|[——！，。？、~@#￥%……&（）]+".decode("utf8"), "".decode("utf8"),
                    step_3)

    return number_normalize(result)


def data_clean_punctuation(original):
    """
    数据清理，只清理中文标点，。！？、
    :param original:原始字符串
    :return: 符号清理后的字符创
    """
    result = re.sub("[——！，。？、~@#￥%……&（）]+".decode("utf8"), "".decode("utf8"),
                    original)

    return result


def cal_accuracy(data_list, doNormalize):
    """
    计算准确率
    :param data_list:数据 expect:期望 xf_recog:讯飞识别结果， bd_recog:百度识别结果
    :param doNormalize:是否执行数据清理
    :return:
    """
    xf_recog_acc_total = 0
    bd_recog_acc_total = 0

    for item in data_list:
        if doNormalize == 0:
            expect = data_clean_punctuation(item["expect"])
            xf_recog = data_clean_punctuation(item["xf_recog"])
            bd_recog = data_clean_punctuation(item["bd_recog"])
        elif doNormalize == 1:
            expect = data_clean(item["expect"])
            xf_recog = data_clean(item["xf_recog"])
            bd_recog = data_clean(item["bd_recog"])
        else:
            expect = item["expect"]
            xf_recog = item["xf_recog"]
            bd_recog = item["bd_recog"]

        xf_recog_accuracy = calculate_accuracy(expect, xf_recog)
        bd_recog_accuracy = calculate_accuracy(expect, bd_recog)
        xf_recog_acc_total += xf_recog_accuracy
        bd_recog_acc_total += bd_recog_accuracy
        tmp_result = "[expect]%s[xf:%f]%s[bd:%f]%s" % (expect, xf_recog_accuracy, xf_recog, bd_recog_accuracy, bd_recog)
        print(tmp_result)
    xf_recog_acc_avg = xf_recog_acc_total / (len(data_list))
    bd_recog_acc_avg = bd_recog_acc_total / (len(data_list))
    print("[{}][xf]{}[bd]{}".format(doNormalize, xf_recog_acc_avg, bd_recog_acc_avg))


def load_data(filename):
    """
    从excel文件中加载识别结果与期望
    :param filename:数据文件路径
    :return:期望及识别结果列表
    """
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    recog_data = []

    for idx in range(1, table.nrows):
        tmp = table.row_values(idx)
        item = {}
        item["expect"] = tmp[0]
        item["xf_recog"] = tmp[1]
        item["bd_recog"] = tmp[3]
        item["xf_cost"] = tmp[2]
        item["bd_cost"] = tmp[4]
        recog_data.append(item)

    return recog_data


def cal_cost(orig_data):
    xf_rps_total = 0
    bd_rps_total = 0

    for item in orig_data:
        char_len = len(item["expect"]) - 1
        xf_cost = int(item["xf_cost"])
        bd_cost = int(item["bd_cost"])
        xf_recog_per_s = float(char_len) / xf_cost
        bd_recog_per_s = float(char_len) / bd_cost
        xf_rps_total += xf_recog_per_s
        bd_rps_total += bd_recog_per_s
        print("[expect]%s[len]%s[xfrps]%f[bdrps]%f" % (item["expect"], char_len, xf_recog_per_s, bd_recog_per_s))
    xf_rps_avg = xf_rps_total / len(orig_data)
    bd_rps_avg = bd_rps_total / len(orig_data)
    print("[xfrps_avg]%f[bdrps_avg]%f" % (xf_rps_avg, bd_rps_avg))

def cal_acc_entrance(filename):
    orig_data = load_data(filename)

    cal_accuracy(orig_data, 0)
    cal_accuracy(orig_data, 1)
    cal_cost(orig_data)


if __name__ == "__main__":
    cal_acc_entrance("./data/test.xlsx")
#! -*- coding:utf-8 -*-

import base64
import sys


def xor(inStr, magicNum):
    """
    XOR加密
    :param inStr:待加密字符串
    :param magicNum: 加密用种子
    :return: 返回加密串
    """
    temp_list = []
    for i in inStr:
        temp_list.append(chr(ord(i)^magicNum))

    return "".join(temp_list)


def xj_decrypt(destStr, magicNum):
    """
    解密函数体-base64解密-xor解密-base64解密
    :param destStr:待解密串
    :param magicNum:解密用秘钥
    :return:解密结果
    """
    temp_dest = base64.urlsafe_b64decode(destStr)
    xor_result = xor(temp_dest, magicNum)
    return base64.urlsafe_b64decode(xor_result)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: decrypt destStr magicNumber"
    else:
        res = xj_decrypt(sys.argv[1], int(sys.argv[2]))
        print unicode(res, "utf-8").encode("gbk")
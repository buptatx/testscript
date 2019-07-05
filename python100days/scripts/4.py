#！ -*- coding:utf-8 -*-

"""
循环
"""

from math import sqrt


def isPrimeNumber(x):
    """
    判断一个输入是否是素数
    :param x:
    :return:
    """
    if not isinstance(x, int):
        return False

    if x < 2:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True


def test_isPrimeNumber():
    test_set = {10:False, 3:True, 5:True, 1:False, 1.1:False, 'test':False}
    for item in test_set:
        if isPrimeNumber(item) != test_set[item]:
            print("function went wrong. data:%d expect:%s" % (item, test_set[item]))
    else:
        print("function isPrimeNumber pass unittest")


def public_factor(x, y):
    """
    求两个正整数的最大公约数，最小公倍数
    :param x: 正整数
    :param y: 正整数
    :return: x,y 最大公约数，最小公倍数
    """
    if x>y:
        x,y = y,x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor, x*y//factor


if __name__ == "__main__":
    test_isPrimeNumber()
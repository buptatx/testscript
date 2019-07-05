#! -*- coding:utf-8 -*-

"""
运算符号
"""


def test_cal():
    a = int(input('a='))
    b = int(input('b='))
    print("%d + %d = %d" % (a, b, a+b))
    print("%d - %d = %d" % (a, b, a-b))
    print("%d / %d = %d" % (a, b, a/b))
    print("%d // %d = %d" % (a, b, a//b))
    print("%d %% %d = %d" % (a, b, a%b))
    print("%d * %d = %d" % (a, b, a*b))
    print("%d ** %d = %d" % (a, b, a**b))


if __name__ == "__main__":
    test_cal()
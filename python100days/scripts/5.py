#! -*- coding:utf-8 -*-

"""
代码逻辑
"""

def chicken():
    """
    求解《百钱百鸡》问题
    1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
    问公鸡 母鸡 小鸡各有多少只
    :return:
    """
    for x in range(100//5):
        for y in range(100//3):
            z = 100 - x - y
            if 5*x + 3*y + z/3 == 100:
                print("公鸡：%d 母鸡：%d 小鸡：%d" % (x,y,z))


def chicken_org():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


def multiplication_table():
    """
    打印乘法口诀
    :return:
    """
    for i in range(1, 10):
        for j in range(1, i+1):
            print("%d*%d=%d" % (j, i, i*j), end=" ")
        print()


def check_huiwen_number(x):
    """
    判断输入的正整数是不是回文数
    回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
    :return: False or True 
    """
    if not isinstance(x, int):
        return False
    if x < 1:
        return False

    x_str = str(x)
    if x == int(x_str[::-1]):
        return True
    else:
        return False


def test_check_huiwen_number():
    test_case = {1:True, 2:True, 232:True, 22:True, 23:False, "232":False, 2.32:False}

    for i in test_case:
        if check_huiwen_number(i) != test_case[i]:
            print("test %d is not %s" % (i, test_case[i]))
            break
    else:
        print("check huiwen number pass")


def check_huiwen_number_org(num):
    temp = num
    num2 = 0
    while temp > 0:
        num2 *= 10
        num2 += temp % 10
        temp //= 10
    if num == num2:
        print('%d是回文数' % num)
    else:
        print('%d不是回文数' % num)


def fibonacci(count):
    """
    斐波那契额数列
    :param count:
    :return:
    """
    a = 0
    b = 1
    for i in range(count):
        a,b = b, a+b
        yield a


if __name__ == "__main__":
    #test_check_huiwen_number()
    # for a in fibonacci(10):
    #     print(a, end=" ")
    # print()
    multiplication_table()
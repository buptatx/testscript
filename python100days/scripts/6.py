#! -*- coding:utf-8 -*-

def factorial(n):
    if n < 1:
        return 0

    res = 1
    for i in range(1, n+1):
        res *= i

    return res


def divide_apple(m, n):
    """
    8个苹果分给4个人，必须保证每人至少有一个苹果
    一共有多少种分发
    :param m: 苹果总数
    :param n: 人数
    :return: 分苹果的方法
    """
    fm = factorial(m)
    fn = factorial(n)
    fmn = factorial(m-n)

    return (fm // fn // fmn)


def orgin_divide_apple():
    m = 7
    n = 3
    fm = 1
    for num in range(1, m + 1):
        fm *= num
    fn = 1
    for num in range(1, n + 1):
        fn *= num
    fmn = 1
    for num in range(1, m - n + 1):
        fmn *= num
    print(fm // fn // fmn)


if __name__ == "__main__":
    res = divide_apple(7, 3)
    print(res)
    # orgin_divide_apple()
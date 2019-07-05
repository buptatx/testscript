#! -*-utf-8 -*-

"""
条件判断
"""


def function_x(x):
    """
        { 3x-5 (x>1)
    y = { x+2 (-1<=x<=1)
        { 5x+3 (x<-1)
    :param x: f(x)
    :return:
    """
    if x>1:
        return 3*x - 5
    elif -1 <= x and x<= 1:
        return x+2
    else:
        return 5*x + 3


if __name__ == "__main__":
    x = float(input("x for function(x)"))
    y = function_x(x)
    print(y)
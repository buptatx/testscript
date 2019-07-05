#! -*- coding:utf-8 -*-

from random import randint, sample


def display(balls):
    """
    展示双色球号码
    :param balls:一条7个随机数的双色球码
    :return: null 直接打印
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            #如果是球序列的最后一个数 则在该数字打印前打印|
            print("|", end=" ")
        #球的号码打印 按照2位数字打印
        print("%02d" % ball, end=" ")
    print()

def random_select():
    """
    :input null
    :return: 一条7个随机数组成的序列 前6位是红色球 后1位是蓝色球
    """
    red_balls = [x for x in range(1, 34)]

    selected_balls = sample(red_balls, 6)
    selected_balls.append(randint(1, 16))
    return selected_balls

def buy():
    n = int(input("机选几注："))
    for i in range(n):
        display(random_select())


if __name__ == "__main__":
    buy()
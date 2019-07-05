#! -*- coding:utf-8 -*-

import sys
import os
import time

def list_test():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x+y for x in 'ABCDE' for y in '1234567']
    print(f)
    f = [x**2 for x in range(1, 1000)]
    print(sys.getsizeof(f))
    print(f)
    f = (x**2 for x in range(1, 1000))
    print(sys.getsizeof(f))
    print(f)
    for item in f:
        print(item)


def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
        yield a

def test_fib(n):
    for i in fib(n):
        print(i, end=" ")
    print()


def test_set():
    s1 = {1,2,3,3,3,2}
    print(s1)
    print("s1 length is %d" % len(s1))
    s2 = set(range(1,10))
    print(s2)
    s1.add(4)
    s1.add(5)
    s2.update([11,12])
    print(s1)
    print(s2)
    s2.discard(5)
    if 4 in s2:
        s2.remove(4)
    print(s2)
    #将元祖转换为集合
    s3 = set((1,2,3,3,2,1))
    print(s3)
    print(s3.pop())
    print(s3)
    #求s1与s2的交集
    print(s1)
    print(s2)
    print(s1&s2)
    #求s1与s2的并集
    print(s1|s2)
    #求s1与s2的差集
    print(s1-s2)
    #求s1与s2的中不重复的元素集合
    print(s1^s2)

    #判断是否是子集 或者是否是超集
    print(s2<=s1)
    print(s3<=s1)
    print(s1>=s2)
    print(s1>=s3)


def test_dict():
    scores = {'骆昊':95, '白元芳': 78, "狄仁杰":82}
    print(scores['骆昊'])
    print(scores["狄仁杰"])
    for i in scores:
        print("%s\t--->\t%d" % (i, scores[i]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    scores.clear()
    print(scores)

def run_light():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


def test_set_pop():
    for i in range(10):
        fruits = {"apple", "banana", "cherry"}
        x = fruits.pop()
        print("loop %d, get %s" % (i, x))


if __name__ == "__main__":
    #list_test()
    #test_fib(8)
    #test_set()
    test_set_pop()
    #test_dict()
    #run_light()
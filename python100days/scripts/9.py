#! -*- coding:utf-8 -*-

import math

class Triangle():
    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and c+b > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter()/2
        return math.sqrt(half*(half-self._a)*(half-self._b)*(half-self._c))


def test_triangle(a, b, c):
    if not Triangle.is_valid(a, b, c):
        print("can not compose triangle")
    else:
        mt = Triangle(a, b, c)
        print("area:%d parimeter:%d" % (mt.area(), mt.perimeter()))


if __name__ == "__main__":
    test_triangle(3, 1, 2)
    test_triangle(3, 3, 3)
    test_triangle(3, 4, 5)
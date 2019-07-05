#！ -*- coding:utf-8 -*-

import math
a = 257

def test_int():
    b = 257
    c = 257
    print(a is b)
    print(b is c)
    print(a is c)


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_to(self, other_point):
        dx = self.x - other_point.get_x()
        dy = self.y - other_point.get_y()
        dis = math.sqrt(dx**2 + dy**2)
        return dis


def test_point():
    p1 = Point(3, 5)
    p2 = Point()
    p2.move_to(-1, 2)
    dis = p1.distance_to(p2)
    print(dis)


if __name__ == "__main__":
    #test_int()
    test_point()
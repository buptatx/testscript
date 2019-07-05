#! -*- coding:utf-8 -*-

"""
绘图模块turtle
"""


import turtle
import time


def turtle_move():
    turtle.pensize(4)
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.mainloop()

def draw_something():
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']  # 列表
    t = turtle.Pen()  # 使用海龟的钢笔，建立一个画布。P记得大写，变量以后慢慢理解
    t.shape("turtle")
    turtle.bgcolor('black')

    for x in range(360):  # range(360)是个列表，是0-359的数字赋值给变量X
        t.pencolor(colors[x % 6])  # x%6是取余数，余数为0为红色。
        t.width(x / 100 + 1)  # 钢笔宽度，循环一次加1
        t.forward(x)
        t.left(59)  # 可以改成别的角度试试哦

    time.sleep(10)


def draw():
    colors = ["red", 'purple', 'blue', 'green', 'yellow', 'orange']
    t = turtle.Pen()
    t.shape('circle')
    turtle.bgcolor('black')

    for i in range(360):
        t.pencolor(colors[i % 6])
        t.width(i/100 + 1)
        t.forward(i)
        t.left(59)

    time.sleep(10)

def draw_v2():
    colors = ["red", "purple", "blue", "green", "yellow", "orange"]
    turtle.bgcolor('black')
    turtle.hideturtle()
    turtle.setup(width=500, height=500)

    for i in range(360):
        turtle.color(colors[i%6])
        turtle.pensize(i/300+1)
        turtle.forward(i)
        turtle.left(59)

    turtle.up()
    turtle.goto(200, -200)
    turtle.down()
    turtle.color('white')
    turtle.write('zhangpeng', font=(20,), align="center", move=True)

    # 点击窗口关闭
    turtle.Screen().exitonclick()


def draw_v3():
    colors = ["red", "purple", "blue", "green", "yellow", "orange"]
    turtle.bgcolor('black')
    turtle.hideturtle()
    turtle.speed(5)
    for i in range(360):
        turtle.color(colors[i%6])
        turtle.pensize(i/100 + 1)
        turtle.forward(i)
        turtle.left(59)
    turtle.Screen().exitonclick()

# 画爱心的顶部
def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

def draw_heart():
    # 输入表白的语句，默认I Love you
    love = input('Please enter a sentence of love, otherwise the default is "I Love you": ')
    # 输入署名或者赠谁，没有不执行
    me = input('Please enter pen name, otherwise the default do not execute: ')
    if love == '':
        love = 'I Love you'
    # 窗口大小
    turtle.setup(width=900, height=500)
    # 颜色
    turtle.color('red', 'pink')
    # 笔粗细
    turtle.pensize(3)
    # 速度
    turtle.speed(1)
    # 提笔
    turtle.up()
    # 隐藏笔
    turtle.hideturtle()
    # 去到的坐标,窗口中心为0,0
    turtle.goto(0, -180)
    turtle.showturtle()
    # 画上线
    turtle.down()
    turtle.speed(1)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    # 调用画爱心左边的顶部
    LittleHeart()
    # 调用画爱右边的顶部
    turtle.left(120)
    LittleHeart()
    # 画下线
    turtle.forward(224)
    turtle.end_fill()
    turtle.pensize(5)
    turtle.up()
    turtle.hideturtle()
    # 在心中写字 一次
    turtle.goto(0, 0)
    turtle.showturtle()
    turtle.color('#CD5C5C', 'pink')
    # 在心中写字 font可以设置字体自己电脑有的都可以设 align开始写字的位置
    turtle.write(love, font=('gungsuh', 30,), align="center")
    turtle.up()
    turtle.hideturtle()
    time.sleep(2)
    # 在心中写字 二次
    turtle.goto(0, 0)
    turtle.showturtle()
    turtle.color('red', 'pink')
    turtle.write(love, font=('gungsuh', 30,), align="center")
    turtle.up()
    turtle.hideturtle()
    # 写署名
    if me != '':
        turtle.color('black', 'pink')
        time.sleep(2)
        turtle.goto(180, -180)
        turtle.showturtle()
        turtle.write(me, font=(20,), align="center", move=True)

    # 点击窗口关闭
    window = turtle.Screen()
    window.exitonclick()


def draw_taiji():
    window = turtle.Screen()
    bage = turtle.Turtle()

    radius = 100
    bage.width(3)
    bage.color("black", "black")
    bage.begin_fill()
    bage.circle(radius / 2, 180)
    bage.circle(radius, 180)
    bage.left(180)
    bage.circle(-radius / 2, 180)
    bage.end_fill()

    bage.left(90)
    bage.up()
    bage.forward(radius * 0.35)
    bage.right(90)
    bage.down()
    bage.color("white", "white")
    bage.begin_fill()
    bage.circle(radius * 0.15)
    bage.end_fill()

    bage.left(90)
    bage.up()
    bage.backward(radius * 0.7)
    bage.down()
    bage.left(90)
    bage.color("black", "black")
    bage.begin_fill()
    bage.circle(radius * 0.15)
    bage.end_fill()

    bage.right(90)
    bage.up()
    bage.backward(radius * 0.65)
    bage.right(90)
    bage.down()
    bage.circle(radius, 180)
    bage.ht()

    window.exitonclick()


def draw_v4(loop_times):
    colors = ["red", "purple", "blue", "green", "yellow", "orange"]
    turtle.bgcolor("black")
    turtle.hideturtle()

    for i in range(loop_times):
        turtle.pensize(i/100 + 1)
        turtle.pencolor(colors[i%len(colors)])
        turtle.forward(i)
        turtle.left(59)
    turtle.exitonclick()

def draw_dome():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

def draw_simple_heart():
    turtle.hideturtle()
    turtle.color("red", "pink")
    turtle.up()
    turtle.goto(0, -180)
    turtle.down()
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    draw_dome()
    turtle.left(120)
    draw_dome()
    turtle.forward(224)
    turtle.end_fill()
    turtle.exitonclick()


if __name__ == "__main__":
    #turtle_move()
    #draw_something()
    #draw()
    #draw_heart()
    #draw_v2()
    #draw_v3()
    #draw_v4(360)
    draw_simple_heart()
    #draw_taiji()


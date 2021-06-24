import math
import turtle


def draw_circle_turtle(x, y, r):
    """
    用turtle画个圆

    :param x:圆心x坐标
    :param y:圆心y坐标
    :param r:半径
    :return:none
    """

    # 提笔
    turtle.up()
    turtle.setpos(x+r, y)
    # 落笔
    turtle.down()

    for i in range(0, 361, 1):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


draw_circle_turtle(10, 10, 150)
turtle.mainloop()

import math
import turtle
import fractions
import random


class Spiro:

    def __init__(self, xc, yc, col, R, r, l):
        """初始化"""

        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.drawing_complete = False

        self.setparams(xc, yc, col, R, r, l)

        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        """set parameters"""

        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        gcdVal = fractions.gcd(self.r, self.R)
        self.n_rot = self.r // gcdVal

        self.k = r / float(R)
        self.t.color(*col)
        self.a = 0

    def restart(self):

        # 设置标志位
        self.drawing_complete = False

        self.t.showturtle()

        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    def draw(self):
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.n_rot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)

        self.t.hideturtle()

    def update(self):
        if self.drawing_complete:
            return
        self.a += self.step

        R, k, l = self.R, self.k, self.l
        a = math.radians(self.a)
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)

        if self.a >= 360*self.n_rot:
            self.drawing_complete = True

            self.t.hideturtle()


class SpiroAnimator:

    def __init__(self, n):
        self.delta_t = 10
        self.width = turtle.window_width()
        self.height = turtle.window_height()

        self.spiros = []

        for i in range(n):
            rparams = self.gen_random_params()
            spiro = Spiro(*rparams)
            self.spiros.append(spiro)
            turtle.ontimer(self.update, self.delta_t)

    def gen_random_params(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
               random.random(),
               random.random())
        return (xc, yc, col, R, r, l)

    def update(self):
        n_complete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawing_complete:
                n_complete += 1
        if n_complete == len(self.spiros):
            self.restart()
        turtle.ontimer(self.update(), self.delta_t)

    def restart(self):
        for spiro in self.spiros:
            spiro.clear()
            rparams = self.gen_random_params()
            spiro.setparams(*rparams)
            spiro.restart()

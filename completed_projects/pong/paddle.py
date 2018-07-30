import pyglet
from pyglet.gl import *
from rect import Rectangle

class Paddle:

    def __init__(self, window, left=True):
        self.window = window
        if left:
            self.pos = (10, self.window.height // 2)
        else:
            self.pos = (self.window.width - 10, self.window.height // 2)
        self.x, self.y = self.pos
        self.y_velocity = 0

        self.size = 10, 100
        self.w, self.h = self.size

        self.bonk = False
        self.bonkdir = None

        self.score = 0

    def draw(self):
        Rectangle(self.x, self.y, self.w, self.h, mode='center')

    def update(self):
        self.y += self.y_velocity

    def move(self, y_amount):
        if not self.bonk:
            self.y_velocity = y_amount
        else:
            if self.bonkdir * y_amount < 0:
                self.y_velocity = y_amount
                self.bonk = False

    def keep_in_bounds(self):
        if self.y + self.h // 2 > self.window.height:
            self.y_velocity = 0
            self.bonk = True
            self.bonkdir = 1
        if self.y - self.h // 2 < 0:
            self.y_velocity = 0
            self.bonk = True
            self.bonkdir = -1

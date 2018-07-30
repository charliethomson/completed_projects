from pyglet.gl import *
import pyglet


class Rectangle:
    def __init__(self, x, y, l, w, color=(255,255,255), mode="CORNER"):
        self.pos = x, y
        self.size = w, l
        self.x, self.y = self.pos
        self.w, self.l = self.size
        self.r, self.g, self.b = color
        self.color = ("c3B", (color) * 4)
        if mode.upper() == "CORNER":
            self.coords = [
                self.x         , self.y + self.w,
                self.x + self.l, self.y + self.w,
                self.x + self.l, self.y         ,
                self.x         , self.y
            ]
        elif mode.upper() == "CENTER":
            self.coords = [
                self.x - self.l // 2, self.y + self.w // 2,
                self.x + self.l // 2, self.y + self.w // 2,
                self.x + self.l // 2, self.y - self.w // 2,
                self.x - self.l // 2, self.y - self.w // 2
            ]
        else: raise Error("mode incorrect use center / corner")

        pyglet.graphics.draw(4, GL_QUADS,
                            ('v2i', self.coords),
                            self.color
                            )

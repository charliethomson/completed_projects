from pyglet.gl import *
import pyglet

class Line:
    def __init__(self, points=(0, 0, 0, 0)):
        if len(points) != 4:
            raise ValueError(f"data incorrect length for line; expected 4; received {len(points)}")
        self.points = points
        self.x1, self.y1, self.x2, self.y2 = self.points


        # a is the bigger y - the smaller y
        a = max(self.y1, self.y2) - min(self.y1, self.y2)
        # b is the bigger x - the smaller x
        b = max(self.x1, self.x2) - min(self.x1, self.x2)
        # a^2 + b^2 = c^2;
        # c = sqrt(a ** 2 + b ** 2)
        # sqrt = x ** 0.5
        self.len = ((a ** 2) + (b ** 2)) ** 0.5

    def draw(self, color=(255, 255, 255)):
        pyglet.graphics.draw(2, GL_LINES,
                            ('v2i', self.points),
                            ('c3B', color * 2  )
                            )

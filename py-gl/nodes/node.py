from include.rect import Rectangle as Rect


class Node:

    def __init__(self, x, y, id=None):
        self.id = id
        self.pos = x, y
        self.x, self.y = self.pos

    def draw(self, col=(255, 255, 255)):
        Rect(self.x, self.y, 15, 15, color=col, mode='center')

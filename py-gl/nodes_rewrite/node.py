from include.generic_classes.position import Position
from include.generic_classes.funcs import *
from random import randint
from include.rect import Rectangle as Rect
from include.line import Line


class Node:

    def __init__(self, window, pos=None, address=None):
        self.window = window
        self.address = address
        self.size = 20
        if pos is None:
            self.pos = Position(randint(self.size + 1, window.width - self.size - 1), randint(self.size + 1, window.height - self.size - 1))
        else:
            self.pos = pos
        self.neighbors = []
        self.neighbor_lens = {}
        self.color = (255, 0, 0)

    def __repr__(self):
        return f"Node object at {self.pos.x}, {self.pos.y} with address {self.address}"

    def draw(self):
        Rect(self.pos.x, self.pos.y, self.size, self.size, color=self.color, mode="CENTER")

    def get_neighbors(self, neighbors):
        self.neighbors = neighbors
        for neighbor in neighbors:
            self.neighbor_lens[neighbor] = 0
        print(self.neighbors)
    
    def get_neighbor_lens(self):
        for neighbor in self.neighbor_lens.keys():
            self.neighbor_lens[neighbor] = dist(self.pos, neighbor.pos)
            print(self.neighbor_lens[neighbor])
    
    def contains(self, pos):
        x_in_range = (pos.x in range(self.pos.x - self.size // 2, self.pos.x + self.size // 2))
        y_in_range = (pos.y in range(self.pos.y - self.size // 2, self.pos.y + self.size // 2))
        return x_in_range and y_in_range
            
        
        



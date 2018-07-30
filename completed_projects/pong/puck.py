import pyglet
import random
import math
import time
from pyglet.gl import *
from rect import Rectangle as Rect


class Puck:

    def __init__(self, window, pos=None):
        if pos is None:
            self.pos = window.width // 2, window.height // 2
        else: self.pos = pos
        self.x, self.y = self.pos
        self.window = window

        self.angle = (random.random() * math.tau) - math.pi
        self.y_vel = 5 * math.cos(self.angle)
        self.x_vel = 10 * math.sin(self.angle)

        self.size = 15, 15
        self.w, self.h = self.size

        self.player_scores = {}

    def draw(self):
        Rect(int(self.x), int(self.y), self.w, self.h, color=(0, 255, 0), mode="Center")

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def raise_score(self, player):
        if player in self.player_scores:
            self.player_scores[player] += 1
        else:
            self.player_scores[player] = 1

    def get_score(self, player):
        if player in self.player_scores:
            return self.player_scores[player]
        else:
            return 0

    def check_collision(self, other):
        # roof / floor
        if self.y < self.w // 2:
            self.y = self.w // 2
            self.y_vel *= -1
        if self.y > self.window.height - self.w // 2:
            self.y = self.window.height - self.w // 2
            self.y_vel *= -1

        if self.x - self.w // 2 < 0:
            self.reset()
            self.raise_score("player2")
        if self.x + self.w // 2 > self.window.width:
            self.raise_score("player1")
            self.reset()

        # paddles
        if self.y - self.h // 2 > other.y - other.h // 2 and self.y + self.h // 2 < other.y + other.h // 2:
            if not (self.x + self.w // 2 < other.x - other.w // 2 or self.x - self.w // 2 > other.x + other.w // 2):
                self.x_vel *= -1

    def reset(self):
        self.x, self.y = self.window.width // 2, self.window.height // 2
        self.angle = (random.random() * math.tau) - math.pi
        self.y_vel = 5 * math.cos(self.angle)
        self.x_vel = 5 * math.sin(self.angle)

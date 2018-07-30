from pyglet.window import key, mouse, Window
from pyglet.gl import *
from include.rect import Rectangle as Rect
from include.line import Line
from include.generic_classes.position import Position
from node import Node
from network import Network

import pyglet


window = Window(1000, 800)
keys = key.KeyStateHandler()
window.push_handlers(keys)

nodes = [Node(window, address=i) for i in range(1, 11)]


def main():
    window.clear()




def update(dt):
    window.clear()
    
    for node in nodes:
        node.get_neighbor_lens()
        node.draw()
        # print(node.neighbors)

@window.event
def on_mouse_motion(x, y, dx, dy):
    pos = Position(x, y)
    for node in nodes:
        if node.contains(pos):
            print("contains")
            
    






pyglet.clock.schedule_interval(update, 1/60.0)
if __name__ == "__main__":
    main()
    pyglet.app.run()
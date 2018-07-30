from pyglet.window import mouse, key, Window
from include.rect  import Rectangle as Rect
from node          import Node
from network       import Network

import argparse
import random
import pyglet

window = Window(resizable=True, width=800, height=800)
window.clear()
parser = argparse.ArgumentParser()
parser.add_argument("num", help="Number of nodes", type=int)
args = parser.parse_args()

num_of_nodes = args.num


def generate_nodes(amount, seed=0):
    """generates an amount of randomly placed nodes"""
    # random.seed(seed)

    return [Node(random.randint(0, window.width), random.randint(0, window.height), id=i) for i in range(amount)]

window_max_line_len = ((window.width ** 2) + (window.height ** 2)) ** 0.5


@window.event
def on_mouse_press(x, y, button, mod):
    window_max_line_len = ((window.width ** 2) + (window.height ** 2)) ** 0.5
    if button == mouse.RIGHT:
        window.clear()
    if button == mouse.LEFT:
        nodes = generate_nodes(num_of_nodes)
        for node in nodes:
            node.draw()
        network = Network(nodes)
        network.draw_connections(window_max_line_len)
        network.get_connection_stats()

if __name__ == "__main__":
    pyglet.app.run()

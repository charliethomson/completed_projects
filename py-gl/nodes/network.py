from include.line import Line

import colorsys
import time
import statistics as stats


def remap(var, var_low, var_high, end_low, end_high):
    return var / ((var_high - var_low) * (end_high - end_low))


def count_connections(node_count):
    # number of connections is: nc - 1 + nc - 2 ... nc - (nc + 1) == 1
    ret = 0
    nc = node_count
    while nc != 0:
        nc -= 1
        ret += nc
    return ret


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def line_color(line, max_len):

    hue = remap(line.len, 0, max_len, 0.2, 0.8)
    return hsv2rgb(hue, 1, 1)


def connection_points(node1, node2):
    return [node1.x, node1.y, node2.x, node2.y]


class Network:

    def __init__(self, nodes):
        self.nodes = nodes  # an array of nodes, each with x, y positions
        self.connection_count = count_connections(len(nodes))
        self.connections = []
        self.connection_lengths = []

        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1.id == None or node2.id == None:
                    raise Error("undefined node id")
                if node1.id != node2.id:
                    connection = connection_points(node1, node2)
                    if connection not in self.connections and connection[::-1] not in self.connections:
                        self.connections.append(connection)

        for array in self.connections:
            line = Line(array)
            self.connection_lengths.append(line.len)



    def draw_connections(self, max_len):
        for array in self.connections:
            line = Line(array)
            line.draw(color=line_color(line, max_len))

    def get_connection_stats(self):
        longest_line = max(self.connection_lengths)
        shortest_line = min(self.connection_lengths)
        average_length = stats.mean(self.connection_lengths)

        print(f"longest line: {longest_line}\nshortest line: {shortest_line}\
              \naverage line length: {average_length}\nconnection count: {self.connection_count}")











####

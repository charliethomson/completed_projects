
class Position:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __repr__(self):
        return f"Position Vector at {self.x}, {self.y} with angle {self.angle}"

from math import sqrt

def dist(pos1, pos2):
    bigX, smallX = max(pos1.x, pos2.x), min(pos1.x, pos2.x)
    bigY, smallY = max(pos1.y, pos2.y), min(pos1.y, pos2.y)
    print(bigX, smallX, bigY, smallY)
    return sqrt(((bigX - smallX) ** 2) + (bigY - smallY) ** 2)


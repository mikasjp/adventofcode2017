import numpy as np

input = [x.split(" => ") for x in open("data.txt","r").read().split("\n")]

def PatternToArray(p):
    return [list(x) for x in p.split("/")]

def RotatePattern(p1):
    p1_90 = list(map(list, zip(*p1[::-1])))
    p1_180 = list(map(list, zip(*p1_90[::-1])))
    p1_270 = list(map(list, zip(*p1_180[::-1])))
    return [p1, p1_90, p1_180, p1_270]

def FlipPattern(p1):
    p1_xf = list(reversed(p1))
    p1_yf = [list(reversed(x)) for x in p1]
    return [p1_xf, p1_yf]

def Compare(p1, p2):
    flp = FlipPattern(p1)
    p = RotatePattern(p1) + flp + RotatePattern(flp[0]) + RotatePattern(flp[1])
    return p2 in p

def FindPattern(item):
    for x in input:
        if Compare(PatternToArray(x[0]), item):
            return PatternToArray(x[1])
    return False

def ProcessGrid(grid):
    if grid.__len__()%2 == 0:
        n = 2
    else:
        n = 3

    g = []
    size = int(grid.__len__() / n)
    for y in range(size):
        r = []
        for x in range(size):
            combinedpattern = [[grid[n*y + j][n*x + i] for i in range(n)] for j in range(n)]
            r.append(FindPattern(combinedpattern))
        r = np.hstack(r).tolist()
        g.extend(r)
    return g


# First part
pattern = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
for i in range(5):
    pattern = ProcessGrid(pattern)

counter = 0
for row in pattern:
    counter += row.count("#")

print("First part: " + str(counter))


# Second part
pattern = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
for i in range(18):
    pattern = ProcessGrid(pattern)

counter = 0
for row in pattern:
    counter += row.count("#")

print("Second part: " + str(counter))

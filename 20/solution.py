import math
import re

input = [[int(s) for s in re.findall("[-\d]+", l)] for l in open("data.txt","r").read().split("\n")]
acc = [math.sqrt(part[8]**2 + part[7]**2 + part[6]**2) for part in input]

p = [0 for i in range(input.__len__())]

# First part:
for w in range(1000):
    for i, q in enumerate(input):
        x, y, z, vx, vy, vz, ax, ay, az = q
        input[i] = [x+vx+ax, y+vy+ay, z+vz+az, vx+ax, vy+ay, vz+az, ax, ay, az]
        p[i] = abs(input[i][0]) + abs(input[i][1]) + abs(input[i][2])    

print("First part: " + str(p.index(min(p))))
import re

input = [[int(s) for s in re.findall("[-\d]+", l)] for l in open("data.txt","r").read().split("\n")]

p = [0 for i in range(input.__len__())]

for i, q in enumerate(input):
    ax = q[6]
    ay = q[7]
    az = q[8]

    vx = q[3]
    vy = q[4]
    vz = q[5]

    x = q[0] + vx + ax
    y = q[1] + vy + ay
    z = q[2] + vz + az

    p[i] += abs(x) + abs(y) + abs(z)

print("First part: " + str(p.index(min(p))))

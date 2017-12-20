import re

input = [[int(s) for s in re.findall("[-\d]+", l)] for l in open("data.txt","r").read().split("\n")]

# First part:
acc = [abs(part[8]) + abs(part[7]) + abs(part[6]) for part in input]
minacc = [i for i,a in enumerate(acc) if a==min(acc)]
v = [abs(input[i][5]) + abs(input[i][4]) + abs(input[i][3]) for i in minacc]
minv = [minacc[i] for i,x in enumerate(v) if x==min(v)]
distance = [abs(input[i][2]) + abs(input[i][1]) + abs(input[i][0]) for i in minv]
mindist = [minv[i] for i,x in enumerate(distance) if x==min(distance)]

if mindist.__len__()==1:
    print("First part: " + str(mindist[0]))
else:
    print("Possible solutions: ")
    print(mindist)

# Second part:
def Collision(a, b):
    x1, y1, z1, vx1, vy1, vz1, ax1, ay1, az1 = a
    x2, y2, z2, vx2, vy2, vz2, ax2, ay2, az2 = b

    dx = (2*(vx1 - vx2))**2 - 8 * (x1-x2) * (ax1 - ax2)
    dy = (2*(vy1 - vy2))**2 - 8 * (y1-y2) * (ay1 - ay2)
    dz = (2*(vz1 - vz2))**2 - 8 * (z1-z2) * (az1 - az2)

    return dx>=0 and dy>=0 and dz>=0


c = []

for ia,a in enumerate(input):
    for ib in range(ia+1, input.__len__()):
        if Collision(a, input[ib]):
            c.extend([ia, ib])

print("Colliding points: " + str(set(c).__len__()))

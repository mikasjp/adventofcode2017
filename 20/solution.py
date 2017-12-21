import re
import math

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

    col = dx>=0 and dy>=0 and dz>=0

    if not col: return False
    if ax1-ax2 == 0:
        if vx1-vx2 == 0:
            return False
        else:
            roots = [x for x in [(x2-x1) / (2*vx1-2*vx2)] if x>=0 and x.is_integer()]
    else:
        roots = [x for x in [(vx1-vx2-math.sqrt(dx))/(2*(ax1-ax2)), (vx1-vx2+math.sqrt(dx))/(2*(ax1-ax2))] if x >= 0 and x.is_integer()]

    if roots.__len__()==0: return False

    return min(roots)
    

c = {}

for ia,a in enumerate(input):
    for ib in range(ia+1, input.__len__()):
        col = Collision(a, input[ib])
        if col:
            if ia in c:
                c[ia] = col if col<c[ia] else c[ia]
            else:
                c[ia] = col

            if ib in c:
                c[ib] = col if col<c[ib] else c[ib]
            else:
                c[ib] = col

def TrueCollision(ia, ib):
    global input
    global c

    col = Collision(input[ia], input[ib])
    if col:
        return c[ia]>=col and c[ib]>=col
    return False

counter = 0

for ia,a in enumerate(input):
    for ib in range(ia+1, input.__len__()):
        if TrueCollision(ia, ib):
            counter += 2

print("Potential candidates: " + str(c.__len__()))

print("True collisions: " + str(counter))

assert 1000 - counter == 499
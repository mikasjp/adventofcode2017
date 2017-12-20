import math
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
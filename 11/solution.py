input = open('data.txt', 'r').read().split(",")

coords = {"x": 0, "y": 0, "z": 0}

dist = []

for c in input:
    if c=="n":
        coords["x"] += 0
        coords["y"] += 1
        coords["z"] += -1

    if c=="ne":
        coords["x"] += 1
        coords["y"] += 0
        coords["z"] += -1

    if c=="se":
        coords["x"] += 1
        coords["y"] += -1
        coords["z"] += 0

    if c=="s":
        coords["x"] += 0
        coords["y"] += -1
        coords["z"] += 1

    if c=="sw":
        coords["x"] += -1
        coords["y"] += 0
        coords["z"] += 1

    if c=="nw":
        coords["x"] += -1
        coords["y"] += 1
        coords["z"] += 0

    dist.append( ( abs(-coords["x"]) + abs(-coords["y"]) + abs(-coords["z"]) )/2 )

print("First part: " + str(dist[-1]))

print("Second part: " + str(max(dist)))
def ExtendCluster(cluster):
    nc = []
    N = cluster.__len__()
    nc.append(["." for i in range(N+2)])
    nc.extend([["."] + x + ["."] for x in cluster])
    nc.append(["." for i in range(N+2)])
    return nc

def Move(d):
    if d =="up": return -1, 0
    if d =="right": return 0, 1
    if d =="down": return 1, 0
    if d =="left": return 0, -1

dir = ["up", "right", "down", "left"]

# First part
input = [list(x) for x in open("data.txt","r").read().split("\n")]
N = int((input.__len__()) / 2)
v = {"x": N, "y": N, "dir": "up"}

counter = 0
for i in range(10000):
    # Turn
    turn = 1 if input[v["y"]][v["x"]]=="#" else -1
    v["dir"] = dir[(dir.index(v["dir"])+turn)%(dir.__len__())]

    # Cure or infect
    if input[v["y"]][v["x"]] == ".":
        counter += 1
        input[v["y"]][v["x"]] = "#"
    else:
        input[v["y"]][v["x"]] = "."
    
    # Move
    m = Move(v["dir"])
    v["y"] += m[0]
    v["x"] += m[1]
    if v["y"] in [0, input.__len__()-1] or v["x"] in [0, input.__len__()-1]:
        input = ExtendCluster(input)
        v["y"] += 1
        v["x"] += 1

print("First part: " + str(counter))


# Second part
input = [list(x) for x in open("data.txt","r").read().split("\n")]
N = int((input.__len__()) / 2)
v = {"x": N, "y": N, "dir": "up"}

counter = 0
for i in range(10000000):
    # Turn then cure, weaken, flag or infect
    if input[v["y"]][v["x"]] == ".":
        turn = -1
        input[v["y"]][v["x"]] = "W"
    elif input[v["y"]][v["x"]] == "W":
        turn = 0
        input[v["y"]][v["x"]] = "#"
        counter += 1
    elif input[v["y"]][v["x"]] == "#":
        turn = 1
        input[v["y"]][v["x"]] = "F"
    else:
        turn = 2
        input[v["y"]][v["x"]] = "."

    v["dir"] = dir[(dir.index(v["dir"])+turn)%(dir.__len__())]
    
    # Move
    m = Move(v["dir"])
    v["y"] += m[0]
    v["x"] += m[1]
    if v["y"] in [0, input.__len__()-1] or v["x"] in [0, input.__len__()-1]:
        input = ExtendCluster(input)
        v["y"] += 1
        v["x"] += 1

print("Second part: " + str(counter))

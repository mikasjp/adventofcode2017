input = [list(map(int,x.split("/"))) for x in open("data.txt","r").read().split("\n")]

def BuildBridges(com, port, weight, i):
    possible = [x for x in com if port in x]
    b = []
    i += 1
    if possible.__len__() > 0:
        for x in possible:
            nextport = x[x.index(port)-1]
            tmp = [y for y in com if y != x]
            b.extend(BuildBridges(tmp, nextport, weight + sum(x), i+1))
        return b
    else:
        return [[weight, i]]

bridges = BuildBridges(input, 0, 0, 0)


# First part
strength = max([w[0] for w in bridges])
print("First part: " + str(strength))

# Second part
maxl = max([w[1] for w in bridges])
longest = max([w[0] for w in bridges if w[1] == maxl])
print("Second part: " + str(longest))

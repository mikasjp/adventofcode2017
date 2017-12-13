input = open('data.txt', 'r').read().split("\n")

groups = [list(map(int, (x.split(" <-> "))[1].split(", ") )) for i,x in enumerate(input)]
groups = [list(set(x+[i])) for i,x in enumerate(groups)]

merged = []

def FindAndMerge(g, gl):
    i = 0
    while i < g.__len__():
        for x in gl:
            if g[i] in x:
                g = list(set(g+x))
                gl.remove(x)
                i = 0
        i += 1

    global groups
    groups = gl
    return g


while groups.__len__()>0:
    merged.append(FindAndMerge(groups[0],groups))

for g in merged:
    if 0 in g:
        print("First part: " + str(g.__len__()))
        break

print("Second part: " + str(merged.__len__()))
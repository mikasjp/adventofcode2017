input = open('data.txt', 'r').read().split("\n")

conn = [list(map(int, (x.split(" <-> "))[1].split(", ") )) for x in input]

l = [0]

j = 0

for j in range(conn.__len__()):
    for i,x in enumerate(conn):
        if i in l:
            l.extend([z for z in x if z not in l])


print("First part: " + str(l.__len__()))

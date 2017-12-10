input = [int(x) for x in open('data.txt', 'r').read().split(",")]

lv = list(range(256))

def GetRange(a,b,l):
    return [a[(x+b) % (a.__len__())] for x in range(l)]

def ReverseRange(a,b,l):
    r = list(reversed(GetRange(a,b,l)))
    for i in range(l):
        a[(i+b) % (a.__len__())] = r[i]
    return a

position = 0

skip = 0

def KnotHashRound():
    global position
    global lv
    global input
    global skip
    for i,x in enumerate(input):
        lv = ReverseRange(lv, position, x)
        position += x + skip
        skip += 1

# First part
KnotHashRound()
print("First part: " + str(lv[0]*lv[1]))

# Second part

def DenseHash(l):
    h = list(range(16))
    for x in range(16):
        h[x] = l[(16*x)]^l[(16*x)+1]^l[(16*x)+2]^l[(16*x)+3]^l[(16*x)+4]^l[(16*x)+5]^l[(16*x)+6]^l[(16*x)+7]^l[(16*x)+8]^l[(16*x)+9]^l[(16*x)+10]^l[(16*x)+11]^l[(16*x)+12]^l[(16*x)+13]^l[(16*x)+14]^l[(16*x)+15]
    q = list(map(hex,h))
    q = [("0" if x.__len__()==3 else "")+x.replace("0x","") for x in q]
    return "".join(q)


li = list(map(str,input))
input = [ord(x) for x in ",".join(li)]
input.extend([17, 31, 73, 47, 23])

lv = list(range(256))
position = 0
skip = 0

for i in range(64):
    KnotHashRound()

print("Second part: " + DenseHash(lv))

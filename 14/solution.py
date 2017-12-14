import binascii

input = open("data.txt").read()

inp = []

lv = []

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
    global inp
    global skip
    for i,x in enumerate(inp):
        lv = ReverseRange(lv, position, x)
        position += x + skip
        skip += 1

def DenseHash(l):
    h = list(range(16))
    for x in range(16):
        h[x] = l[(16*x)]^l[(16*x)+1]^l[(16*x)+2]^l[(16*x)+3]^l[(16*x)+4]^l[(16*x)+5]^l[(16*x)+6]^l[(16*x)+7]^l[(16*x)+8]^l[(16*x)+9]^l[(16*x)+10]^l[(16*x)+11]^l[(16*x)+12]^l[(16*x)+13]^l[(16*x)+14]^l[(16*x)+15]
    q = list(map(hex,h))
    q = [("0" if x.__len__()==3 else "")+x.replace("0x","") for x in q]
    return "".join(q)

def KnotHash(s):
    global inp
    global lv
    global position
    global skip
    lv  = list(range(256))
    inp = [ord(x) for x in s]
    inp.extend([17, 31, 73, 47, 23])

    lv = list(range(256))
    position = 0
    skip = 0

    for i in range(64):
        KnotHashRound()

    return DenseHash(lv)

assert KnotHash("TEST") == "273d1ca62e42c54300605f37b66958c5"

rows = []
for i in range(128):
    r = KnotHash(input+"-"+str(i))
    rows.append( (bin(int(r, 16))[2:]) ) 

# First part
cnt = [x.count("1") for x in rows]
print("First part: " + str(sum(cnt)))


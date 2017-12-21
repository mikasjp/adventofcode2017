input = [x.split(" => ") for x in open("data.txt","r").read().split("\n")]

def PatternToArray(p):
    return [list(x) for x in p.split("/")]

def CmpArr(a1, a2):

    if a1.__len__() != a2.__len__():
        return False

    same = True
    for y in range(a1.__len__()):
        for x in range(a1.__len__()):
            if a1[y][x] != a2[y][x]:
                same = False
                break
    return same

def RotatePattern(p1):
    p1_90 = list(map(list, zip(*p1[::-1])))
    p1_180 = list(map(list, zip(*p1_90[::-1])))
    p1_270 = list(map(list, zip(*p1_180[::-1])))
    return [p1, p1_90, p1_180, p1_270]

def FlipPattern(p1):
    p1_xf = list(reversed(p1))
    p1_yf = [list(reversed(x)) for x in p1]
    return [p1_xf, p1_yf]

def Compare(p1, p2):
    p = RotatePattern(p1) + RotatePattern(p1)
    return p2 in p1

pattern = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]

for x in input:
    if Compare(PatternToArray(x[0]), pattern):
        print("Mamy to!")

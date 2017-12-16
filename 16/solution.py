input = [x for x in open("data.txt","r").read().split(",")]

dancefloor = [chr(l) for l in range(97, 113)]

def DanceStep(x):
    global dancefloor
    if x[0]=="s":
        s = int(x[1:])
        dancefloor = dancefloor[-s:] + dancefloor[0:-s]

    if x[0]=="x":
        s = [int(z) for z in x[1:].split("/")]
        tmp = dancefloor[s[0]]
        dancefloor[s[0]] = dancefloor[s[1]]
        dancefloor[s[1]] = tmp

    if x[0]=="p":
        s = [dancefloor.index(z) for z in x[1:].split("/")]
        tmp = dancefloor[s[0]]
        dancefloor[s[0]] = dancefloor[s[1]]
        dancefloor[s[1]] = tmp

def Dance():
    global input
    for x in input:
        DanceStep(x)

Dance()

print("First part: " + "".join(dancefloor))

for i in range((1000000000-1)%36):
    Dance()

print("Second part: " + "".join(dancefloor))
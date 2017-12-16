input = [x for x in open("data.txt","r").read().split(",")]

dancefloor = []

def InitDancefloor():
    return [chr(l) for l in range(97, 113)]

def DanceStep(x, df):
    if x[0]=="s":
        s = int(x[1:])
        df = df[-s:] + df[0:-s]

    if x[0]=="x":
        s = [int(z) for z in x[1:].split("/")]
        tmp = df[s[0]]
        df[s[0]] = df[s[1]]
        df[s[1]] = tmp

    if x[0]=="p":
        s = [df.index(z) for z in x[1:].split("/")]
        tmp = df[s[0]]
        df[s[0]] = df[s[1]]
        df[s[1]] = tmp
    return df

def Dance(steps, df):
    for x in steps:
        df = DanceStep(x, df)
    return df

def DetectPeriod(steps):
    df = InitDancefloor()
    l = []
    i = 0
    df = Dance(steps, df)
    while True:
        df = Dance(steps, df)
        if tuple(df) in l: break
        l.append(tuple(df))
        i += 1
    return i

dancefloor = InitDancefloor()

#First part
dancefloor = Dance(input, dancefloor)
print("First part: " + "".join(dancefloor))

# Second part
MagicNumber = DetectPeriod(input)

for i in range((1000000000-1) % MagicNumber):
    dancefloor = Dance(input, dancefloor)

print("Second part: " + "".join(dancefloor))
input = open("data.txt","r").read().split("\n")

x,y = input[0].index("|"), 0
d = "s"
NoWayToGo = False
letters = []
steps = 0

while not NoWayToGo:
    while True:
        if input[y][x] not in ["|", "-", "+"]: letters.append(input[y][x])
        if d=="n": y -= 1
        if d=="s": y += 1
        if d=="w": x -= 1
        if d=="e": x += 1
        if x<0 or x>=input[0].__len__() or y<0 or y>=input.__len__():
            NoWayToGo = True
            break
        steps += 1
        if input[y][x] == "+": break

    if d=="n" or d=="s":
        if x>0:
            if input[y][x-1]=="-":
                d = "w"
                continue
        if x<input[0].__len__()-1:
            if input[y][x+1]=="-":
                d = "e"
                continue

    if d=="e" or d=="w":
        if y>0:
            if input[y-1][x]=="|":
                d = "n"
                continue
        if y<input.__len__()-1:
            if input[y+1][x]=="|":
                d = "s"
                continue

    NoWayToGo = True

# First part
print("First part: " + "".join(letters))

# Second part
print("Second part: " + str(steps))

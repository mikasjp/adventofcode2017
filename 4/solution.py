input = open('data.txt', 'r').read()

# First part
counter = 0

for line in input.split("\n"):
    check = True
    spl = line.split(" ")
    for word in spl:
        if(spl.count(word)>1):
            check = False
            break
    if check:
        counter = counter+1

print("First part: "+str(counter))

# Second part

def SortLetters(s):
    return  "".join(sorted(s))

counter = 0

for line in input.split("\n"):
    check = True
    spl = line.split(" ")
    sorted_spl = list(map(SortLetters, spl))
    for word in sorted_spl:
        if(sorted_spl.count(word)>1):
            check = False
            break
    if check:
        counter = counter+1

print("Second part: "+str(counter))
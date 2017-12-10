input = open('data.txt', 'r').read()

filtered = []

i = 0

while i<input.__len__():
    if input[i]=="!":
        input = input[:i] + input[i+2:]
        i = 0
    i += 1

garbage = 0

clear = False

while not clear:
    try:
        o = input.index("<")
        c = input.index(">")
        input = input[:o] + input[c+1:]
        garbage += c-o-1
    except:
        clear = True


input = input.replace(",","")

score = 0
depth = 0
for x in input:
    if x == "{":
        depth += 1
    if x == "}":
        score += depth
        depth -= 1

print("First part: " + str(score))
print("Second part: " + str(garbage))

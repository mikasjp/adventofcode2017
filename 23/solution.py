import math

input = [x for x in open("data.txt","r").read().split("\n")]

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def Value(s):
    global reg
    if isInt(s):
        return int(s)
    else:
        if s not in reg: reg[s] = 0
        return reg[s]


# First part
reg = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

counter = 0

i = 0
while i < input.__len__() and i >= 0:
    ins = input[i].split(" ")

    if ins[0] == "set":
        reg[ins[1]] = Value(ins[2])
        i += 1
        continue
    
    if ins[0] == "sub":
        reg[ins[1]] = Value(ins[1]) - Value(ins[2])
        i += 1
        continue

    if ins[0] == "mul":
        reg[ins[1]] = Value(ins[1]) * Value(ins[2])
        i += 1
        counter += 1
        continue

    if ins[0] == "jnz":
        if Value(ins[1]) != 0: 
            i += Value(ins[2])
        else:
            i += 1

print("First part: " + str(counter))


# Second part

def isPrime(n):
    ans = True
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            ans = False
            break
    return ans

h = 0
b = 93
c = b
b = b * 100
b = b + 100000
c = b
c = c + 17000

for x in range(b, c+1, 17):
    if not isPrime(x):
        h = h + 1

print("Second part: " + str(h))

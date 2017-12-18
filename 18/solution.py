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

reg = {}
LastSound = 0

i = 0
while i < input.__len__():
    ins = input[i].split(" ")
    
    if ins[0] == "snd":
        LastSound = Value(ins[1])
        i += 1
        continue

    if ins[0] == "set":
        reg[ins[1]] = Value(ins[2])
        i += 1
        continue
    
    if ins[0] == "add":
        reg[ins[1]] = Value(ins[1]) + Value(ins[2])
        i += 1
        continue

    if ins[0] == "mul":
        reg[ins[1]] = Value(ins[1]) * Value(ins[2])
        i += 1
        continue

    if ins[0] == "mod":
        reg[ins[1]] = Value(ins[1]) % Value(ins[2])
        i += 1
        continue

    if ins[0] == "rcv":
        if Value(ins[1]) != 0:
            reg[ins[1]] = LastSound
        break

    if ins[0] == "jgz":
        if Value(ins[1]) != 0:
            i += Value(ins[2])
        else:
            i += 1

print("First part: " + str(LastSound))

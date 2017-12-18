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


# Second part
reg = [{"p": 0}, {"p": 1}]
queue = [[], []]
pointer = [0, 0]
counter = [0, 0]

def Value2(s, id):
    global reg
    if isInt(s):
        return int(s)
    else:
        if s not in reg[id]: reg[id][s] = 0
        return reg[id][s]

def ProgramStep(id):
    global reg
    global pointer
    global input
    global queue
    global counter

    if pointer[id] >= input.__len__():
        return False

    ins = input[pointer[id]].split(" ")
    
    if ins[0] == "snd":
        queue[id-1].append(Value2(ins[1], id))
        pointer[id] += 1
        return True

    if ins[0] == "set":
        reg[id][ins[1]] = Value2(ins[2], id)
        pointer[id] += 1
        return True
    
    if ins[0] == "add":
        reg[id][ins[1]] = Value2(ins[1], id) + Value2(ins[2], id)
        pointer[id] += 1
        return True

    if ins[0] == "mul":
        reg[id][ins[1]] = Value2(ins[1], id) * Value2(ins[2], id)
        pointer[id] += 1
        return True

    if ins[0] == "mod":
        reg[id][ins[1]] = Value2(ins[1], id) % Value2(ins[2], id)
        pointer[id] += 1
        return True

    if ins[0] == "rcv":
        if queue[id].__len__()>0:
            reg[id][ins[1]] = queue[id][0]
            queue[id].pop(0)
            pointer[id] += 1
            counter[id] += 1
            return True
        else:
            return False

    if ins[0] == "jgz":
        if Value2(ins[1], id) != 0:
            pointer[id] += Value2(ins[2], id)
        else:
            pointer[id] += 1
        return True

while True:
    print("Running program 0")
    while ProgramStep(0):
        pass
    print("Running program 1")
    while ProgramStep(1):
        pass
    print(queue)
    if queue[0].__len__() == 0 and queue[1].__len__() == 0: break

print("Second part: " + str(counter[1]))

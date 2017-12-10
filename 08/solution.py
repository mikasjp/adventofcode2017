input = [x.split(" ") for x in open('data.txt', 'r').read().split("\n")]

reg = {}

def condition(r, c, v):
    val = int(v)
    if c==">":
        return reg[r]>val
    if c=="<":
        return reg[r]<val
    if c==">=":
        return reg[r]>=val
    if c=="<=":
        return reg[r]<=val
    if c=="==":
        return reg[r]==val
    if c=="!=":
        return reg[r]!=val

previous_values = []

for x in input:
    
    if x[4] not in reg:
        reg[x[4]] = 0
        previous_values.append(0)
    
    if x[0] not in reg:
        reg[x[0]] = 0
        previous_values.append(0)

    if condition(x[4], x[5], x[6]):
        if x[1]=="inc":
            reg[x[0]] += int(x[2])
        if x[1]=="dec":
            reg[x[0]] -= int(x[2])
        previous_values.append(reg[x[0]])

# First part
print("First part: " + str(max(reg.values())))

# Second part
print("First part: " + str(max(previous_values)))
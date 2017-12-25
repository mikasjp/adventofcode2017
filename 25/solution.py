input = open("data.txt", "r").read().split("\n")

state = input[0][-2]
checksum = int(input[1].split(" ")[5])
tape = {0: 0}
pos = 0
turing = {}

for i in range((int(input.__len__()-3)/10)):
    l = i * 10 + 3
    s = input[l][-2]
    zero = [int(input[l+2][-2]), -1 if input[l+3].split(" ")[-1]=="left." else 1, input[l+4][-2]]
    one = [int(input[l+6][-2]), -1 if input[l+7].split(" ")[-1]=="left." else 1, input[l+8][-2]]
    turing[s] = [zero, one]

for i in range(checksum):
    if pos not in tape: tape[pos] = 0
    v = tape[pos]
    tape[pos] = turing[state][v][0]
    pos += turing[state][v][1]
    state = turing[state][v][2]


# First part
counter = 0
for k, v in tape.items():
    if v == 1: counter += 1

print("First part: " + str(counter))

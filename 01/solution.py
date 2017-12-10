input = open('data.txt', 'r').read()


# First part

s = 0

for i in range(0, input.__len__()):
    if input[i]==input[(i+1) % (input.__len__())]:
        s += int(input[i])

print("First part: " + str(s))


# Second part

s = 0
offset = int(input.__len__()/2)

for i in range(0, input.__len__()):
    if input[i]==input[(i+offset)  % (input.__len__())]:
        s += int(input[i])

print("Second part: " + str(s))
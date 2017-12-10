input = open('data.txt', 'r').read()

# First part

memory = list( map(int, input.split("\n")) )

address = 0
counter = 0

while address<memory.__len__():
    next = address+memory[address]
    memory[address] = memory[address] + 1
    address = next
    counter = counter + 1

print("First part: " + str(counter))


# Second part

memory = list( map(int, input.split("\n")) )

address = 0
counter = 0

while address<memory.__len__():
    next = address+memory[address]
    if memory[address]>2:
        offset = -1
    else:
        offset = 1
    memory[address] = memory[address] + offset
    address = next
    counter = counter + 1

print("Second part: " + str(counter))
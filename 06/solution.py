input = [int(x) for x in open('data.txt', 'r').read().split("\t")]

memory_history = {}

def redistribute():
    bank = input.index(max(input))
    bank_size = input[bank]
    input[bank] = 0
    for i in range(0,bank_size):
        input[(i+1+bank) % input.__len__()] += 1
    memory_history[str(input)] = memory_history[str(input)]+1 if str(input) in memory_history else 1


# First part

counter = 0
while (memory_history[max(memory_history, key=memory_history.get)] if memory_history.__len__()>0 else 1)<2:
    redistribute()
    counter += 1

print("First part: " + str(counter))

# Second part

counter = 0
while (memory_history[max(memory_history, key=memory_history.get)] if memory_history.__len__()>0 else 1)<3:
    redistribute()
    counter += 1

print("Second part:" + str(counter))
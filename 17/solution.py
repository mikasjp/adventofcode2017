input = 359

def Spinlock(jump, iterations):
    buffer = [0]
    position = 0

    for i in range(iterations):
        position = (position + jump) % buffer.__len__()
        buffer.insert(position+1, i+1)
        position += 1

    return buffer

# First part
buffer = Spinlock(input, 2018)
ans = buffer[(buffer.index(2017) + 1) % buffer.__len__()]
print("First part: " + str(ans))

# Second part
bl = 1
position = 0
ans = 0

for i in range(1, 50000001):
    position = (position + input) % bl
    bl += 1
    position += 1
    if (position)==1:
        ans = i

print("Second part: " + str(ans))
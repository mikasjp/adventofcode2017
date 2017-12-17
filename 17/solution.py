input = 359

buffer = [0]
position = 0

for i in range(2018):
    position = (position + input) % buffer.__len__()
    buffer.insert(position+1, i+1)
    position += 1

# First part
ans = buffer[(buffer.index(2017) + 1) % buffer.__len__()]
print("First part: " + str(ans))

input = open('data.txt', 'r').read()

part1 = [int(x) for i,x in enumerate(input) if x==input[(i+1) % (input.__len__())]]
part2 = [int(x) for i,x in enumerate(input) if x==input[(i+int(input.__len__()/2)) % (input.__len__())]]

print("First part: " + str(sum(part1)))
print("Second part: " + str(sum(part2)))
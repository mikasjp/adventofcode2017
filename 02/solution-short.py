import itertools

input = [list(map(int, x.split("\t"))) for x in list( open('data.txt', 'r').read().split("\n") )]

part1 = sum([max(x)-min(x) for x in input])
print("First part: " + str(part1))

part2 = sum([[x[w[0][0]]/x[w[0][-1]] for w in list(map(lambda a: [(a[0][0], a[-1][0]) ,a[0][1]%a[-1][1]], [p for i,p in enumerate(itertools.product(enumerate(x), repeat=2)) if i%(x.__len__()+1)!=0])) if w[-1]==0][0] for x in input])
print("Second part: " + str(part2))
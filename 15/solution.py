input = [int(x.split(" ")[4]) for x in open("data.txt", "r").read().split("\n")]

A = 16807
B = 48271

judge = 0

for i in range(40000000):
    A *= input[0]
    A %= 2147483647
    B *= input[0]
    B %= 2147483647

    if A & 0xFFFF == B & 0xFFFF:
        judge +=1

print("First part: " + judge)
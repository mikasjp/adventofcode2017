input = [int(x.split(" ")[4]) for x in open("data.txt", "r").read().split("\n")]

AF = 16807
BF = 48271

A = input[0]
B = input[1]

judge = 0

for i in range(40000000):
    A *= AF
    A %= 2147483647
    B *= BF
    B %= 2147483647

    if A & 0xFFFF == B & 0xFFFF:
        judge +=1

print("First part: " + str(judge))
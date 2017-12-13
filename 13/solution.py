input = [list(map(int,x.split(": "))) for x in open('data.txt').read().split("\n")]

class Scanner:

    movement = True
    pos = 0
    max = 0

    def __init__(self, max):
        self.max = max

    def Step(self):
        self.pos += 1 if self.movement else -1
        if self.pos==0: self.movement = True
        if self.pos==self.max-1: self.movement = False

i = 0
firewall = []

for x in range(input[-1][0]+1):
    if input[i][0]==x:
        firewall.append(Scanner(input[i][1]))
        i += 1
    else:
        firewall.append(None)

# sprawdz, rusz

severity = 0

for packet in range(firewall.__len__()):
    if firewall[packet] != None:
        if firewall[packet].pos == 0:
            severity += packet * firewall[packet].max
    for i in firewall:
        if i != None:
            i.Step()

print(severity)
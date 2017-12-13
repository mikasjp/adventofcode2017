input = [list(map(int,x.split(": "))) for x in open('data.txt').read().split("\n")]

firewall = []

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

def ResetFirewall():
    global firewall
    i = 0
    for x in range(input[-1][0]+1):
        if input[i][0]==x:
            firewall.append(Scanner(input[i][1]))
            i += 1
        else:
            firewall.append(None)

def StepFirewall():
    global firewall
    for i in firewall:
        if i != None:
            i.Step()

def ThrowPacket(delay):
    global firewall
    severity = 0
    packet = -delay
    while packet<firewall.__len__():

        if packet<0:
            packet += 1
            StepFirewall()
            continue

        if firewall[packet] != None:
            if firewall[packet].pos == 0:
                severity += packet * firewall[packet].max
        StepFirewall()
        
        packet += 1
    return severity


# First part
ResetFirewall()
print("First part: " + str(ThrowPacket(0)))

# Second part
d = 0
while ThrowPacket(d)!=0:
    d += 1
    ResetFirewall()

print("Second part: " + str(d))
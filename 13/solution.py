input = [list(map(int,x.split(": "))) for x in open('data.txt').read().split("\n")]

class Scanner:

    max = 0
    layer = 0

    def __init__(self, max, layer):
        self.max = max
        self.layer = layer

    def isOnTop(self, t, delay):
        return (self.layer+delay) % ( (self.max-1)*2 ) == 0

firewall = [Scanner(x[1], x[0]) for x in input]

def ThrowPacket(delay, BreakIfSeen=False):
    severity = 0
    for t, x in enumerate(firewall):
        if x.isOnTop(t, delay):
            severity += x.layer * x.max
            if BreakIfSeen:
                severity = 1
                break
    return severity

# First part
print("First part: " + str(ThrowPacket(0)))

# SecondPart
d = 0
while ThrowPacket(d, True)!=0:
    d += 1
print("Second part: " + str(d))
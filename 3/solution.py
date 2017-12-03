input = int( open('data.txt', 'r').read() )

# PART 1 (not very efficient way)

# constants
DIR_RIGHT = 0
DIR_UP = 1
DIR_LEFT = 2
DIR_DOWN = 3

# location of the given number
x = 0
y = 0

# initial direction
DIR = 0

# how many steps in actual direction
MAX_STEPS = 1

STEPS = 0
DIR_CHANGES = 0


for i in range(1,input):
    if DIR==DIR_RIGHT:
        x = x+1
    if DIR==DIR_UP:
        y = y+1
    if DIR==DIR_LEFT:
        x = x-1
    if DIR==DIR_DOWN:
        y = y-1
    
    STEPS = STEPS+1
    if STEPS==MAX_STEPS:
        DIR_CHANGES = DIR_CHANGES+1
        DIR = (DIR+1)%4
        STEPS = 0
        if DIR_CHANGES%2==0:
            MAX_STEPS = MAX_STEPS+1

print("First part: " + str(abs(x)+abs(y)))



# Second part (spaghetti)

n = 20

tab = [ [0]*n for _ in range(0,n) ]

y = int(n/2)
x = y+1

tab[y][x-1] = 1       # initial value

DIR = 0
MAX_STEPS = 1
STEPS = 0
DIR_CHANGES = 0

while (x<=n and y<=n):
    tab[y][x] += (tab[y-1][x-1] if y>0 and x>0 else 0) + (tab[y-1][x] if y>0 else 0) + (tab[y-1][x+1] if y>0 and x<n else 0)
    tab[y][x] += (tab[y][x-1] if x>0 else 0) + (tab[y][x+1] if x<n else 0)
    tab[y][x] += (tab[y+1][x-1] if y<n and x>0 else 0) + (tab[y+1][x] if y<n else 0) + (tab[y+1][x+1] if y<n and x<n else 0)

    if tab[y][x] > input:
        print("Second part: " + str(tab[y][x]))
        break

    STEPS = STEPS+1
    if STEPS==MAX_STEPS:
        DIR_CHANGES = DIR_CHANGES+1
        DIR = (DIR+1)%4
        STEPS = 0
        if DIR_CHANGES%2==0:
            MAX_STEPS = MAX_STEPS+1

    if DIR==DIR_RIGHT:
        x = x+1
    if DIR==DIR_UP:
        y = y+1
    if DIR==DIR_LEFT:
        x = x-1
    if DIR==DIR_DOWN:
        y = y-1

# If You want to see Your square simply uncomment code below this line
#for line in tab:
#    print("\t".join(map(str,line)))
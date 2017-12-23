def isPrime(n):
    ans = True
    for i in range(2, n-1):
        if n%i == 0:
            ans = False
            break
    return ans

a, b, c, d, e, f, g, h = 1, 0, 0, 0, 0, 0, 0, 0

b = 93
c = b

b = b * 100
b = b + 100000
c = b
c = c + 17000

while True:
    f = 1
    while True:
    
    for d in range(2, b):
        for e in range(2,b):
            g = d * e - b
            if g == 0:
                f = 0

    if f == 0:
        h = h + 1
    g = b
    g = g - c
    if g == 0: break
    b = b - 17

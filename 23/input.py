a, b, c, d, e, f, g, h = 1, 0, 0, 0, 0, 0, 0, 0

b = 93
c = b

b = b * 100
b = b + 100000
c = b
c = c + 17000

while True:
    f = 1
    d = 2
    while True:
        e = 2

        while True:
            g = d
            g = g * e
            g = g - b
            if g == 0:
                f = 0
            e = e + 1
            g = e
            g = g - b
            if g == 0: break

        d = d + 1
        g = d
        g = g - b
        if g == 0: break

    if f == 0:
        h = h + 1
    g = b
    g = g - c
    if g == 0: break
    b = b - 17

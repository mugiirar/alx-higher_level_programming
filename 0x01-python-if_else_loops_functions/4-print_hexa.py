#!/usr/bin/python3

n = 0

while n <= 98:
    if n >= 0 and n <= 10:
        k = str(n)

    if n >= 10 and n <= 15:
        lett = "abcdef"

        k = lett[n - 10]

    if n > 15:

        p = str(int(n / 16))

        m = str(n % 16)

        k = p[0] + m
        if len(k) > 2:
            y = p[0]
            d = int(k[1] + k[2])

            if d >= 10 and d <= 15:
                letters = "abdcef"
                v = letters[d - 10]
                k = y + v

        l = str(n)

    print(str(n) + " = 0x" + k)
    n = int(n)
    n += 1

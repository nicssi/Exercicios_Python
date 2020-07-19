def computepay(h, r):
    if h > 40:
        p1 = horaextra(h, r)
    else:
        p1 = h * r
    return p1


def horaextra(h, r):
    return 1.5 * r * (h - 40) + (40 * r)


hr = float(input("Enter Hours:"))

rphr = float(input("Enter rate per hour:"))

p = computepay(hr, rphr)
print(p)

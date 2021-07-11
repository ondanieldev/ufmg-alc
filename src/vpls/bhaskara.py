from math import sqrt


def bhaskara(a, b, c):
    delta = b*b-4*a*c
    if delta < 0:
        return (None, None)
    root1 = (-1*b+sqrt(delta))/2*a
    root2 = (-1*b-sqrt(delta))/2*a
    return (root1, root2)

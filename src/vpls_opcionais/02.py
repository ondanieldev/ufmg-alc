from math import sqrt


def raio_circ(area):
    radius = sqrt(area/3.14)
    circunference = 2*3.14*radius
    return (radius, circunference)

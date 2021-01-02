import math


class TPTriangle:
    def __init__(self, a):
        self.a = a

    def print(self, a):
        if a > 0:
            print("side=", self.a)
        else:
            print("side<0")

    def s(self):
        return ((math.sqrt(3)) * (self.a ** 2)) / 4

    def p(self):
        return self.a * 3

    def compare(self, other):
        if (((math.sqrt(3)) * (self.a ** 2)) / 4) < (((math.sqrt(3)) * (other.a ** 2)) / 4):
            print("площа першого <")
        elif (((math.sqrt(3)) * (self.a ** 2)) / 4) > (((math.sqrt(3)) * (other.a ** 2)) / 4):
            print("площа першого >")
        else:
            print("equel")

    def __add__(self, item):
        return TPTriangle(self.a + item.a)

    def __sub__(self, item):
        return TPTriangle(self.a - item.a)

    def __mul__(self, number):
        return TPTriangle(self.a * number)


class Piramida(TPTriangle):
    def __init__(self, a, h):
        super().__init__(a)
        self.h = h

    def v(self):
        return ((super().s()) * self.h) * (1 / 3)


a = int(input("side of triangle="))
b = int(input("one more side of triangle="))
d = TPTriangle(a)
print(d.print(a))
print("s=", d.s())
print("p=", d.p())
c = TPTriangle(b)
d.compare(c)
summ = c+d
print(summ)
sub = c-d
print(sub)
number = int(input("number="))
mul = d * number
print(mul)

h = int(input("h="))
k = Piramida(a, h)
print("v=", k.v())

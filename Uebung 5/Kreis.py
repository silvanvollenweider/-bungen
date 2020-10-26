from figur import *
from Punkt import *
import math

class Kreis(Figur):
    def __init__(self, m, r):
        super().__init__("Kreis")
        self.m = m
        self.r = r

    def umfang(self):
        return self.r*2*math.pi

    def __str__(self):
        return f"{self.name}: {self.m}, {self.r}"

k = Kreis(Punkt(5,4), 6)
print(k)
print("Umfang Kreis:", k.umfang())
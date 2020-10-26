from figur import *
from Punkt import *
import math

class Dreieck(Figur):
    def __init__(self, punkte):
        super().__init__("Dreieck")
        self.punkte = []
        for i in punkte:
            self.punkte.append((i.x,i.y))

    def umfang(self):
        return super().umfang(Punkt.umfangberechnung(self, self.punkte))


d = Dreieck([Punkt(2,3), Punkt(4,5), Punkt(2,7)])
print(d)
print(d.umfang())
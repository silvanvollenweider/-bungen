from figur import *
from Punkt import *
import math

class Rechteck(Figur):
    def __init__(self, punkte):
        super().__init__("Rechteck")
        self.punkte = []
        for i in punkte:
            self.punkte.append((i.x, i.y))

    def umfang(self):
        return super().umfang(Punkt.umfangberechnung(self, self.punkte))




re = Rechteck([Punkt(1,1), Punkt(4,4)])
print(re)
print(re.umfang())
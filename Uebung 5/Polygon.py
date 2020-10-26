from figur import *
from Punkt import *

class Polygon(Figur):
    def __init__(self, punkte):
        super().__init__("Polygon")
        self.punkte = []
        for i in punkte:
            self.punkte.append((i.x, i.y))


    def umfang(self):
        return super().umfang(Punkt.umfangberechnung(self, self.punkte))



pp = Polygon([Punkt(0,0), Punkt(1,0), Punkt(1,1), Punkt(0,1)])
print(pp)
print(pp.umfang())
import math
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def umfangberechnung(self, punkte):
        if len(punkte) == 2:
            p1 = Punkt(punkte[0][0], punkte[0][1])
            p2 = Punkt(punkte[1][0], punkte[1][1])
            u = 2 * abs(p2.x - p1.x) + 2 * abs(p2.y - p1.y)
            return round(u, 2)
        u = 0
        for i in range(0, len(punkte)):
            u += math.sqrt((punkte[i - 1][0] - punkte[i][0]) ** 2 + (punkte[i - 1][1] - punkte[i][1]) ** 2)
        return round(u, 2)

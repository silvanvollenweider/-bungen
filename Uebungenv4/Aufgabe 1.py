class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return Vector3(self.x * other, self.y * other, self.z * other)
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other):
        if type(other) == float or type(other) == int:
            return Vector3(self.x * other, self.y * other, self.z * other)
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    def normalize(self):
        k = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        return Vector3(round(self.x / k, 2), round(self.y / k, 2), round(self.z / k, 2))


f1 = Vector3(3, 5, 3)
f2 = Vector3(1, 2, 1)
v = 10.5

#a = f1 + f2
#a = f1 - f2
#a = f1 * v
#a = v * f1
#a = f1.dot(f2)
#a = f1.cross(f2)
#a = f1.normalize()
print(a)

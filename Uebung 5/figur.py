class Figur:
    def __init__(self, name):
        self.name = name

    def flaeche(self):
        return 0.0

    def umfang(self, u):
        return f"Umfang {self.name}: {u}"
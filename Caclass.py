class Victor():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.vicself = (a, b)

    def plus(self, other):
        return Victor(self.a + other.a, self.b + other.b)

Va = Victor(1, 2)
Vb = Victor(2, 3)

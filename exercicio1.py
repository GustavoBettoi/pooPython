import math

class Circle:
    def __init__(self, O, r):
        self.O = O
        self.r = r

    def calcularArea(self):
        return math.pi*self.r**2

    def calcularPerimetro(self):
        return math.pi*self.r*2
    
    def test_pertencente(self, A):
        if ((self.O[0] - A[0])**2 + (self.O[1] - A[1])**2)**0.5 <= self.r:
            return True
        else:
            return False

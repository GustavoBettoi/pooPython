class Domino:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mostrar_pontos(self):
        return f"Lado A: {self.a} Lado B: {self.b}"
    
    def valor(self):
        return self.a + self.b
    
    def __str__(self):
        return (self.a, self.b)
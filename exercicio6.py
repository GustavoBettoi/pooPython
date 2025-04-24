from abc import ABC, abstractmethod
import math


class FiguraGeometrica(ABC):

    def __init__(self, nome):
        self.nome = nome 
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass 

class Circulo(FiguraGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def area(self):
        return math.pi*self.raio**2
    
    def perimetro(self):
        return math.pi*2*self.raio
    

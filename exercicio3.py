import datetime

data = datetime.datetime.now()


class Funcionario:
    def __init__(self, codigo, sobrenome, nome, dataNasc, dataAd, salario):
        params = locals()
        del params['self']
        self.__dict__.update(params)
    
    def idade(self):
        return data.year - self.dataNasc[2]
    
    def tempoDeCasa(self):
        return data.year - self.dataAd[2]
    
    def aumentarSalario(self):
        if self.tempoDeCasa() < 5:
            self.salario *= 1.02
        elif self.tempoDeCasa()<10:
            self.salario *= 1.05
        else:
            self.salario *= 1.1

    def mostrarFuncionario(self):
        lista = f"""Número: {self.codigo}\nSobrenome: {self.sobrenome}\nnome: {self.nome} \nidade: {self.idade()}\nTempo de casa: {self.tempoDeCasa()}\nsalario: {self.salario:.2f}
        """
        return lista
    

pedro = Funcionario(131, "oliveira", "pedro", (10, 10, 2000), (10, 10, 2015), 1000)

print(pedro.mostrarFuncionario())
class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def _validar_preco(self, preco):
        return preco > 0

    def alterar_preco(self, novo_preco):
        if self._validar_preco(novo_preco):
            self.__preco = novo_preco
        else:
            print("Erro: O preço deve ser maior que zero.")

    def vender(self, quantidade):
        if quantidade > 0 and self.__estoque >= quantidade:
            self.__estoque -= quantidade
        elif quantidade <= 0:
            print("Erro: Quantidade de venda inválida.")
        else:
            print("Erro: Estoque insuficiente!")

    def reabastecer(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
        else:
            print("Erro: Quantidade de reabastecimento inválida.")

    def exibir_detalhes(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: {self.__preco:.2f}")
        print(f"Estoque: {self.__estoque}")

    def __str__(self):
        return f"Produto: {self.__nome}"


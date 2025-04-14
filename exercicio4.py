class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
        else:
            print("Erro: Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
        elif valor <= 0:
            print("Erro: Valor de saque inválido.")
        else:
            print("Erro: Saldo insuficiente!")

    def exibir_saldo(self):
        return self._saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_titular):
        if novo_titular and novo_titular.strip():
            self._titular = novo_titular.strip()
        else:
            print("Erro: Nome do titular não pode ser vazio!")

    def __str__(self):
        return f"Conta de {self._titular}"


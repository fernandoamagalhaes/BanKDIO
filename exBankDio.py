class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.historico_transacoes = []
        self.saques_realizados_hoje = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico_transacoes.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 500:
            print("Limite de saque excedido. O limite é de R$ 500 por saque.")
        elif self.saques_realizados_hoje >= 3:
            print("Limite de saques diários excedido.")
        elif self.saldo >= valor:
            self.saldo -= valor
            self.historico_transacoes.append(f"Saque: R$ {valor:.2f}")
            self.saques_realizados_hoje += 1
        else:
            print("Saldo insuficiente para saque.")

    def exibir_extrato(self):
        if self.historico_transacoes:
            for transacao in self.historico_transacoes:
                print(transacao)
            print(f"Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")

# Uso do sistema bancário
conta = ContaBancaria()
conta.depositar(1500)
conta.sacar(300)
conta.sacar(200)
conta.exibir_extrato()

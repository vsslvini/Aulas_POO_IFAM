class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # atributo privado
        self.__saldo = saldo_inicial  

    # Destruidor 
    def __del__(self):
        print(f"Objeto destruído...")
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultarSaldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")
from conta_bancaria import ContaBancaria
 
# Classe principal da aplicação
class Main:
    
    def __init__(self):
        pass    
        
    def executar(self):
        contaBancaria = ContaBancaria("Benevaldo", 100)
        contaBancaria.consultarSaldo()
        contaBancaria.depositar(50)
        contaBancaria.consultarSaldo()
        contaBancaria.sacar(60)
        contaBancaria.consultarSaldo()

# Inicia a execução do programa
app = Main()
app.executar()
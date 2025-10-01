from smartphone import Smartphone


# Classe principal da aplicação
class Main:

    def __init__(self):
        pass

    # Método público
    def executar(self):

        smartphone = Smartphone(numero="99187-1516", capacidade_gb=128,
                                modelo="Samsung S24")
        print(smartphone)
        print("\n--- Testando Ações ---")
        smartphone.acao_especifica()
        smartphone.desligar()


# Inicia a execução do programa
app = Main()
app.executar()

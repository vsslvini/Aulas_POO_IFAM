# Definição da primeira classe base
class Telefone:
    # Define funcionalidades básicas de um telefone (ligar/desligar).
    def __init__(self, numero):
        self.numero = numero
        print(f"Telefone ({self.numero}) inicializado.")

    def ligar(self, destino):
        # Método exclusivo do Telefone.
        print(f"Discando {destino} a partir de {self.numero}...")

    def desligar(self):
        # Método que pode ser chamado por qualquer dispositivo.
        print("Dispositivo: Desligando a função de comunicação.")

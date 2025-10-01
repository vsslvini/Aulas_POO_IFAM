# Definição da segunda classe base
class PlayerMusica:
    # Define funcionalidades básicas de um player de música (reproduzir/pausar)
    def __init__(self, capacidade_gb):
        self.capacidade = capacidade_gb
        print(f"Player de Música ({self.capacidade}GB) inicializado.")

    def reproduzir(self, faixa):
        # Método exclusivo do Player de Música.
        print(f"Reproduzindo: {faixa}")

    def desligar(self):
        # Método que pode ser chamado por qualquer dispositivo.
        print("Dispositivo: Desligando o módulo de áudio.")

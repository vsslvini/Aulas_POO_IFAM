# CLASSE FILHA com Herança Múltipla
from telefone import Telefone
from player_musica import PlayerMusica


class Smartphone(Telefone, PlayerMusica):
    # Smartphone herda de Telefone e PlayerMusica
    def __init__(self, numero, capacidade_gb, modelo):
        self.modelo = modelo
        # Chamando construtores das classes base.
        # É necessário chamar explicitamente todos
        # os construtores em herança múltipla.
        Telefone.__init__(self, numero)
        PlayerMusica.__init__(self, capacidade_gb)
        print(f"Smartphone '{self.modelo}' totalmente configurado.")

    def acao_especifica(self):
        # Demonstra o uso de métodos de ambas as classes base.
        self.ligar("99112-2030")
        self.reproduzir("Música: Samba do Aprendizado")

    # MÉTODO SOBRESCRITO usando a função super() para
    # chamar ambos os 'desligar'.
    def desligar(self):
        # Método que demonstra o MRO ao chamar
        # o método da primeira classe base.
        print(f"\n--- DESLIGAMENTO DO {self.modelo} ---")

        # 1. Chamada explícita à primeira classe na ordem (Telefone)
        Telefone.desligar(self)

        # 2. Chamada explícita à segunda classe na ordem (PlayerMusica)
        PlayerMusica.desligar(self)

        print("Smartphone desligado com sucesso.")

    # Função que retorna a forma que deseja-se exibir o objeto.
    def __str__(self):
        return (
            f"****************************************\n"
            f"SmartPhone:\n"
            f"Modelo    : {self.modelo}\n"
            f"Numero    : {self.numero}\n"
            f"Capacidade: {self.capacidade}\n"
            f"****************************************\n"
        )

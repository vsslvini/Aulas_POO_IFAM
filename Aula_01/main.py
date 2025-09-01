from Aula_01.aluno import Aluno

#Clsse principal da aplicação
class Main:
    aluno: Aluno

    def __init__(self):
        pass

    def executar(self):
        print("Programa executando...")
        self.aluno = self.entraDados()
        self.exibirDados()
        print("Programa finalizado...")

    def entraDados(self):
        print("Cadastro de Aluno")
        # Entrada de dados
        matricula = int(input("Digite a matricula: "))
        nome = input("Digite o nome ")
        idade = int(input("Digite a idade "))
        # IMPORTANTE: cria uma instância, em memória, do objeto aluno
        # a parit da Classe Aluno e retorna o objeto preenchido
        return Aluno(matricula, nome, idade)
    
    def exibirDados(self):
        print(self.aluno)


# Inicia a execução do programa

app = Main()
app.executar()
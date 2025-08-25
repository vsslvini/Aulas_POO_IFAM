'''
Comentário com multiplas linhas.

Definição de Classe Aluno com seus
respectivos Atributos e Métodos.
'''

class Aluno:
    #comentário de uma única linha
    #Declaração de atributos Classe
    instituicaoEnsino = "IFAM"

###############################################
# Implementações dos Métodos: Ações e Estados
###############################################

    #construtor
    def __init__(self, matricula: int, nome: str, idade: int):
        #Atribuição de Instancia:
        #Valores único para cada instância do Obejto

        self.matricula = matricula 
        self.nome = nome
        self.idade = idade
        print("******************************************************************************")
        print(f"ATENÇÃO: O Construtor é o primeiro método a ser executado automaticamente")
        print(f"Objeto Aluno criado com sucesso...")
        print("******************************************************************************")

    #destruidor
    def __del__(self):
        print("******************************************************************************")
        print(f"ATENÇÃO: O Destruidor é o último método a ser executado automaticamente")
        print("******************************************************************************")


    #Função que retorna a forma que deseja-se exibir o projeto.
    def __str__(self):
        return (
            f"******************************************\n"
            f"Objeto Aluno:\n"
            f"Matrícula: {self.matricula}\n"
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Instituição de Ensino: {self.instituicaoEnsino}\n"
            f"******************************************\n"
            )
    

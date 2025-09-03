from aluno import Aluno
 
# Classe principal da aplicação
class Main:
    
    def __init__(self):
        pass    
        
    # Método público    
    def executar(self):
        aluno:Aluno
        aluno = Aluno()
        self.__obterDados(aluno)
        
    # Método privado    
    def __obterDados(self,aluno):
        try:
            # Entrada do aluno
            print("Dados do Aluno:")
            aluno.matricula = int(input("Digite a matrícula: "))
            aluno.nome = input("Digite o nome: ")
            aluno.idade = int(input("Digite a idade: "))
            # Entrada de dados do Endereço do Aluno
            print("Dados do Endereço:")
            aluno.rua = input("Rua: ")
            aluno.numero = int(input("Numero: "))
            aluno.cep = int(input("CEP: "))
            aluno.bairro = input("Bairro: ")
            aluno.cidade = input("Cidade: ")
            aluno.uf = input("Estado: ")
            
            #Exibir os dados
            self.__exibirDados(aluno)
            
        except ValueError as e:
            print("Erro: ", e)
            
    def __exibirDados(self, aluno):
        print(aluno)

# Inicia a execução do programa
app = Main()
app.executar()


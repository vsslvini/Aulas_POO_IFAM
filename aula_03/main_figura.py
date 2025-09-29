from retangulo import Retangulo
from triangulo import Triangulo


# Classe principal da aplicação
class Main:

    def __init__(self):
        pass

    # Método público
    def executar(self):
        # Definir Objetos
        retangulo: Retangulo
        triangulo: Triangulo
        # Instanciar Objetos
        retangulo = Retangulo()
        triangulo = Triangulo()
        self.__obterDados(retangulo, triangulo)

    # Método privado
    def __obterDados(self, retangulo, triangulo):
        try:
            # Entrada de dados do Retanculo
            print("Dados do Retangulo:")
            retangulo.ladoMaior = int(input("Digite o valor do lado maior: "))
            retangulo.ladoMenor = int(input("Digite o valor do lado menor: "))
            print("Dados do Triangulo:")
            triangulo.ladoA = int(input("Digite o valor do A: "))
            triangulo.ladoB = int(input("Digite o valor do B: "))
            triangulo.base = int(input("Digite o valor da Base: "))
            # Exibir os dados
            self.__exibirDados(retangulo, triangulo)

        except ValueError as e:
            print("Erro: ", e)

    def __exibirDados(self, retangulo, triangulo):
        print(retangulo)
        print(triangulo)


# Inicia a execução do programa
app = Main()
app.executar()

# Importa as classes Triangulo e Retangulo de seus respectivos arquivos.
from triangulo import Triangulo
from retangulo import Retangulo


# Declaração da classe Main, que orquestra a execução do programa.
class Main:
    """
    Classe principal da aplicação, responsável por interagir com o usuário
    e utilizar as classes de figuras geométricas.
    """

    # Método que gerencia a entrada de dados e a exibição dos resultados.
    def executar(self):
        """
        Solicita ao usuário os dados para criar um Triângulo e um Retângulo,
        depois exibe a área e o desenho de cada um.
        """
        try:
            # Seção para coletar dados e processar o Triângulo.
            print("--- DADOS DO TRIÂNGULO ---")
            # Solicita ao usuário que insira os valores para o triângulo.
            base = input("Digite o valor da base: ")
            altura = input("Digite o valor da altura: ")
            ladoA = input("Digite o valor do lado A: ")
            ladoB = input("Digite o valor do lado B: ")

            # Cria uma (objeto) da classe Triangulo com os dados
            # fornecidos.
            triangulo = Triangulo(ladoA, ladoB, base, altura)

            # Seção para coletar dados e processar o Retângulo.
            print("\n--- DADOS DO RETÂNGULO ---")
            # Solicita ao usuário que insira os valores para o retângulo.
            largura = input("Digite o valor da largura: ")
            comprimento = input("Digite o valor do comprimento: ")

            # Cria uma instância (objeto) da classe Retangulo com os dados
            # fornecidos.
            retangulo = Retangulo(largura, comprimento)

            # Exibe os dados da figura Triangulo.
            print(triangulo)
            # Exibe os dados da figura Retangulo.
            print(retangulo)

        # Bloco de tratamento de exceção.
        # Se o usuário digitar um valor não numérico, um ValueError será
        # lançado.
        except ValueError:
            # Informa ao usuário que a entrada foi inválida.
            print("\nErro: Insira apenas valores numéricos válidos.")
        # Bloco de exceção genérico para outros possíveis erros.
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")


# Este é o ponto de entrada do programa.
# A condição __name__ == "__main__" verifica se o script está sendo executado
# diretamente.
if __name__ == "__main__":
    # Cria uma instância da classe Main.
    app = Main()
    # Chama o método entradaDados() para iniciar a aplicação.
    app.executar()

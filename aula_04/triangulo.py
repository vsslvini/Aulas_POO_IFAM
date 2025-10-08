# Importa a classe abstrata FiguraGeometrica do arquivo figura_geometrica.py
from figura_geometrica import FiguraGeometrica


# Declaração da classe concreta Triangulo, que herda da classe
# FiguraGeometrica.
class Triangulo(FiguraGeometrica):
    """
    Classe concreta que representa uma figura geométrica do tipo Triângulo.
    Herda de FiguraGeometrica e implementa seus métodos abstratos.
    """

    """
    Python não suporta Polimorfismo de sobrecarga de métodos de forma nativa.
    Quando você define dois métodos com o mesmo nome
    (como exemplo __init__ ) na mesma classe, o último
    método definido simplesmente sobrescreve o anterior.
    """

    # Método construtor da classe Triangulo.
    def __init__(self, ladoA: float, ladoB: float, base: float, altura: float):
        # Chama o construtor da classe pai (FiguraGeometrica) usando super().
        # Define o nome da figura como "Triângulo".
        super().__init__("Triângulo")
        # Define os atributos privados da classe Triangulo.
        # A função float() garante que os valores sejam numéricos do tipo real.
        self.__ladoA = float(ladoA)
        self.__ladoB = float(ladoB)
        self.__base = float(base)
        self.__altura = float(altura)

    # Implementação do método area() para o Triangulo.
    # Este método foi declarado como abstrato na classe pai.
    # (Polimorfismo: Sobreposição​).
    def area(self) -> float:
        """
        Calcula a área do triângulo usando a fórmula: (base * altura) / 2.
        Retorna:
            float: O valor da área calculada.
        """
        # Retorna o resultado do cálculo da área.
        return (self.__base * self.__altura) / 2

    # Implementação do método desenhar() para o Triangulo.
    # Este método também foi declarado como abstrato na classe pai.
    # (Polimorfismo: Sobreposição​).
    def desenhar(self) -> str:
        """
        Imprime uma representação textual (ASCII art) de um triângulo no
        console.
        """
        # Imprime o desenho da figura no console.
        return (
            "Desenho da figura: Triângulo\n"
            "   /\\ \n"
            "  /  \\ \n"
            " /____\\ \n"
        )

    # Método especial que retorna uma representação em string do objeto.
    # É chamado automaticamente pela função print().
    # (Polimorfismo: Sobreposição​).
    def __str__(self) -> str:
        """
        Retorna uma string que descreve o objeto Triangulo, incluindo
        seu nome, base, altura e área calculada.
        """
        # Retorna uma string formatada com as informações do objeto.
        # self.nome, self.area() e self.desenhar() chamam os métodos da
        # própria instância.
        return (
            f"****************************************\n"
            f"Figura Geométrica:\n"
            f"Nome: {super().nome}\n"
            f"Lado A: {self.__ladoA}\n"
            f"Lado B: {self.__ladoB}\n"
            f"Base  : {self.__base}\n"
            f"Altura: {self.__altura}\n"
            f"Area  : {self.area():.2f}\n"
            f"{self.desenhar()}\n"
            f"****************************************\n"
        )

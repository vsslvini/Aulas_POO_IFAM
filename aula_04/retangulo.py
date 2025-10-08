# Importa a classe abstrata FiguraGeometrica do arquivo figura_geometrica.py
from figura_geometrica import FiguraGeometrica


# Declaração da classe concreta Retangulo, que herda da classe
# FiguraGeometrica.
class Retangulo(FiguraGeometrica):
    """
    Classe concreta que representa uma figura geométrica do tipo Retângulo.
    Herda de FiguraGeometrica e implementa seus métodos abstratos.
    """

    """
    Python não suporta Polimorfismo de sobrecarga de métodos de forma nativa.
    Quando você define dois métodos com o mesmo nome
    (como exemplo __init__ ) na mesma classe, o último
    método definido simplesmente sobrescreve o anterior.
    """

    # Método construtor da classe Retangulo.
    def __init__(self, largura: float, comprimento: float):
        # Chama o construtor da classe pai (FiguraGeometrica) usando super().
        # Define o nome da figura como "Retângulo".
        super().__init__("Retângulo")
        # Define os atributos privados da classe Retangulo.
        self.__largura = float(largura)
        self.__comprimento = float(comprimento)

    # Implementação do método area() para o Retangulo
    # (Polimorfismo: Sobreposição​).
    def area(self) -> float:
        """
        Calcula a área do retângulo usando a fórmula: largura * comprimento.
        Retorna:
            float: O valor da área calculada.
        """
        # Retorna o resultado do cálculo da área.
        return self.__largura * self.__comprimento

    # Implementação do método desenhar() para o Retangulo.
    # (Polimorfismo: Sobreposição​).
    def desenhar(self) -> str:
        """
        Imprime uma representação textual (ASCII art) de um retângulo no
        console.
        """
        # Imprime o desenho da figura no console.
        return (
            "Desenho da figura: Retângulo\n"
            " ______ \n"
            "|      |\n"
            "|______|\n"
        )

    # Método especial que retorna uma representação em string do objeto.
    # É chamado automaticamente pela função print().
    # (Polimorfismo: Sobreposição​).
    def __str__(self) -> str:
        # Retorna uma string que descreve o objeto Retangulo
        return (
            f"****************************************\n"
            f"Figura Geométrica:\n"
            f"Nome: {super().nome}\n"
            f"Largura: {self.__largura}\n"
            f"Comprimento: {self.__comprimento}\n"
            f"Area  : {self.area():.2f}\n"
            f"{self.desenhar()}\n"
            f"****************************************\n"
        )

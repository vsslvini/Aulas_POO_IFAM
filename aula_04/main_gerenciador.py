from figura_geometrica import FiguraGeometrica
from retangulo import Retangulo
from triangulo import Triangulo
from gerenciador_figuras import GerenciadorDeFiguras


if __name__ == "__main__":
    # 1. Criar instâncias das classes concretas (subtipos)
    retangulo = Retangulo(largura=10, comprimento=5)
    triangulo = Triangulo(ladoA=3, ladoB=4, base=6, altura=5)
    # Você poderia criar mais figuras aqui (Círculo, Quadrado, etc.)

    # 2. Criar uma lista de Figuras Geométricas
    # Note que a lista armazena o tipo base (FiguraGeometrica),
    # mas contém instâncias de seus subtipos.
    todas_as_figuras: list[FiguraGeometrica] = [retangulo, triangulo]

    # 3. Instanciar o Gerenciador de Figuras
    gerenciador = GerenciadorDeFiguras()

    # 4. Demonstrar os métodos com Polimorfismo de Subtipo

    print("Demonstrando apresentação individual (Polimorfismo de Subtipo)")
    gerenciador.apresentar_figura(retangulo)
    gerenciador.apresentar_figura(triangulo)

    print("\nDemonstrando cálculo de área total (Polimorfismo de Subtipo)")
    area_total = gerenciador.calcular_area_total(todas_as_figuras)
    print(f"\nResultado final da área total: {area_total:.2f}")

    print("\nDemonstrando todas as figuras (Polimorfismo de Subtipo)")
    gerenciador.desenhar_todas_as_figuras(todas_as_figuras)

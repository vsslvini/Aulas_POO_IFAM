# gerenciador_figuras.py

# Importa a classe abstrata (o tipo base)
from figura_geometrica import FiguraGeometrica
# Não precisamos importar Retangulo ou Triangulo aqui,
# pois o método opera sobre o tipo base FiguraGeometrica.


class GerenciadorDeFiguras:
    """
    Classe utilitária para demonstrar o Polimorfismo de Subtipo.
    Seus métodos operam sobre objetos do tipo FiguraGeometrica,
    independentemente de serem Retangulo, Triangulo, ou outros.
    """

    def apresentar_figura(self, figura: FiguraGeometrica):
        """
        Apresenta as informações de uma figura geométrica.
        Demonstra Polimorfismo de Subtipo e de Sobreposição,
        pois chama métodos específicos da subclasse.
        """
        print("\n=== APRESENTAÇÃO DA FIGURA ===")
        print("Tipo genérico esperado: FiguraGeometrica")
        print(f"Tipo real do objeto: {type(figura).__name__}")
        # Chama o __str__ específico do subtipo
        print(figura)
        # Chama o area() específico do subtipo
        print(f"Área calculada: {figura.area():.2f}")
        # Chama o desenhar() específico do subtipo
        print(figura.desenhar())
        print("==============================")

    def calcular_area_total(self, figuras: list[FiguraGeometrica]) -> float:
        """
        Calcula a área total de uma lista de figuras geométricas.
        Este método é um excelente exemplo de Polimorfismo de Subtipo,
        pois itera sobre um tipo base (FiguraGeometrica) e delega
        a execução do método area() a cada subtipo.
        """
        area_total = 0.0
        print("\n--- CALCULANDO ÁREA TOTAL ---")
        for i, figura in enumerate(figuras):
            # Polimorfismo de Subtipo em ação!
            area_da_figura = figura.area()
            print(f"  Figura {i+1} ({figura.nome}): {area_da_figura:.2f}")
            area_total += area_da_figura
        print(f"--- Área total combinada: {area_total:.2f} ---")
        return area_total

    def desenhar_todas_as_figuras(self, figuras: list[FiguraGeometrica]):
        """
        Desenha todas as figuras geométricas de uma lista.
        Outro exemplo de Polimorfismo de Subtipo, chamando desenhar()
        em diferentes subtipos.
        """
        print("\n--- DESENHANDO TODAS AS FIGURAS ---")
        for i, figura in enumerate(figuras):
            print(f"\n--- Desenho da Figura {i+1} ({figura.nome}) ---")
            # Polimorfismo de Subtipo em ação!
            print(figura.desenhar())
        print("--- FIM DO DESENHO ---")

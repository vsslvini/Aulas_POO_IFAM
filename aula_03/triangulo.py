from dataclasses import dataclass
from figura_geometrica import FiguraGeometrica


# SubClasse: Triangulo
# SuperClasse: FiguraGeometrica
@dataclass
class Triangulo(FiguraGeometrica):
    _ladoA: int = 0
    _ladoB: int = 0
    _base: int = 0

    def __init__(self, nome: str = "Triangulo"):
        super().__init__(nome)
        self._ladoA = 0
        self._ladoB = 0
        self._base = 0

    @property
    def ladoA(self):
        return self._ladoA

    @ladoA.setter
    def ladoA(self, value):
        # Verifica se o valor é inteiro e maior que Zero
        if isinstance(value, int) and value > 0:
            self._ladoA = value
        else:
            raise ValueError(
                "O valor do lado A deve ser um inteiro positivo."
                )

    @property
    def ladoB(self):
        return self._ladoB

    @ladoB.setter
    def ladoB(self, value):
        # Verifica se o valor é inteiro e maior que Zero
        if isinstance(value, int) and value > 0:
            self._ladoB = value
        else:
            raise ValueError(
                "O valor do lado B deve ser um inteiro positivo."
                )

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        # Verifica se o valor é inteiro e maior que Zero
        if isinstance(value, int) and value > 0:
            self._base = value
        else:
            raise ValueError(
                "O valor da base deve ser um inteiro positivo."
                )

    # Função que retorna a forma que deseja-se exibir o objeto.
    def __str__(self):
        return (
            f"****************************************\n"
            f"Figura Geométrica:\n"
            f"Nome: {super().__str__()}"
            f"Lado A: {self.ladoA}\n"
            f"Lado B: {self.ladoB}\n"
            f"Base  : {self.base}\n"
            f"****************************************\n"
        )

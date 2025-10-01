from figura_geometrica import FiguraGeometrica


class Retangulo(FiguraGeometrica):
    def __init__(self, nome: str = "Retângulo"):
        super().__init__(nome)
        self._ladoMaior = 0
        self._ladoMenor = 0

    @property
    def ladoMaior(self):
        return self._ladoMaior

    @ladoMaior.setter
    def ladoMaior(self, value):
        if isinstance(value, int) and value > 0:
            self._ladoMaior = value
        else:
            raise ValueError(
                "O valor do lado maior deve ser um inteiro positivo."
                )

    @property
    def ladoMenor(self):
        return self._ladoMenor

    @ladoMenor.setter
    def ladoMenor(self, value):
        if isinstance(value, int) and value > 0:
            self._ladoMenor = value
        else:
            raise ValueError(
                "O valor do lado menor deve ser um inteiro positivo."
                )

    def __str__(self):
        return (
            f"****************************************\n"
            f"Figura Geométrica:\n"
            f"Nome: {self.nome}\n"
            f"Maior Lado: {self.ladoMaior}\n"
            f"Menor Lado: {self.ladoMenor}\n"
            f"****************************************\n"
        )

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
    def ladoMaior(self, maiorLado):
        if isinstance(maiorLado, int) and maiorLado > 0 and maiorLado > self._ladoMenor:
            self._ladoMaior = maiorLado
        else:
            raise ValueError(
                "O valor do lado maior deve ser um inteiro positivo e MAIOR que o lado MENOR."
                )

    @property
    def ladoMenor(self):
        return self._ladoMenor

    @ladoMenor.setter
    def ladoMenor(self, menorLado):
        if isinstance(menorLado, int) and menorLado > 0 and menorLado < self._ladoMaior:
            self._ladoMenor = menorLado
        else:
            raise ValueError(
                "O valor do lado menor deve ser um inteiro positivo e MENOR que o lado MAIOR."
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

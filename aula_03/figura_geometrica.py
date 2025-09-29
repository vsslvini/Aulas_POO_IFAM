from abc import ABC


class FiguraGeometrica(ABC):
    def __init__(self, nome: str = ""):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return f"Nome: {self.nome}\n"

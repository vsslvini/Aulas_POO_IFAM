# Importa os módulos ABC (Abstract Base Class) e abstractmethod do pacote abc
# ABC é usada como uma metaclasse para criar classes abstratas.
# abstractmethod é um decorador para indicar métodos abstratos.
from abc import ABC, abstractmethod


# Declaração da classe abstrata FiguraGeometrica, que herda de ABC.
# Uma classe abstrata não pode ser instanciada diretamente.
class FiguraGeometrica(ABC):
    """
    Classe abstrata que serve como modelo para qualquer figura geométrica.
    Define os métodos e atributos que toda figura deve ter.
    """

    # Método construtor da classe. É chamado quando um objeto é criado.
    # O parâmetro 'self' se refere à instância do objeto.
    def __init__(self, nome: str):
        # Define um atributo "privado" chamado __nome.
        # O duplo underscore (__) indica que o atributo não deve ser acessado
        # diretamente de fora da classe.
        self.__nome = nome

    # O decorador @property permite acessar um método como se fosse
    # um atributo.
    # Este é um método "getter" para o atributo __nome, permitindo sua leitura
    # de forma segura.
    @property
    def nome(self) -> str:
        # Retorna o valor do atributo privado __nome.
        return self.__nome

    # Decorador que define o método area() como um método abstrato.
    # Classes filhas concretas SÃO OBRIGADAS a implementar este método.
    @abstractmethod
    def area(self) -> float:
        # 'pass' indica que o método não tem implementação nesta classe.
        pass

    # Decorador que define o método desenhar() como um método abstrato.
    # Classes filhas concretas SÃO OBRIGADAS a implementar este método.
    @abstractmethod
    def desenhar(self) -> str:
        # 'pass' indica que o método não tem implementação nesta classe.
        pass

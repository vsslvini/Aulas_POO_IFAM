from abc import ABC
from dataclasses import dataclass
# from typing import Optional
from datetime import datetime
from dateutil.relativedelta import relativedelta
from endereco import Endereco

# ABC: Define uma Classe Abstrada
# SuperClasse


@dataclass
class Pessoa(ABC):
    _nome: str = ""
    # 'DD-MM-YYYY'
    _dataNascimento: str = ""
    # Definir o atributo endereço como NULO
    _endereco = Endereco()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        # Verifica se o valor é string e não é Vazio
        if isinstance(value, str) and value.strip():
            self._nome = value
        else:
            raise ValueError("Nome deve ser uma string não vazia.")

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @dataNascimento.setter
    def dataNascimento(self, value):
        # Verifica se o valor é string e não é Vazio
        if isinstance(value, str) and value.strip():
            self._dataNascimento = value
        else:
            raise ValueError(
                "Data de nascimento deve ser uma string não vazia."
                )

    @property
    def idade(self):
        return self.calcularIdadeCompleta(self._dataNascimento)

    # Delegação: Através da classe Pessoar obter os dados da classe Endereço de
    # forma encapsulada.
    @property
    def rua(self):
        return self._endereco.rua

    @rua.setter
    def rua(self, value):
        self._endereco.rua = value

    @property
    def numero(self):
        return self._endereco.numero

    @numero.setter
    def numero(self, value):
        self._endereco.numero = value

    @property
    def cep(self):
        return self._endereco.cep

    @cep.setter
    def cep(self, value):
        self._endereco.cep = value

    @property
    def bairro(self):
        return self._endereco.bairro

    @bairro.setter
    def bairro(self, value):
        self._endereco.bairro = value

    @property
    def cidade(self):
        return self._endereco.cidade

    @cidade.setter
    def cidade(self, value):
        self._endereco.cidade = value

    @property
    def uf(self):
        return self._endereco.uf

    @uf.setter
    def uf(self, value):
        self._endereco.uf = value

    # Função que retorna a forma que deseja-se exibir o objeto.
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Data Nascimento: {self.dataNascimento}\n"
            f"Idade: {self.idade}\n"
            f"Endereço:\n"
            f"Rua: {self.rua}\n"
            f"Numero: {self.numero}\n"
            f"CEP: {self.cep}\n"
            f"Bairro: {self.bairro}\n"
            f"Cidade: {self.cidade}\n"
            f"Estado: {self.uf}\n"
            )

    def calcularIdadeCompleta(self, data_nascimento: str) -> str:
        """
        Calcula a idade completa (anos, meses e dias) a partir
        da data de nascimento.
        Parâmetros:
        - data_nascimento (str): Data no formato 'YYYY-MM-DD'
        Retorna:
        - str: Idade formatada como 'X anos, Y meses e Z dias'
        """
        nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()
        hoje = datetime.today().date()
        # Calcular a diferença entre as datas
        diferenca = relativedelta(hoje, nascimento)
        return (
         f"{diferenca.years} anos, "
         f"{diferenca.months} meses e "
         f"{diferenca.days} dias"
        )

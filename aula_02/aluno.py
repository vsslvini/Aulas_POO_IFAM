from dataclasses import dataclass, field
from typing import Optional
from endereco import Endereco 


@dataclass
class Aluno:
    _matricula: int = 0
    _nome: str = ""
    _idade: int = 0
    # Definir o atributo endereço como NULO
    # _endereco: Optional[Endereco] = None  
    _endereco = Endereco()  

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        # Verifica se o valor é inteiro e maior que Zero
        if isinstance(value, int) and value > 0:
            self._matricula = value
        else:
            raise ValueError("Matrícula deve ser um inteiro positivo.")

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
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        # Verifica se o valor é inteiro e maior que Zero
        if isinstance(value, int) and value > 0:
            self._idade = value
        else:
            raise ValueError("Idade deve ser um inteiro positivo.")

    # Delegação: Através da classe Aluno obter os dados da classe Endereço de
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
            f"****************************************\n"
            f"Aluno:\n"
            f"Matrícula: {self.matricula}\n"
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Endereço:\n"
            f"Rua: {self.rua}\n"
            f"Numero: {self.numero}\n"
            f"CEP: {self.cep}\n"
            f"Bairro: {self.bairro}\n"
            f"Cidade: {self.cidade}\n"
            f"Estado: {self.uf}\n"
            f"****************************************\n"
            )
    
    

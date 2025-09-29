from dataclasses import dataclass
from pessoa import Pessoa


# SubClasse: Aluno
# SuperClasse: Pessoa
# class Aluno(Pessoa): indica a Herança entre a SubClasse Aluno
# e a SuperClasse Pessoa
@dataclass
class Aluno(Pessoa):
    _matricula: int = 0

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

    # Função que retorna a forma que deseja-se exibir o objeto.
    def __str__(self):
        _dadosPessoa: str = ""
        # ATENÇÃO: A função super() acessar atributo e método da SuperClasse
        _dadosPessoa = super().__str__()
        return (
            f"****************************************\n"
            f"Aluno:\n"
            f"Matrícula: {self.matricula}\n"
            f"{_dadosPessoa}\n"
            f"****************************************\n"
            )

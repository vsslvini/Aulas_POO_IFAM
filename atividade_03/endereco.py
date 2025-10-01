from dataclasses import dataclass


@dataclass
class Endereco:
    _rua: str = ''
    _numero: int = 0
    _cep: int = 0
    _bairro: str = ''
    _cidade: str = ''
    _uf: str = ''

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, value):
        if isinstance(value, str) and value.strip():
            self._rua = value
        else:
            raise ValueError("Rua deve ser uma string não vazia.")

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if isinstance(value, int) and value > 0:
            self._numero = value
        else:
            raise ValueError("Número deve ser um inteiro positivo.")

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        if isinstance(value, int) and 1000000 <= value <= 99999999:
            self._cep = value
        else:
            raise ValueError("CEP deve ter entre 7 e 8 dígitos.")

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        if isinstance(value, str) and value.strip():
            self._bairro = value
        else:
            raise ValueError("Bairro deve ser uma string não vazia.")

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        if isinstance(value, str) and value.strip():
            self._cidade = value
        else:
            raise ValueError("Cidade deve ser uma string não vazia.")

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, value):
        if isinstance(value, str) and len(value) == 2 and value.isalpha():
            # Transforma em letra em MAIÚSCULA
            self._uf = value.upper()
            if not self._validar_uf(self._uf):
                raise ValueError("Unidade Federativa inválida.")
        else:
            raise ValueError("UF deve conter exatamente 2 letras.")

    def _validar_uf(self, sigla: str) -> bool:
        """
        Valida se a sigla informada corresponde a uma Unidade
          Federativa do Brasil.
        Parâmetros:
        - sigla (str): Sigla da UF (ex: 'AM', 'SP')
        Retorna:
        - bool: True se for uma UF válida, False caso contrário
        """
        ufs_validas = {
            'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
            'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
            'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
        }
        return sigla.upper() in ufs_validas

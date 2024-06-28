from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, Iterable


# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Augusto Pontes'

# Sequências 
lista: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Augusto']
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Luiz')

# Dicionários e conjuntos
MeuDict = Dict[str, Union[str, int, List[int]]]
pessoa: Dict[str, Union[str, int]] = {'nome': 'Augusto Pontes', 'sobrenome': 'Pontes', 'idade': 20}
pessoa2: MeuDict = {'nome': 'Augusto Pontes', 'sobrenome': 'Pontes', 'idade': 20, 'l': [1, 2]}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(321345)


def retorna_funcao(funcao: Callable[[], None]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return x + y

print(retorna_funcao(soma(10,20)))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} - {self.sobrenome} está falando...')

def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]

def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]

print(iterar([1,2,3]))
print(iterar(('a', 2, 3)))
print(iterar2([1,2,3]))
print(iterar2(('a', 2, 3)))
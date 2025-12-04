"""
Pacote aventura_pkg

Exporta funções/objetos principais para facilitar importação em main.py.
"""

from .labirinto import criar_labirinto, imprimir_labirinto, resolver_labirinto
from .jogador import Jogador, iniciar_jogador
from .utils import imprime_instrucoes, animacao_festa

__all__ = [
    "criar_labirinto"
    "imprimir_labirinto",
    "resolver_labirinto",
    "Jogador",
    "iniciar_jogador",
    "imprime_instrucoes",
    "animacao_festa",
]
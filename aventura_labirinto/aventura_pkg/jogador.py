"""
Define a classe Jogador e funções para iniciar e controlar a movimentação e pontuação.
"""

from typing import Tuple

class Jogador:
    def __init__(self, x: int = 1, y: int = 1):
        self.x = x
        self.y = y
        self.pontos = 0
        self.itens_coletados = 0

    def posicao(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def mover(self, dx: int, dy: int, lab: list) -> bool:
        """
        Tenta mover o jogador. Retorna True se movimento ocorreu, False caso haja parede.
        """
        nx = self.x + dx
        ny = self.y + dy

        # limites
        if ny < 0 or ny >= len(lab) or nx < 0 or nx >= len(lab[0]):
            return False

        # parede
        if lab[ny][nx] == "#":
            return False

        # coletou item?
        # coleta item (corrigido)
        if lab[ny][nx] == "P":
            self.itens_coletados += 1
            self.pontos += 10
            lab[ny][nx] = " "   # ← remove o item do labirinto!

        # mover jogador
        self.x = nx
        self.y = ny
        return True

    def pontuar(self, valor: int) -> None:
        self.pontos += valor


def iniciar_jogador(x: int = 1, y: int = 1) -> Jogador:
    """Cria e retorna um jogador na posição inicial."""
    return Jogador(x, y)
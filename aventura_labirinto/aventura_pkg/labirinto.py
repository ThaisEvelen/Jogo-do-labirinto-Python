"""
labirinto.py

Funções:
- criar_labirinto(dificuldade="facil", from_file=None) -> lista de listas (matriz)
- imprimir_labirinto(lab, jogador=None) -> imprime o labirinto na tela
- resolver_labirinto(lab, inicio, objetivo) -> retorna lista com caminho (recursiva) ou None
"""

from rich.console import Console
from typing import List, Optional, Tuple
import random
import copy

Console = Console()

def criar_labirinto(dificuldade: str = "facil", from_file: Optional[str] = None) -> List[List[str]]:
    """
    Cria um labirinto simples. Se from_file for passado, tenta ler um labirinto de arquivo.
    Dificuldade ajusta tamanho/obstáculos.
    Retorna uma matriz (lista de listas) com:
    '#' parede, ' ' espaço, 'S' saída, 'P' (opcional) para itens.
    """
    if from_file:
        with open(from_file, 'r', encoding='utf-8') as f:
            lines = [list(line.rstrip('\n')) for line in f]
        return lines

    # layouts pré-definidos
    if dificuldade == "facil":
        w, h, density = 9, 7, 0.12
    elif dificuldade == "medio":
        w, h, density = 15, 11, 0.18
    else:  # dificil
        w, h, density = 21, 13, 0.24

    # cria paredes externas
    lab = [["#" for _ in range(w)] for _ in range(h)]

    # preenche interior com espaços
    for y in range(1, h-1):
        for x in range(1, w-1):
            lab[y][x] = " " if random.random() > density else "#"

    # garante ponto inicial e saída
    lab[1][1] = " "          # posição inicial (1,1)
    lab[h-2][w-2] = "S"      # saída

    # opcional: colocar alguns itens 'P' para coletar
    for _ in range(max(1, (w*h)//40)):
        rx = random.randint(1, w-2)
        ry = random.randint(1, h-2)
        if lab[ry][rx] == " " and (rx, ry) not in [(1,1),(w-2,h-2)]:
            lab[ry][rx] = "P"

    return lab

def imprimir_labirinto(lab: List[List[str]], jogador = None) -> None:
    """
    Imprime o labirinto usando rich. jogador (objeto) pode ter atributos x,y.
    """
    Console.clear()
    for y, linha in enumerate(lab):
        linha_str = ""
        for x, cel in enumerate(linha):
            if jogador and (x, y) == (jogador.x, jogador.y):
                linha_str += "[bold green]@[/]"
            elif cel == "#":
                linha_str += "[grey37]#[/]"
            elif cel == "S":
                linha_str += "[bold magenta]S[/]"
            elif cel == "P":
                linha_str += "[yellow]P[/]"
            elif cel == ".":
                linha_str += "[dim].[/]"
            else:
                linha_str += " "
        Console.print(linha_str)

def resolver_labirinto(lab: List[List[str]], inicio: Tuple[int,int], objetivo: Tuple[int,int]) -> Optional[List[Tuple[int,int]]]:
    """
    Função recursiva que tenta achar um caminho do inicio até objetivo.
    Retorna lista de coordenadas (x,y) se encontrar, caso contrário None.
    OBS: recebe uma cópia do labirinto para marcar visitados sem modificar o original.
    """
    w = len(lab[0])
    h = len(lab)
    visited = [[False]*w for _ in range(h)]
    caminho = []

    def _rec(x: int, y: int) -> bool:
        # limites
        if x < 0 or x >= w or y < 0 or y >= h:
            return False
        if visited[y][x]:
            return False
        cell = lab[y][x]
        if cell == "#":
            return False

        visited[y][x] = True
        caminho.append((x,y))

        if (x,y) == objetivo:
            return True

        # tenta vizinhos (direita, esquerda, baixo, cima)
        if _rec(x+1, y): return True
        if _rec(x-1, y): return True
        if _rec(x, y+1): return True
        if _rec(x, y-1): return True

        # backtrack
        caminho.pop()
        return False

    if _rec(inicio[0], inicio[1]):
        return caminho
    return None
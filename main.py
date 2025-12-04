"""
main.py
Executável principal. Fornece CLI e menu interativo.
"""

import argparse
import os
import time
import sys
from rich.console import Console

# importações do pacote
from aventura_labirinto.aventura_pkg import (
    criar_labirinto,
    imprimir_labirinto,
    resolver_labirinto,
    iniciar_jogador,
    Jogador,
    imprime_instrucoes,
    animacao_festa,
    imprime_titulo,
    status_jogador,
    game_over_visual
)

console = Console()


def parse_args():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto - CLI")
    parser.add_argument("--name", type=str, required=True, help="Nome do(a) jogador(a)")
    parser.add_argument("--color", type=str, default="default", help="Cor principal do jogo (apenas rótulo)")
    parser.add_argument("--dificuldade", type=str, choices=["facil","medio","dificil"], default="facil")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa sons (se houver)")
    parser.add_argument("--auto", action="store_true", help="Executa solução automática do labirinto")
    return parser.parse_args()


def menu_interativo(args):
    console.clear()
    imprime_titulo()  # 🎉 título estilizado

    nome = args.name
    console.print(f"[bold cyan]Bem vinda(o), {nome}![/]\n")

    while True:
        console.print("[bold magenta]Menu[/]")
        console.print("1 - Jogar")
        console.print("2 - Instruções")
        console.print("3 - Resolver automaticamente (mostrar caminho)")
        console.print("4 - Sair")

        opc = input("Escolha: ").strip()

        match opc:
            case "1":
                jogar(args)
            case "2":
                imprime_instrucoes()
            case "3":
                lab = criar_labirinto(args.dificuldade)
                inicio = (1,1)
                objetivo = None

                # encontrar a saída
                for y, row in enumerate(lab):
                    for x, cell in enumerate(row):
                        if cell == "S":
                            objetivo = (x, y)

                caminho = resolver_labirinto(lab, inicio, objetivo)

                if caminho:
                    mark_lab = [list(r) for r in lab]
                    for (x,y) in caminho:
                        if mark_lab[y][x] == " ":
                            mark_lab[y][x] = "."
                    imprimir_labirinto(mark_lab)
                    console.print(f"[green]Caminho encontrado com {len(caminho)} passos.[/green]")
                else:
                    console.print("[red]Nenhum caminho encontrado.[/red]")

            case "4":
                console.print("[bold yellow]Até a próxima![/]")
                break

            case _:
                console.print("[red]Opção inválida[/]")


def jogar(args):
    lab = criar_labirinto(args.dificuldade)
    jogador = iniciar_jogador(1,1)

    jogadas_restantes = 30  # 🎮 limite de jogadas

    imprimir_labirinto(lab, jogador)
    status_jogador(jogador, jogadas_restantes)

    if args.auto:
        objetivo = None
        for y, row in enumerate(lab):
            for x, cell in enumerate(row):
                if cell == "S":
                    objetivo = (x, y)

        caminho = resolver_labirinto(lab, jogador.posicao(), objetivo)

        if caminho:
            for (x, y) in caminho:
                jogador.x, jogador.y = x, y
                imprimir_labirinto(lab, jogador)
                time.sleep(0.15)

            console.print("[bold green]🎉 Saída alcançada automaticamente![/]")
            animacao_festa(3)
        else:
            console.print("[red]Não foi possível resolver automaticamente.[/red]")
        return

    console.print("[dim]Use WASD + Enter para se mover. 'q' para sair.[/dim]")

    while True:
        imprimir_labirinto(lab, jogador)
        status_jogador(jogador, jogadas_restantes)

        comando = input("Mover (w/a/s/d) ou 'q': ").strip().lower()

        if comando == 'q':
            console.print("[yellow]Você desistiu.[/yellow]")
            break

        if comando == 'w':
            jogador.mover(0, -1, lab)
        elif comando == 's':
            jogador.mover(0, 1, lab)
        elif comando == 'a':
            jogador.mover(-1, 0, lab)
        elif comando == 'd':
            jogador.mover(1, 0, lab)
        else:
            console.print("[red]Comando inválido[/]")
            continue

        # reduzir jogadas
        jogadas_restantes -= 1

        # game over por falta de jogadas
        if jogadas_restantes <= 0:
            game_over_visual()
            return

        # checar vitória
        if lab[jogador.y][jogador.x] == "S":
            imprimir_labirinto(lab, jogador)
            console.print("[bold green]🎉 Você encontrou a saída!🏁[/]")
            status_jogador(jogador, jogadas_restantes)
            animacao_festa(4)
            break


if __name__ == "__main__":
    args = parse_args()
    menu_interativo(args)
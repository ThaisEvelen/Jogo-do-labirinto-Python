"""
main.py
Executável principal. Fornece CLI e menu interativo.
"""

import argparse
from aventura_labininto.aventura_pkg import (
    criar_labirinto,
    imprimir_labirinto,
    resolver_labirinto,
    iniciar_jogador,
    Jogador,
    imprime_instrucoes,
    animacao_festa
)
from rich.console import Console
import time
import sys

console = Console()

def parse_args():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto - CLI")
    parser.add_argument("--name", type=str, required=True, help="Nome do(a) jogador(a)")
    parser.add_argument("--color", type=str, default="default", help="Cor principal do jogo (apenas um rótulo)")
    parser.add_argument("--dificuldade", type=str, choices=["facil","medio","dificil"], default="facil", help="Dificuldade do labirinto")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa sons (se houver)")
    parser.add_argument("--auto", action="store_true", help="Executa solução automática do labirinto (chama resolver)")
    return parser.parse_args()

def menu_interativo(args):
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
                # encontra a saída 'S'
                for y,row in enumerate(lab):
                    for x,cell in enumerate(row):
                        if cell == "S":
                            objetivo = (x,y)
                if objetivo is None:
                    console.print("[red]Não foi possível encontrar a saída 'S' no labirinto gerado.[/red]")
                    continue
                caminho = resolver_labirinto(lab, inicio, objetivo)
                if caminho:
                    # imprime caminho marcado (faz uma cópia)
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

    # mostrar lab inicial
    imprimir_labirinto(lab, jogador)

    if args.auto:
        # executa solução automática, se pediram
        objetivo = None
        for y,row in enumerate(lab):
            for x,cell in enumerate(row):
                if cell == "S":
                    objetivo = (x,y)
        if objetivo is None:
            console.print("[red]Não foi possível encontrar a saída 'S' no labirinto gerado.[/red]")
            return
        caminho = resolver_labirinto(lab, jogador.posicao(), objetivo)
        if caminho:
            for (x,y) in caminho:
                # pausa e desenha passo a passo
                jogador.x, jogador.y = x, y
                imprimir_labirinto(lab, jogador)
                time.sleep(0.15)
            console.print("[bold green]🎉 Saída alcançada automaticamente![/]")
            animacao_festa(3)
        else:
            console.print("[red]Não foi possível resolver automaticamente.[/red]")
        return

    console.print("[dim]Use WASD + Enter para se mover (fallback). Se tiver 'keyboard' instalado e rodando como admin, o jogo pode ser adaptado para ler setas diretamente.[/dim]")

    # loop de jogo simples usando input (compatível em qualquer terminal)
    try:
        while True:
            imprimir_labirinto(lab, jogador)
            comando = input("Mover (w/a/s/d) ou 'q' para sair: ").strip().lower()
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

            # checar vitória
            if lab[jogador.y][jogador.x] == "S":
                imprimir_labirinto(lab, jogador)
                console.print("[bold green]🎉 Você encontrou a saída! Parabéns![/]")
                animacao_festa(4)
                break
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Jogo interrompido pelo usuário (CTRL+C). Voltando ao menu.[/]")
        return

if __name__ == "__main__":
    args = parse_args()
    menu_interativo(args)
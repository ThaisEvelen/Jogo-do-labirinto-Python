from rich.console import Console
console = Console()

def imprime_instrucoes(arquivo: str = None) -> None:
    """
    Imprime instruções do jogo. Se arquivo for passado, tenta ler o arquivo de texto.
    """
    if arquivo:
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                texto = f.read()
            console.print(texto)
            return
        except FileNotFoundError:
            console.print(f"[red]Arquivo de instruções '{arquivo}' não encontrado. Usando instruções padrão.[/red]")

    console.print("[bold underline]INSTRUÇÕES - Aventura no Labirinto[/]\n")
    console.print("Use as setas do teclado (ou WASD) para se mover.")
    console.print("Objetivo: encontre 'S' (a saída). Colete 'P' para ganhar pontos.\n")
    console.print("Comandos no menu: escolha 'Jogar' para começar, ou 'Resolver' para visualizar um caminho automático.\n")

def animacao_festa(rodadas: int = 5) -> None:
    """
    Função recursiva simples que imprime um mini 'fogos' em recursão.
    Serve apenas como demonstração de recursão extra para o exercício.
    """
    if rodadas <= 0:
        return
    console.print("[bold green]✨🎉 FESTA! 🎉✨[/]")
    animacao_festa(rodadas - 1)
# ================================
# VISUAIS CYBERPUNK EXTRAS
# ================================

def imprime_titulo() -> None:
    Console.clear()
    Console.print("\n")
    Console.print("[bold magenta]"
                  "██╗     ██╗ █████╗ ██████╗ ██╗██████╗ ██╗   ██╗\n"
                  "██║     ██║██╔══██╗██╔══██╗██║██╔══██╗╚██╗ ██╔╝\n"
                  "██║     ██║███████║██████╔╝██║██████╔╝ ╚████╔╝ \n"
                  "██║     ██║██╔══██║██╔══██╗██║██╔══██╗  ╚██╔╝  \n"
                  "███████╗██║██║  ██║██║  ██║██║██║  ██║   ██║   \n"
                  "╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝   ╚═╝   "
                  "[/bold magenta]")
    Console.print("\n[cyan]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]\n")
    Console.print("[bold cyan]Bem-vinda à Aventura Cyberpunk no Labirinto![/]\n")
    Console.print("[cyan]Use as setas ou WASD para jogar.[/]\n")
    Console.print("[cyan]Colete itens, marque pontos e fuja antes que acabem suas jogadas![/]\n")
    Console.print("[magenta]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]\n")
    Console.print("\n")


def status_jogador(jogador, jogadas_restantes: int) -> None:
    Console.print("[bold blue]╔════════════ STATUS DO JOGADOR ════════════╗[/]")
    Console.print(f"[bold blue]║  Pontos:            [/][yellow]{jogador.pontos:<10}[/][bold blue]        ║[/]")
    Console.print(f"[bold blue]║  Itens coletados:   [/][yellow]{jogador.itens_coletados:<10}[/][bold blue]  ║[/]")
    Console.print(f"[bold blue]║  Jogadas restantes: [/][yellow]{jogadas_restantes:<10}[/][bold blue]     ║[/]")
    Console.print("[bold blue]╚════════════════════════════════════════════╝[/]\n")


def game_over_visual() -> None:
    Console.clear()
    Console.print("\n")
    Console.print("[bold red]💀 GAME OVER 💀[/]")
    Console.print("[magenta]Você ficou sem jogadas![/]\n")
    Console.print("[red]███████████████████████████████████████████[/]")
    Console.print("[magenta]Obrigado por jogar a versão cyberpunk![/]")
    Console.print("[red]███████████████████████████████████████████[/]\n")
    Console.print("\n")
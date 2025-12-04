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
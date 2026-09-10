"""Funções para leitura e validação das entradas do usuário."""


def ler_numero_positivo(mensagem):
    """Lê um número decimal maior que zero."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def ler_inteiro_positivo(mensagem):
    """Lê um número inteiro maior que zero."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Digite um número inteiro maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

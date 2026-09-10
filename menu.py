"""Menu principal do sistema FarmTech Solutions."""

from csv_utils import exportar_csv
from registros import atualizar_dados, cadastrar_dados, excluir_dados, visualizar_dados


def executar_menu():
    """Executa o menu até que o usuário escolha sair."""
    while True:
        print("\n===== FARMTECH SOLUTIONS =====")
        print("1 - Cadastrar dados")
        print("2 - Visualizar dados")
        print("3 - Atualizar dados")
        print("4 - Excluir dados")
        print("5 - Exportar dados para CSV")
        print("6 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 6.")
            continue

        if opcao == 1:
            cadastrar_dados()
        elif opcao == 2:
            visualizar_dados()
        elif opcao == 3:
            atualizar_dados()
        elif opcao == 4:
            excluir_dados()
        elif opcao == 5:
            exportar_csv()
        elif opcao == 6:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 6.")

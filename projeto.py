"""
FARMTECH SOLUTIONS

Sistema para trabalhar com duas culturas agrícolas:
- Soja
- Café

O sistema realiza:
- Cálculo da área de plantio
- Cálculo da quantidade de insumos
- Cadastro dos dados em uma lista
- Visualização
- Atualização
- Exclusão
"""

dados = []


def cadastrar_dados():
    nome = input("Insira o nome da fazenda: ")
    cultura = input("Digite a cultura (soja/café): ").lower()

    if cultura == "soja":
        print("\n--- Cálculo da área da soja ---")

        comprimento = float(input("Digite o comprimento do terreno em metros: "))
        largura = float(input("Digite a largura do terreno em metros: "))

        area_m2 = comprimento * largura
        area_hectares = area_m2 / 10000

        fertilizante_por_hectare = float(
            input("Quantidade de fertilizante utilizada por hectare (kg): ")
        )

        insumo_total = area_hectares * fertilizante_por_hectare
        unidade = "kg de fertilizante"
        print(f"\nÁrea de plantio: {area_m2:.2f} m²")
        print(f"Quantidade de fertilizante necessária: {insumo_total:.2f} {unidade}")
        

    elif cultura == "café":
        print("\n--- Cálculo da área do café ---")

        import math

        raio = float(input("Digite o raio da área de plantio em metros: "))
        area_m2 = math.pi * raio ** 2
        area_hectares = area_m2 / 10000
        numero_ruas = int(input("Digite o número de ruas da lavoura: "))
        comprimento_rua = float(
            input("Digite o comprimento de cada rua em metros: ")
        )
        ml_por_metro = float(
            input("Digite a quantidade aplicada em mL por metro: ") 
        )
        total_ml = numero_ruas * comprimento_rua * ml_por_metro
        insumo_total = total_ml / 1000
        unidade = "litros de produto"
        print(f"\nÁrea de plantio: {area_m2:.2f} m²")
        print(f"Quantidade de produto necessária: {insumo_total:.2f} {unidade}")


    else:
        print("Cultura inválida. Escolha soja ou café.")
        return

    registro = {
        "nome": nome,
        "cultura": cultura,
        "area_m2": area_m2,
        "area_hectares": area_hectares,
        "insumo_total": insumo_total,
        "unidade": unidade
    }

    dados.append(registro)

    print("\nCadastro realizado com sucesso.")


def visualizar_dados():
    if not dados:
        print("\nNenhum dado cadastrado.")
        return

    print("\n===== DADOS CADASTRADOS =====")

    for i, dado in enumerate(dados):
        print(f"\nRegistro {i + 1}")
        print(f"Fazenda: {dado['nome']}")
        print(f"Cultura: {dado['cultura']}")
        print(f"Área: {dado['area_m2']:.2f} m²")
        print(f"Área: {dado['area_hectares']:.2f} hectares")
        print(
            f"Insumo necessário: "
            f"{dado['insumo_total']:.2f} {dado['unidade']}"
        )


def atualizar_dados():
    if not dados:
        print("\nNenhum dado cadastrado.")
        return

    visualizar_dados()

    indice = int(
        input("\nDigite o número do registro que deseja atualizar: ")
    ) - 1

    if 0 <= indice < len(dados):
        nome = input("Digite o novo nome da fazenda: ")
        cultura = input("Digite a nova cultura (soja/café): ").lower()

        if cultura == "soja":
            comprimento = float(input("Comprimento do terreno em metros: "))
            largura = float(input("Largura do terreno em metros: "))

            area_m2 = comprimento * largura
            area_hectares = area_m2 / 10000

            fertilizante_por_hectare = float(
                input("Quantidade de fertilizante por hectare (kg): ")
            )

            insumo_total = area_hectares * fertilizante_por_hectare
            unidade = "kg de fertilizante"

        elif cultura == "café":
            comprimento = float(input("Comprimento do terreno em metros: "))
            largura = float(input("Largura do terreno em metros: "))

            area_m2 = comprimento * largura
            area_hectares = area_m2 / 10000

            numero_ruas = int(input("Número de ruas da lavoura: "))
            comprimento_rua = float(
                input("Comprimento de cada rua em metros: ")
            )
            ml_por_metro = float(
                input("Quantidade aplicada em mL por metro: ")
            )

            total_ml = numero_ruas * comprimento_rua * ml_por_metro
            insumo_total = total_ml / 1000
            unidade = "litros de produto"

        else:
            print("Cultura inválida.")
            return

        dados[indice] = {
            "nome": nome,
            "cultura": cultura,
            "area_m2": area_m2,
            "area_hectares": area_hectares,
            "insumo_total": insumo_total,
            "unidade": unidade
        }

        print("\nDado atualizado com sucesso.")

    else:
        print("Índice inválido.")


def excluir_dados():
    if not dados:
        print("\nNenhum dado cadastrado.")
        return

    visualizar_dados()

    indice = int(
        input("\nDigite o número do registro que deseja excluir: ")
    ) - 1

    if 0 <= indice < len(dados):
        del dados[indice]
        print("Dado excluído com sucesso.")
    else:
        print("Índice inválido.")


while True:
    print("\n===== FARMTECH SOLUTIONS =====")
    print("1 - Cadastrar dados")
    print("2 - Visualizar dados")
    print("3 - Atualizar dados")
    print("4 - Excluir dados")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_dados()

    elif opcao == 2:
        visualizar_dados()

    elif opcao == 3:
        atualizar_dados()

    elif opcao == 4:
        excluir_dados()

    elif opcao == 5:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")

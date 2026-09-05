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

import math

# Lista que armazena os registros cadastrados durante a execução do programa.
dados = []


def ler_numero_positivo(mensagem):
    """Lê um número decimal e garante que ele seja maior que zero."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")


def ler_inteiro_positivo(mensagem):
    """Lê um número inteiro e garante que ele seja maior que zero."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("Digite um número inteiro maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def calcular_cultura(cultura):
    """Solicita os dados da cultura e retorna os cálculos realizados."""
    if cultura == "soja":
        print("\n--- Cálculo da área da soja ---")

        # Para a soja, o terreno é considerado retangular.
        comprimento = ler_numero_positivo(
            "Digite o comprimento do terreno em metros: "
        )
        largura = ler_numero_positivo(
            "Digite a largura do terreno em metros: "
        )

        area_m2 = comprimento * largura
        area_hectares = area_m2 / 10000

        fertilizante_por_hectare = ler_numero_positivo(
            "Quantidade de fertilizante utilizada por hectare (kg): "
        )
        insumo_total = area_hectares * fertilizante_por_hectare

        return {
            "area_m2": area_m2,
            "area_hectares": area_hectares,
            "insumo_total": insumo_total,
            "unidade": "kg de fertilizante",
            "comprimento": comprimento,
            "largura": largura,
            "fertilizante_por_hectare": fertilizante_por_hectare,
        }

    if cultura in ("café", "cafe"):
        print("\n--- Cálculo da área do café ---")

        # Para o café, a área de plantio é considerada circular.
        raio = ler_numero_positivo(
            "Digite o raio da área de plantio em metros: "
        )
        area_m2 = math.pi * raio ** 2
        area_hectares = area_m2 / 10000

        # O produto é calculado pela quantidade aplicada em cada metro das ruas.
        numero_ruas = ler_inteiro_positivo(
            "Digite o número de ruas da lavoura: "
        )
        comprimento_rua = ler_numero_positivo(
            "Digite o comprimento de cada rua em metros: "
        )
        ml_por_metro = ler_numero_positivo(
            "Digite a quantidade aplicada em mL por metro: "
        )

        total_ml = numero_ruas * comprimento_rua * ml_por_metro
        insumo_total = total_ml / 1000

        return {
            "area_m2": area_m2,
            "area_hectares": area_hectares,
            "insumo_total": insumo_total,
            "unidade": "litros de produto",
            "raio": raio,
            "numero_ruas": numero_ruas,
            "comprimento_rua": comprimento_rua,
            "ml_por_metro": ml_por_metro,
        }

    print("Cultura inválida. Escolha soja ou café.")
    return None


def cadastrar_dados():
    """Cadastra uma fazenda e os dados de uma das duas culturas."""
    nome = input("Insira o nome da fazenda: ").strip()
    cultura = input("Digite a cultura (soja/café): ").strip().lower()

    calculos = calcular_cultura(cultura)
    if calculos is None:
        return

    # Junta os dados de identificação aos valores calculados.
    registro = {
        "nome": nome,
        "cultura": cultura,
    }
    registro.update(calculos)
    dados.append(registro)

    print(f"\nÁrea de plantio: {registro['area_m2']:.2f} m²")
    print(f"Área de plantio: {registro['area_hectares']:.4f} hectares")
    print(
        f"Insumo necessário: {registro['insumo_total']:.2f} "
        f"{registro['unidade']}"
    )
    print("\nCadastro realizado com sucesso.")


def visualizar_dados():
    """Exibe todos os registros armazenados na lista."""
    if not dados:
        print("\nNenhum dado cadastrado.")
        return

    print("\n===== DADOS CADASTRADOS =====")

    for i, dado in enumerate(dados):
        print(f"\nRegistro {i + 1}")
        print(f"Fazenda: {dado['nome']}")
        print(f"Cultura: {dado['cultura']}")
        print(f"Área: {dado['area_m2']:.2f} m²")
        print(f"Área: {dado['area_hectares']:.4f} hectares")
        print(
            f"Insumo necessário: "
            f"{dado['insumo_total']:.2f} {dado['unidade']}"
        )

        # Mostra também os valores que deram origem aos cálculos.
        if dado["cultura"] == "soja":
            print(f"Comprimento: {dado['comprimento']:.2f} m")
            print(f"Largura: {dado['largura']:.2f} m")
            print(
                "Fertilizante por hectare: "
                f"{dado['fertilizante_por_hectare']:.2f} kg/ha"
            )
        else:
            print(f"Raio: {dado['raio']:.2f} m")
            print(f"Número de ruas: {dado['numero_ruas']}")
            print(f"Comprimento de cada rua: {dado['comprimento_rua']:.2f} m")
            print(f"Aplicação: {dado['ml_por_metro']:.2f} mL/m")


def atualizar_dados():
    """Substitui um registro escolhido pelo usuário por novos dados."""
    if not dados:
        print("\nNenhum dado cadastrado.")
        return

    visualizar_dados()

    indice = ler_inteiro_positivo(
        "\nDigite o número do registro que deseja atualizar: "
    ) - 1

    if not 0 <= indice < len(dados):
        print("Índice inválido.")
        return

    nome = input("Digite o novo nome da fazenda: ").strip()
    cultura = input("Digite a nova cultura (soja/café): ").strip().lower()

    # Usa a mesma função do cadastro para evitar cálculos diferentes
    # entre cadastrar e atualizar um registro.
    calculos = calcular_cultura(cultura)
    if calculos is None:
        return

    registro = {
        "nome": nome,
        "cultura": cultura,
    }
    registro.update(calculos)
    dados[indice] = registro

    print("\nDado atualizado com sucesso.")


def excluir_dados():
    """Exclui da lista o registro escolhido pelo usuário."""
    if not dados:
        print("\nNenhum dado cadastrado.")
        return

    visualizar_dados()

    indice = ler_inteiro_positivo(
        "\nDigite o número do registro que deseja excluir: "
    ) - 1

    if 0 <= indice < len(dados):
        del dados[indice]
        print("Dado excluído com sucesso.")
    else:
        print("Índice inválido.")


def executar_menu():
    """Mantém o menu principal em execução até o usuário escolher sair."""
    while True:
        print("\n===== FARMTECH SOLUTIONS =====")
        print("1 - Cadastrar dados")
        print("2 - Visualizar dados")
        print("3 - Atualizar dados")
        print("4 - Excluir dados")
        print("5 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 5.")
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
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


executar_menu()

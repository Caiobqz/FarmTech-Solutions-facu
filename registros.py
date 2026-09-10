"""Operações de cadastro, visualização, atualização e exclusão."""

from culturas import calcular_cultura
from dados import dados
from validacoes import ler_inteiro_positivo


def criar_registro(nome, cultura):
    """Monta um registro usando os cálculos da cultura escolhida."""
    calculos = calcular_cultura(cultura)
    if calculos is None:
        return None

    registro = {"nome": nome, "cultura": cultura}
    registro.update(calculos)
    return registro


def cadastrar_dados():
    """Cadastra uma fazenda e sua cultura."""
    nome = input("Insira o nome da fazenda: ").strip()
    cultura = input("Digite a cultura (soja/café): ").strip().lower()

    registro = criar_registro(nome, cultura)
    if registro is None:
        return

    dados.append(registro)
    print(f"\nÁrea de plantio: {registro['area_m2']:.2f} m²")
    print(f"Área de plantio: {registro['area_hectares']:.4f} hectares")
    print(f"Produto utilizado: {registro['produto']}")
    print(f"Insumo necessário: {registro['insumo_total']:.2f} {registro['unidade']}")
    print("\nCadastro realizado com sucesso.")


def visualizar_dados():
    """Exibe todos os registros armazenados."""
    if not dados:
        print("\nNenhum dado cadastrado.")
        return

    print("\n===== DADOS CADASTRADOS =====")
    for i, dado in enumerate(dados, start=1):
        print(f"\nRegistro {i}")
        print(f"Fazenda: {dado['nome']}")
        print(f"Cultura: {dado['cultura']}")
        print(f"Área: {dado['area_m2']:.2f} m²")
        print(f"Área: {dado['area_hectares']:.4f} hectares")
        print(f"Produto utilizado: {dado['produto']}")
        print(f"Insumo necessário: {dado['insumo_total']:.2f} {dado['unidade']}")

        if dado["cultura"] == "soja":
            print(f"Comprimento: {dado['comprimento']:.2f} m")
            print(f"Largura: {dado['largura']:.2f} m")
            print(f"Fertilizante por hectare: {dado['fertilizante_por_hectare']:.2f} kg/ha")
        else:
            print(f"Raio: {dado['raio']:.2f} m")
            print(f"Número de ruas: {dado['numero_ruas']}")
            print(f"Comprimento de cada rua: {dado['comprimento_rua']:.2f} m")
            print(f"Aplicação: {dado['ml_por_metro']:.2f} mL/m")


def atualizar_dados():
    """Substitui um registro escolhido pelo usuário."""
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
    registro = criar_registro(nome, cultura)

    if registro is not None:
        dados[indice] = registro
        print("\nDado atualizado com sucesso.")


def excluir_dados():
    """Exclui um registro escolhido pelo usuário."""
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

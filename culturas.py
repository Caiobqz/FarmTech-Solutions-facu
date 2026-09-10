"""Cálculos de área e insumos das culturas atendidas pelo sistema."""

import math

from validacoes import ler_inteiro_positivo, ler_numero_positivo


def calcular_soja():
    """Calcula área retangular e fertilizante necessário para soja."""
    print("\n--- Cálculo da área da soja ---")
    comprimento = ler_numero_positivo("Digite o comprimento do terreno em metros: ")
    largura = ler_numero_positivo("Digite a largura do terreno em metros: ")

    area_m2 = comprimento * largura
    area_hectares = area_m2 / 10000
    fertilizante_por_hectare = ler_numero_positivo(
        "Quantidade de fertilizante utilizada por hectare (kg): "
    )

    return {
        "area_m2": area_m2,
        "area_hectares": area_hectares,
        "insumo_total": area_hectares * fertilizante_por_hectare,
        "unidade": "kg de fertilizante",
        "comprimento": comprimento,
        "largura": largura,
        "fertilizante_por_hectare": fertilizante_por_hectare,
    }


def calcular_cafe():
    """Calcula área circular e produto necessário para café."""
    print("\n--- Cálculo da área do café ---")
    raio = ler_numero_positivo("Digite o raio da área de plantio em metros: ")
    area_m2 = math.pi * raio ** 2
    area_hectares = area_m2 / 10000

    numero_ruas = ler_inteiro_positivo("Digite o número de ruas da lavoura: ")
    comprimento_rua = ler_numero_positivo(
        "Digite o comprimento de cada rua em metros: "
    )
    ml_por_metro = ler_numero_positivo(
        "Digite a quantidade aplicada em mL por metro: "
    )

    total_ml = numero_ruas * comprimento_rua * ml_por_metro

    return {
        "area_m2": area_m2,
        "area_hectares": area_hectares,
        "insumo_total": total_ml / 1000,
        "unidade": "litros de produto",
        "raio": raio,
        "numero_ruas": numero_ruas,
        "comprimento_rua": comprimento_rua,
        "ml_por_metro": ml_por_metro,
    }


def calcular_cultura(cultura):
    """Seleciona o cálculo correspondente à cultura informada."""
    if cultura == "soja":
        return calcular_soja()
    if cultura in ("café", "cafe"):
        return calcular_cafe()

    print("Cultura inválida. Escolha soja ou café.")
    return None

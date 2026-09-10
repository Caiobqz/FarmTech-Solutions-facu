"""Exportação dos registros do sistema para CSV."""

import csv

from dados import dados


CAMPOS_COMUNS = [
    "nome",
    "cultura",
    "area_m2",
    "area_hectares",
    "insumo_total",
    "unidade",
]


def exportar_csv():
    """Exporta todos os registros para dados_fazendas.csv."""
    if not dados:
        print("\nNenhum dado disponível para exportar.")
        return

    campos = CAMPOS_COMUNS.copy()
    for dado in dados:
        for chave in dado:
            if chave not in campos:
                campos.append(chave)

    with open("dados_fazendas.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

    print("\nDados exportados para dados_fazendas.csv com sucesso.")

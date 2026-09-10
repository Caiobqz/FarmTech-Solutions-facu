# FARMTECH SOLUTIONS - ANALISE ESTATISTICA EM R
#
# Este programa le o arquivo CSV gerado pelo projeto em Python
# e calcula estatisticas basicas das areas cadastradas.

arquivo_csv <- "dados_fazendas.csv"

# Verifica se o CSV existe antes de tentar le-lo.
if (!file.exists(arquivo_csv)) {
  stop(
    "Arquivo dados_fazendas.csv nao encontrado. ",
    "Execute o projeto Python, cadastre os dados e use a opcao de exportar CSV."
  )
}

# Le os dados exportados pelo Python.
dados <- read.csv(
  arquivo_csv,
  stringsAsFactors = FALSE,
  fileEncoding = "UTF-8"
)

# Mostra os dados recebidos para facilitar a conferencia.
cat("\n===== DADOS IMPORTADOS =====\n")
print(dados)

# Media e desvio padrao da area em hectares.
media_area <- mean(dados$area_hectares, na.rm = TRUE)
desvio_area <- sd(dados$area_hectares, na.rm = TRUE)

cat("\n===== ESTATISTICAS DAS AREAS =====\n")
cat("Media da area em hectares:", round(media_area, 4), "ha\n")

if (is.na(desvio_area)) {
  cat("Desvio padrao: sao necessarios pelo menos dois registros.\n")
} else {
  cat("Desvio padrao da area:", round(desvio_area, 4), "ha\n")
}

# Os insumos nao sao misturados em uma unica media porque soja usa kg
# e cafe usa litros. As estatisticas sao calculadas separadamente.
soja <- dados[dados$cultura == "soja", ]
cafe <- dados[dados$cultura %in% c("cafe", "café"), ]

cat("\n===== ESTATISTICAS POR CULTURA =====\n")

if (nrow(soja) > 0) {
  cat("\nSoja:\n")
  cat("Media do fertilizante:", round(mean(soja$insumo_total, na.rm = TRUE), 2), "kg\n")

  if (nrow(soja) >= 2) {
    cat("Desvio padrao do fertilizante:", round(sd(soja$insumo_total, na.rm = TRUE), 2), "kg\n")
  } else {
    cat("Desvio padrao do fertilizante: sao necessarios pelo menos dois registros de soja.\n")
  }
}

if (nrow(cafe) > 0) {
  cat("\nCafe:\n")
  cat("Media do produto:", round(mean(cafe$insumo_total, na.rm = TRUE), 2), "litros\n")

  if (nrow(cafe) >= 2) {
    cat("Desvio padrao do produto:", round(sd(cafe$insumo_total, na.rm = TRUE), 2), "litros\n")
  } else {
    cat("Desvio padrao do produto: sao necessarios pelo menos dois registros de cafe.\n")
  }
}

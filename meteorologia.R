# FARMTECH SOLUTIONS - CONSULTA METEOROLOGICA EM R
#
# Consulta a API publica Open-Meteo e exibe dados climaticos atuais
# no terminal. A consulta usa coordenadas de Betim, Minas Gerais.

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  cat("Pacote jsonlite nao encontrado. Instalando...\n")
  install.packages("jsonlite", repos = "https://cloud.r-project.org")
}

library(jsonlite)

latitude <- -19.9678
longitude <- -44.1983

url_api <- paste0(
  "https://api.open-meteo.com/v1/forecast?latitude=", latitude,
  "&longitude=", longitude,
  "&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
  "&timezone=America%2FSao_Paulo"
)

cat("\n===== CONSULTA METEOROLOGICA =====\n")
cat("Local de referencia: Betim - MG\n")

resultado <- tryCatch(
  fromJSON(url_api),
  error = function(erro) {
    cat("Nao foi possivel consultar a API meteorologica.\n")
    cat("Verifique sua conexao com a internet e tente novamente.\n")
    NULL
  }
)

if (!is.null(resultado)) {
  atual <- resultado$current

  cat("Data e hora:", atual$time, "\n")
  cat("Temperatura:", atual$temperature_2m, "°C\n")
  cat("Umidade relativa:", atual$relative_humidity_2m, "%\n")
  cat("Precipitacao:", atual$precipitation, "mm\n")
  cat("Velocidade do vento:", atual$wind_speed_10m, "km/h\n")

  if (atual$precipitation > 0) {
    cat("Situacao: ha precipitacao registrada no momento.\n")
  } else {
    cat("Situacao: sem precipitacao registrada no momento.\n")
  }
}

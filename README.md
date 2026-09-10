# FarmTech Solutions

Projeto acadêmico desenvolvido para a atividade da FIAP, aplicando programação e análise de dados a um cenário de Agricultura Digital.

## Culturas atendidas

- Soja
- Café

## Aplicação em Python

A aplicação permite cadastrar, visualizar, atualizar e excluir registros armazenados em uma lista (vetor), além de exportar os dados para CSV.

### Cálculos

**Soja**
- Área retangular: comprimento × largura;
- Conversão de m² para hectares;
- Escolha do fertilizante utilizado;
- Cálculo da quantidade necessária em kg a partir da dose por hectare.

**Café**
- Área circular: π × raio²;
- Conversão de m² para hectares;
- Escolha do produto utilizado no manejo;
- Cálculo do produto necessário considerando número de ruas, comprimento de cada rua e aplicação em mL por metro;
- Conversão do resultado para litros.

O sistema utiliza estruturas de repetição, decisão e validação de entradas.

## Integração Python e R

Os registros podem ser exportados pelo menu do Python para `dados_fazendas.csv`. Esse arquivo é utilizado por `estatisticas.R` para calcular e exibir:

- média das áreas em hectares;
- desvio padrão das áreas;
- média e desvio padrão do insumo da soja;
- média e desvio padrão do insumo do café.

Os insumos das duas culturas são analisados separadamente porque possuem unidades diferentes.

## API meteorológica em R

O arquivo `meteorologia.R` consulta a API pública Open-Meteo utilizando R e exibe no terminal dados meteorológicos atuais para uma localização de referência em Betim, Minas Gerais:

- temperatura;
- umidade relativa;
- precipitação;
- velocidade do vento;
- indicação textual sobre ocorrência de precipitação.

A consulta utiliza o pacote R `jsonlite`. Caso ele não esteja instalado, o próprio script realiza a instalação pelo CRAN.

## Estrutura do projeto

```text
FarmTech-Solutions-facu/
├── projeto.py          # ponto de entrada
├── menu.py             # menu principal
├── culturas.py         # cálculos de área e manejo de insumos
├── registros.py        # cadastro, consulta, atualização e exclusão
├── validacoes.py       # validação das entradas
├── dados.py            # vetor/lista compartilhado
├── csv_utils.py        # exportação para CSV
├── estatisticas.R      # análise estatística
├── meteorologia.R      # consulta à API meteorológica
├── .gitignore
└── README.md
```

## Como executar

### Python

No terminal, dentro da pasta do projeto:

```bash
python projeto.py
```

Cadastre os registros e utilize a opção **Exportar dados para CSV** antes de executar a análise estatística.

### Estatísticas em R

```bash
Rscript estatisticas.R
```

### Meteorologia em R

```bash
Rscript meteorologia.R
```

> No Windows, caso `Rscript` não esteja configurado no PATH, execute o `Rscript.exe` pelo caminho da instalação do R.

## Tecnologias

- Python
- R
- Git
- GitHub
- CSV
- Open-Meteo API

## Entrega acadêmica

Além dos códigos, a entrega final da atividade deverá incluir o resumo solicitado na disciplina de Formação Social e um arquivo TXT contendo o link do vídeo de demonstração publicado no YouTube como não listado.

## Status

Python, exportação CSV e análise estatística em R implementados. Consulta meteorológica em R adicionada e pendente de validação no ambiente final antes da entrega.

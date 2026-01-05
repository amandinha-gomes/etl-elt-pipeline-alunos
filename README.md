# 📊 Pipeline de Dados — ETL & ELT com Python e SQL

## 🔍 Visão Geral
Este projeto demonstra a construção de um pipeline de dados completo, aplicando conceitos de **ETL (Extract, Transform, Load)** e **ELT (Extract, Load, Transform)** utilizando Python, SQL e SQLite.<br>
O objetivo é simular um cenário real de engenharia e análise de dados, desde a ingestão de dados brutos até a geração de análises e visualizações consolidadas em um mini dashboard.

## 🧱 Estrutura do Projeto
- data/
  - alunos.csv
- etl.py
- elt.py
- queries_analiticas.py
- validacao_dados.py
- graficos.py
- dashboard.py
- database.db
- dashboard_alunos_pronto.png

## ⚙️ Tecnologias Utilizadas

- Python
- Pandas
- SQLite
- SQL (queries analíticas)
- Matplotlib
- VS Code

## 🔄 Pipeline de Dados
🔹 ETL
- Extração de dados a partir de arquivo CSV
- Tratamento e padronização dos dados
- Carga em tabela intermediária

🔹 ELT
- Carga dos dados brutos no banco
- Transformações aplicadas diretamente via SQL
- Criação de tabela analítica final (alunos_elt)

## 📈 Análises Realizadas (SQL)
As análises incluem:

- Quantidade de alunos por curso

- Renda média por curso

- Distribuição por faixa etária
  
- Distribuição de alunos por sexo

- Renda média por sexo

- Idade média por sexo

Todas as consultas são realizadas via SQL e integradas ao Python.

### 📊 Dashboard Analítico

O projeto gera um dashboard consolidado com os principais indicadores:

- 📌 Quantidade de alunos por curso

- 💰 Renda média por curso

- 👥 Distribuição por faixa etária

- ⚧️ Distribuição por sexo

O dashboard é salvo automaticamente como imagem `(dashboard_alunos_pronto.png).`

## ✅ Validação de Dados
O projeto conta com um script de validação que verifica:

- Valores nulos
- Idades fora do intervalo esperado
- Rendas inválidas
- Consistência geral dos dados

## 🎯 Objetivo do Projeto

Demonstrar domínio prático em:

- ETL e ELT

- SQL analítico

- Validação de dados

- Visualização e storytelling com dados

- Organização de projetos de dados


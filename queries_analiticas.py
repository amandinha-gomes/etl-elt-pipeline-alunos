import sqlite3
import pandas as pd

conexao = sqlite3.connect("database.db")

# 1. Alunos por curso
query1 = """
SELECT curso, COUNT(*) AS total_alunos
FROM alunos_elt
GROUP BY curso
ORDER BY total_alunos DESC;
"""
df1 = pd.read_sql_query(query1, conexao)
print("\nAlunos por curso:")
print(df1)

print("-" * 40)

# 2. Renda média por curso
query2 = """
SELECT curso, ROUND(AVG(renda), 2) AS renda_media
FROM alunos_elt
GROUP BY curso
ORDER BY renda_media DESC;
"""
df2 = pd.read_sql_query(query2, conexao)
print("\nRenda média por curso:")
print(df2)

print("-" * 40)

# 3. Distribuição por faixa etária
query3 = """
SELECT faixa_etaria, COUNT(*) AS total
FROM alunos_elt
GROUP BY faixa_etaria;
"""
df3 = pd.read_sql_query(query3, conexao)
print("\nDistribuição por faixa etária:")
print(df3)

print("-" * 40)

# 4. Idade média dos alunos
query4 = """
SELECT
    ROUND(AVG(idade), 1) AS idade_media
FROM alunos_elt;
"""
df4 = pd.read_sql_query(query4, conexao)
print("\nIdade média dos alunos:")
print(df4)

print("-" * 40)

# 5. Distribuição de alunos por sexo
query5 = """
SELECT
    CASE
        WHEN sexo = 'F' THEN 'Feminino'
        WHEN sexo = 'M' THEN 'Masculino'
    END AS sexo,
    COUNT(*) AS total
FROM alunos_elt
GROUP BY sexo;
"""
df5 = pd.read_sql_query(query5, conexao)
print("\nDistribuição de alunos por sexo:")
print(df5)

print("-" * 40)

# 6. Renda média por sexo
query6 = """
SELECT
    CASE
        WHEN sexo = 'F' THEN 'Feminino'
        WHEN sexo = 'M' THEN 'Masculino'
    END AS sexo,
    ROUND(AVG(renda), 2) AS renda_media
FROM alunos_elt
GROUP BY sexo;
"""
df6 = pd.read_sql_query(query6, conexao)
print("\nRenda média por sexo:")
print(df6)

print("-" * 40)

# 7. Idade média por sexo
query7 = """
SELECT
    CASE
        WHEN sexo = 'F' THEN 'Feminino'
        WHEN sexo = 'M' THEN 'Masculino'
    END AS sexo,
    ROUND(AVG(idade), 1) AS idade_media
FROM alunos_elt
GROUP BY sexo;
"""
df7 = pd.read_sql_query(query7, conexao)
print("\nIdade média por sexo:")
print(df7)

conexao.close()

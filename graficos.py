import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conexao = sqlite3.connect("database.db")

# QUERIES

# 1. Alunos por curso
df1 = pd.read_sql_query("""
SELECT curso, COUNT(*) AS total
FROM alunos_elt
GROUP BY curso
ORDER BY total DESC;
""", conexao)

# 2. Renda média por curso
df2 = pd.read_sql_query("""
SELECT curso, ROUND(AVG(renda), 2) AS renda_media
FROM alunos_elt
GROUP BY curso
ORDER BY renda_media DESC;
""", conexao)

# 3. Faixa etária
df3 = pd.read_sql_query("""
SELECT faixa_etaria, COUNT(*) AS total
FROM alunos_elt
GROUP BY faixa_etaria;
""", conexao)

# 4. Idade média geral
df4 = pd.read_sql_query("""
SELECT ROUND(AVG(idade), 1) AS idade_media
FROM alunos_elt;
""", conexao)

# 5. Quantidade por sexo
df5 = pd.read_sql_query("""
SELECT
    CASE
        WHEN sexo = 'F' THEN 'Feminino'
        WHEN sexo = 'M' THEN 'Masculino'
    END AS sexo,
    COUNT(*) AS total
FROM alunos_elt
GROUP BY sexo;
""", conexao)

# 6. Renda média por sexo
df6 = pd.read_sql_query("""
SELECT
    CASE
        WHEN sexo = 'F' THEN 'Feminino'
        WHEN sexo = 'M' THEN 'Masculino'
    END AS sexo,
    ROUND(AVG(renda), 2) AS renda_media
FROM alunos_elt
GROUP BY sexo;
""", conexao)

# 7. Idade média por sexo
df7 = pd.read_sql_query("""
SELECT
    CASE
        WHEN sexo = 'F' THEN 'Feminino'
        WHEN sexo = 'M' THEN 'Masculino'
    END AS sexo,
    ROUND(AVG(idade), 1) AS idade_media
FROM alunos_elt
GROUP BY sexo;
""", conexao)

conexao.close()


# DASHBOARD
fig, axs = plt.subplots(4, 2, figsize=(17, 18))
fig.suptitle("Dashboard Analítico de Alunos (ETL & ELT)", fontsize=20)

# Alunos por curso
axs[0, 0].barh(df1["curso"], df1["total"])
axs[0, 0].set_title("Quantidade de Alunos por Curso")
axs[0, 0].invert_yaxis()

# Renda média por curso
axs[0, 1].barh(df2["curso"], df2["renda_media"])
axs[0, 1].set_title("Renda Média por Curso")
axs[0, 1].invert_yaxis()

# Distribuição por faixa etária
axs[1, 0].bar(df3["faixa_etaria"], df3["total"])
axs[1, 0].set_title("Distribuição por Faixa Etária")

# Indicador: idade média geral
axs[1, 1].axis("off")
axs[1, 1].text(
    0.5,
    0.5,
    f"Idade Média Geral\n{df4['idade_media'][0]} anos",
    fontsize=22,
    ha="center",
    va="center",
    bbox=dict(boxstyle="round", pad=0.6)
)

# Quantidade por sexo
axs[2, 0].bar(df5["sexo"], df5["total"])
axs[2, 0].set_title("Distribuição de Alunos por Sexo")

# Renda média por sexo
axs[2, 1].bar(df6["sexo"], df6["renda_media"])
axs[2, 1].set_title("Renda Média por Sexo")

# Idade média por sexo
axs[3, 0].bar(df7["sexo"], df7["idade_media"])
axs[3, 0].set_title("Idade Média por Sexo")

# Espaço vazio (layout limpo)
axs[3, 1].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("dashboard_alunos.png")
plt.show()

print("Dashboard atualizado e salvo como 'dashboard_alunos.png'")

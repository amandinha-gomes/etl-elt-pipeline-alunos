import pandas as pd
import sqlite3

# EXTRACT
df = pd.read_csv("data/alunos.csv")

print("Linhas no CSV:", len(df))

# LOAD
conexao = sqlite3.connect("database.db")
df.to_sql("alunos_raw", conexao, if_exists="replace", index=False)

conexao.commit()
conexao.close()

print("ETL executado com sucesso!")

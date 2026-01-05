import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("SELECT COUNT(*) FROM alunos_raw")
print("Registros em alunos_raw:", cursor.fetchone()[0])

cursor.execute("DROP TABLE IF EXISTS alunos_elt")

cursor.execute("""
CREATE TABLE alunos_elt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    curso TEXT,
    idade INTEGER,
    renda REAL,
    sexo TEXT,
    faixa_etaria TEXT
)
""")

cursor.execute("""
INSERT INTO alunos_elt (nome, curso, idade, renda, sexo, faixa_etaria)
SELECT
    nome,
    UPPER(curso),
    idade,
    renda,
    sexo,
    CASE
        WHEN idade < 21 THEN 'Jovem'
        ELSE 'Adulto'
    END
FROM alunos_raw
""")

# DEBUG FINAL
cursor.execute("SELECT COUNT(*) FROM alunos_elt")
print("Registros em alunos_elt:", cursor.fetchone()[0])

conexao.commit()
conexao.close()

print("ELT executado com sucesso!")

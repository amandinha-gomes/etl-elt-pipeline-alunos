import pandas as pd

print("=== Validação de Qualidade dos Dados ===")

# Leitura do CSV
df = pd.read_csv("data/alunos.csv")

# 1. Verificar valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# 2. Verificar idades inválidas
idades_invalidas = df[(df["idade"] < 0) | (df["idade"] > 100)]
print(f"\nRegistros com idade inválida: {len(idades_invalidas)}")

# 3. Verificar rendas negativas
rendas_invalidas = df[df["renda"] < 0]
print(f"Registros com renda negativa: {len(rendas_invalidas)}")

# 4. Cursos distintos (para checar padronização)
print("\nCursos encontrados:")
for curso in df["curso"].unique():
    print("-", curso)

# 5. Tipos de dados
print("\nTipos de dados:")
print(df.dtypes)

print("\nValidação concluída com sucesso.")

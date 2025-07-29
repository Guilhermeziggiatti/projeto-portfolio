import tabula
import pandas as pd

# lê todas as tabelas do PDF usando lattice (bom pra grades)
tables = tabula.read_pdf(
    "menu.pdf",
    pages="all",
    multiple_tables=True,
    lattice=True
)

if not tables:
    print("⚠️ Não encontrou nenhuma tabela com tabula-py.")
    exit(1)

# concatena tudo
df = pd.concat(tables, ignore_index=True)

# (opcional) ajuste nomes de colunas:
# df.columns = ["título","categoria","ingredientes","tempo_min"]

df.to_csv("receitas.csv", index=False)
print("✅ receitas.csv gerado com sucesso!")

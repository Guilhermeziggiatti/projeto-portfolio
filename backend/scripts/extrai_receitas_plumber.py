import pdfplumber
import pandas as pd

tabelas = []

with pdfplumber.open('menu.pdf') as pdf:
    for page in pdf.pages:
        tbl = page.extract_table()
        if tbl and len(tbl) > 1:
            # primeira linha é cabeçalho
            df_page = pd.DataFrame(tbl[1:], columns=tbl[0])
            tabelas.append(df_page)

if tabelas:
    df = pd.concat(tabelas, ignore_index=True)
    df.to_csv('receitas.csv', index=False)
    print("✅ receitas.csv gerado com sucesso!")
else:
    print("⚠️ Não encontrou nenhuma tabela no PDF.")

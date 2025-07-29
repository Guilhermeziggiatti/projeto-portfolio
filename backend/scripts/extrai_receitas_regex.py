import pdfplumber
import re
import pandas as pd

receitas = []

# abra o PDF
with pdfplumber.open("menu.pdf") as pdf:
    for page in pdf.pages:
        texto = page.extract_text()
        if not texto:
            continue
        for linha in texto.split("\n"):
            # remove “pontos de preenchimento” e outros símbolos
            linha_norm = re.sub(r"[·…\.]+", " ", linha).strip()
            # busca “nome ... número final”
            m = re.match(r"(.+?)\s+(\d+)\s*$", linha_norm)
            if m:
                nome   = m.group(1).strip()
                preco  = int(m.group(2))
                receitas.append({"nome": nome, "preço": preco})

if not receitas:
    print("⚠️ Não achei nenhum item na página — cheque o padrão de texto.")
    exit(1)

# transforma em DataFrame e salva CSV
df = pd.DataFrame(receitas)
df.to_csv("receitas.csv", index=False)
print("✅ receitas.csv gerado com", len(receitas), "itens.")

import pdfplumber

with pdfplumber.open("menu.pdf") as pdf:
    for pagina, p in enumerate(pdf.pages, 1):
        print(f"--- Página {pagina} ---")
        texto = p.extract_text() or ""
        for i, linha in enumerate(texto.split("\n")[:30], 1):
            # mostramos o índice e a repr() pra ver pontos, espaços, cifrões, etc.
            print(f"{i:02d}: {linha!r}")
        break  # só a primeira página, pra não lotar a saída

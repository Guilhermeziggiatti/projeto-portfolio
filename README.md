# Projeto Portfolio

## Descrição

Este repositório contém a primeira versão de um site estático de **receitas saudáveis**, desenvolvido por Guilherme Ziggiatti. O objetivo é oferecer receitas funcionais, práticas e acessíveis através de um front-end leve, e conter scripts de back-end para extração e tratamento de dados de receitas (a partir de PDF ou HTML).

## Tecnologias Utilizadas

* **Front-end**

  * HTML5, CSS3 (Flexbox, Grid e Responsividade)
  * JavaScript vanilla

* **Back-end / Scripts**

  * Python 3.9+
  * Bibliotecas: `pandas`, `dash`, `plotly`, `pdfplumber`, `tabula-py`

* **Ferramentas**

  * Git e GitHub
  * Ambiente virtual Python (`venv`)

## Estrutura de Pastas

```
projeto-portfolio/
├─ backend/
│  ├─ app.py                  # Aplicação Dash (se aplicável)
│  └─ scripts/                # Scripts de extração de receitas
│     ├─ extrai_receitas_plumber.py
│     ├─ extrai_receitas_tabula.py
│     ├─ extrai_receitas_regex.py
│     └─ debug_extracao.py
├─ frontend/
│  ├─ index.html              # Página principal
│  ├─ menu.pdf                # eBook em PDF
│  └─ assets/
│     ├─ css/style.css        # Estilos globais
│     ├─ js/script.js         # Comportamento na página
│     └─ img/capa-alimentos.jpg # Imagem de fundo
└─ README.md                  # Documentação do projeto
```

## Instalação e Execução Local

1. **Clone este repositório**

   ```bash
   git clone https://github.com/Guilhermeziggiatti/projeto-portfolio.git
   cd projeto-portfolio
   ```

2. **Configure o ambiente virtual e instale as dependências**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install dash pandas plotly pdfplumber tabula-py
   ```

3. **Execute a aplicação**

   * **Front-end**: Abra `frontend/index.html` diretamente no navegador.
   * **Back-end (Dash)**: Caso tenha um dash app em `backend/app.py`, execute:

     ```bash
     cd backend
     python app.py
     ```

     E acesse [http://127.0.0.1:8050](http://127.0.0.1:8050) no navegador.

## Publicação

* **GitHub Pages**: Para publicar somente o front-end estático, ative o GitHub Pages no repositório e aponte para a branch `main` e pasta `/frontend`.
* **Heroku / Vercel / Render**: Para publicar a aplicação Dash, escolha um provedor de hosting Python e siga a documentação específica. Certifique-se de incluir um `Procfile` ou `vercel.json` conforme necessário.

## Contribuições

Contribuições são bem-vindas! Siga estes passos:

1. Fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Faça commits das suas mudanças (`git commit -m 'Adiciona feature X'`).
4. Push para a branch remota (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

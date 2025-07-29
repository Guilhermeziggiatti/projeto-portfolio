#!/usr/bin/env bash
set -e

# 1) Cria a estrutura de pastas
mkdir -p frontend/assets/css frontend/assets/js frontend/assets/img backend/scripts

# 2) Move o front-end
mv index.html            frontend/
mv menu.pdf              frontend/
mv style.css             frontend/assets/css/
mv script.js             frontend/assets/js/
mv imagens/capa-alimentos.jpg frontend/assets/img/
rmdir imagens

# 3) Move o back-end e scripts
mv app.py                          backend/
mv extrai_receitas_plumber.py      backend/scripts/
mv extrai_receitas_tabula.py       backend/scripts/
mv extrai_receitas_regex.py        backend/scripts/
mv debug_extracao.py               backend/scripts/

import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# 1) Carrega dados (ajuste o nome/format)
df = pd.read_csv('receitas.csv')

app = dash.Dash(__name__, title='Dashboard Receitas')

app.layout = html.Div([
    html.H1('Painel de Receitas', style={'textAlign':'center'}),
    dcc.Dropdown(
        id='filtro-categoria',
        options=[{'label': c, 'value': c} for c in df['categoria'].unique()],
        placeholder='Filtrar por categoria'
    ),
    dcc.Graph(id='grafico-pizza'),
    html.Div(id='lista-receitas')
], style={'maxWidth':'800px', 'margin':'auto', 'padding':'20px'})

@app.callback(
    [Output('grafico-pizza', 'figure'),
     Output('lista-receitas', 'children')],
    [Input('filtro-categoria', 'value')]
)
def atualizar(categoria):
    dff = df if not categoria else df[df['categoria']==categoria]
    fig = px.pie(dff, names='categoria', hole=0.4, title='Distribuição')
    cards = [
        html.Div([
            html.H3(row['título']),
            html.P(f"Tempo: {row['tempo_min']} min"),
            html.P(f"Ingredientes: {row['ingredientes']}")
        ], style={
            'border':'1px solid #ccc','borderRadius':'8px',
            'padding':'10px','marginBottom':'10px'
        }) for _, row in dff.iterrows()
    ]
    return fig, cards

if __name__=='__main__':
    app.run_server(debug=True, port=8050)

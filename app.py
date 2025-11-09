import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from data.placeholder_data import get_placeholder_data


# Load data
df = get_placeholder_data()


# Dash app initialization
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# Layout
app.layout = html.Div([
html.Header(
[html.Img(src='/assets/logo.svg', className='logo'), html.H1('Mai Shan Yun Inventory Intelligence')],
className='header'
),


html.Div([
html.Nav([
html.H3('Dashboard Navigation'),
html.Ul([
html.Li('Inventory Overview'),
html.Li('Usage Trends'),
html.Li('Forecasting'),
])
], className='sidebar'),


html.Main([
html.H2('Interactive Graph Placeholder'),
dcc.Graph(
id='example-graph',
figure=px.line(df, x='Month', y='Inventory Level', title='Inventory Over Time')
)
], className='content')
], className='container')
])


if __name__ == '__main__':
app.run_server(host='0.0.0.0', port=8080, debug=False)

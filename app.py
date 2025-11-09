import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from data.placeholder_data import get_placeholder_data

# === Load placeholder data ===
df = get_placeholder_data()

# === Initialize Dash app ===
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server

# === Define reusable example figures (created once, not regenerated each render) ===
fig_inventory = px.line(
    df, x="Month", y="Inventory Level",
    title="Inventory Over Time", markers=True
)
fig_usage = px.bar(
    df, x="Month", y="Inventory Level",
    title="Ingredient Usage Trends",
    color_discrete_sequence=["#500000"]
)
fig_forecast = px.scatter(
    df, x="Month", y="Inventory Level",
    title="Forecasting (Placeholder)",
    trendline="ols"
)

# === Freeze layout config to prevent continuous updates ===
graph_config = {"staticPlot": True, "displayModeBar": False}

# === Define layout as a function for clean instantiation ===
def serve_layout():
    return html.Div([
        # Header
        html.Header([
            html.Img(src="/assets/logo.svg", className="logo"),
            html.H1("Mai Shan Yun Inventory Intelligence")
        ], className="header"),

        # Main container
        html.Div([
            # Sidebar navigation
            html.Nav([
                html.H3("Dashboard Navigation"),
                dcc.RadioItems(
                    id="page-selector",
                    options=[
                        {"label": "Inventory Overview", "value": "inventory"},
                        {"label": "Usage Trends", "value": "usage"},
                        {"label": "Forecasting", "value": "forecast"}
                    ],
                    value="inventory",
                    className="sidebar-radio"
                )
            ], className="sidebar"),

            # Content area
            html.Main([
                html.H2(id="graph-title", children="Inventory Overview"),
                dcc.Graph(
                    id="main-graph",
                    figure=fig_inventory,
                    config=graph_config
                )
            ], className="content")
        ], className="container")
    ])

app.layout = serve_layout

# === Callback for switching graphs ===
@app.callback(
    Output("main-graph", "figure"),
    Output("graph-title", "children"),
    Input("page-selector", "value")
)
def update_graph(selected_page):
    """Switch between graphs without reloading layout."""
    if selected_page == "usage":
        return fig_usage, "Usage Trends"
    elif selected_page == "forecast":
        return fig_forecast, "Forecasting (Placeholder)"
    else:
        return fig_inventory, "Inventory Overview"

# === Run server ===
if __name__ == "__main__":
    # debug=False prevents autoreload that can re-trigger loops on Render
    app.run_server(host="0.0.0.0", port=8080, debug=False)

# app.py
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# --- SAMPLE DATA (placeholder only) ---
df_sample = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=12, freq="M"),
    "usage": [50, 60, 55, 80, 75, 90, 120, 110, 95, 85, 70, 65],
    "purchases": [60, 55, 65, 70, 90, 85, 140, 100, 100, 80, 70, 60]
})

fig_usage = px.line(df_sample, x="date", y="usage", title="Ingredient Usage (Placeholder)")
fig_purchases = px.bar(df_sample, x="date", y="purchases", title="Purchases (Placeholder)")
fig_forecast = px.line(
    df_sample.assign(forecast=[u * 1.1 for u in df_sample.usage]),
    x="date", y="forecast", title="Forecast (Placeholder)"
)

# --- APP SETUP ---
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server  # for Render.com

# --- HEADER WITH LOGO ---
header = html.Header(
    [
        html.Div(
            className="header-left",
            children=[
                html.Img(
                    src="/assets/logo-placeholder.png",
                    className="header-logo",
                    alt="Mai Shan Yun Logo"
                ),
                html.Div(
                    children=[
                        html.Div("Mai Shan Yun — Inventory Intelligence", className="header-title"),
                        html.Div("College Station — Aggie Edition", className="header-sub"),
                    ],
                    className="header-text"
                ),
            ],
        ),
        html.Button("—", id="toggle-header", title="Minimize header", className="min-btn"),
    ],
    className="top-header",
    id="top-header"
)

# --- SIDEBAR ---
sidebar = html.Div(
    [
        html.Div(className="logo-wrap", children=[
            html.Img(src="/assets/logo-placeholder.png", className="logo", alt="Sidebar Logo"),
        ]),
        html.Hr(className="sidebar-divider"),
        html.Div([
            dcc.RadioItems(
                id="nav-selection",
                options=[
                    {"label": "Inventory Overview", "value": "overview"},
                    {"label": "Ingredient Usage", "value": "usage"},
                    {"label": "Purchases & Shipments", "value": "purchases"},
                    {"label": "Forecasting", "value": "forecasting"},


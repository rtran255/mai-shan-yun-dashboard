import dash
from dash import html, dcc, Input, Output

# --- Initialize app ---
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # for Render

# --- Header ---
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
                        html.Div("College Station — Aggie Edition", className="header-sub")
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

# --- Sidebar ---
sidebar = html.Div(
    className="sidebar",
    id="sidebar",
    children=[
        html.Div(
            className="logo-wrap",
            children=[
                html.Img(src="/assets/logo-placeholder.png", className="logo", alt="Mai Shan Yun Logo"),
                html.H2("Dashboard", className="sidebar-title"),
            ]
        ),
        html.Div(
            className="nav-links",
            children=[
                html.Label("Select Graph View:", className="nav-label"),
                dcc.Dropdown(
                    id="graph-selector",
                    options=[
                        {"label": "Inventory Overview", "value": "inventory"},
                        {"label": "Ingredient Usage", "value": "ingredients"},
                        {"label": "Purchases & Shipments", "value": "purchases"},
                        {"label": "Forecasting", "value": "forecasting"},
                    ],
                    value="inventory",
                    clearable=False,
                    className="dropdown"
                ),
            ],
        ),
    ]
)

# --- Main content area ---
main_content = html.Div(
    className="main-content",
    id="main-content",
    children=[
        dcc.Graph(id="main-graph", figure={}),
        html.Div(id="graph-description", className="graph-desc")
    ]
)

# --- Layout ---
app.layout = html.Div(
    className="dashboard-container",
    children=[header, html.Div(className="content-area", children=[sidebar, main_content])]
)

# --- Callbacks ---
@app.callback(
    Output("main-graph", "figure"),
    Output("graph-description", "children"),
    Input("graph-selector", "value")
)
def update_graph(selected):
    # Placeholder content for now
    if selected == "inventory":
        desc = "Overview of all inventory items and usage trends."
    elif selected == "ingredients":
        desc = "Monthly ingredient usage and top/least used ingredients."
    elif selected == "purchases":
        desc = "Shipment and purchase analysis by date."
    elif selected == "forecasting":
        desc = "Predictive trends and restock suggestions."
    else:
        desc = "Select a view to explore inventory intelligence."

    return {}, desc


# --- Run server ---
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=False)

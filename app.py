from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from pages import dashboard,geography,question,data_helper,design_helper


# build your Dash app
app = Dash(__name__, suppress_callback_exceptions=True,assets_folder='assets', external_stylesheets=[dbc.themes.BOOTSTRAP,'typography.css'],use_pages=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content'),
    dcc.Store(id='storage',data=[],storage_type='memory'),
    dcc.Store(id='sentence',data=[],storage_type='memory'),
    dcc.Store(id='dashboard_tables',data=[],storage_type='memory')
])

layout_home=html.Div(
    style={'display':'flex','flexDirection':'column'},
    children=[
        design_helper.top_banner(),
        design_helper.landing_page_paragraph1(),
        design_helper.landing_page_paragraph2(),
        design_helper.proceed_button()
    ]
)


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname=='/dashboard':
        return dashboard.layout
    elif pathname=='/dashboard-geography':
        return geography.layout_geography
    elif pathname=='/statement':
        return question.layout_question
    else:
        return layout_home
if __name__ == '__main__':    
    app.run_server(debug=True)
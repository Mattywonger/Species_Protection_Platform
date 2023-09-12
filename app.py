from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash_bootstrap_components as dbc
from pages import dashboard,geography,question,data_helper


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
        html.Div(
            style={'display': 'flex',
                   'width': '1728px',
                    'height': '111px',
                    'padding': '26px 709px 27px 104px',
                    'align-items': 'center',
                    'flex-shrink': 0,
                    'background': 'black'},
                children=[
                    html.Img(src='assets/Tree.png',style={'width': '54.908px','height': '48.004px', 'flex-shrink': 0,'display':'inline-block'}),
                   html.Img(src='assets/Project.png',style={'width': '140.438px','height': '42.499px', 'flex-shrink': 0,'display':'inline-block'}),
                    html.Img(src='assets/six_buttons.png',style={'width': '12px','height': '21px','flex-shrink': 0}),
                    html.Img(src='assets/Canopy.png',style={'width': '127.164px','height': '42.499px','flex-shrink': 0,'fill': 'rgba(215, 216, 219, 0.80)'}),
            ]
                ),
        html.Div(
            style={'margin-top':'150px','margin-left':'104px','margin-right':'709px'},
            children=[
                html.Div("At Project Canopy, we mine, synthesize, and translate the data so that you can \n maximize your effort conserving the Congo Basin.")
            ]
                ),
        
        html.Div(
            style={'margin-top':'54px','margin-left':'104px','margin-right':'709px'},
            children=[
                html.Div("Simply adapt the statement on the next page to arrive at the actionable data you need.")
            ]
        ),

         html.Div(
            style={'margin-left':'104px','margin-top':'103px','margin-right':'1466px'},
            children=[dbc.Button('Proceed',id='proceed-button',href="/statement")]
        ),

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

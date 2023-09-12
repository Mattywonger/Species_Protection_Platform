import dash_bootstrap_components as dbc
from pages import geography,dashboard
from dash import dcc, html, Input, Output, callback,dash_table
import plotly.express as px
import pandas as pd
import dash_daq as daq

df_geography=pd.read_csv("NSL_master.csv")
df_geo_count=pd.read_csv("Geography_count_master.csv")



layout_geography= html.Div(
        style={'display':'flex', 'flexDirection':'column'},
        children=[
             html.Div( #1
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
                    html.Img(src='assets/Canopy.png',style={'width': '127.164px','height': '42.499px','flex-shrink': 0,'fill': 'rgba(215, 216, 219, 0.80)'})]),
            html.Div("The current Conservation Status of all land vertebrates in the Congo Basin."), #2
            html.Div( #3
    style={
        'display': 'flex',
        'flexDirection': 'row'  # Set the flex direction to 'row'
    },
    children=[
    html.Div( #3.1
        style={'width': '247px', 'height': '839px','background-color':'blue'}
    ),
    html.Div(#3.2
            style={  'display': 'flex',
                     'flexDirection': 'column'} , #The style for 3.2

            children=[
                html.Div(
                    html.H2("Protections by Geography",style={"width":'378px',"height":"35px","margin-bottom":"4px",'margin-left':'80px'})
                ),
                html.Div(
                     dash_table.DataTable( #3.21
                        id='table_geography_top',
                        columns=[
                            {"name": ["Conservation Status", ""], "id": "Conservation"},
                            {"name": ["National Protection", "Region"], "id": "Region"},
                            {"name": ["National Protection", "CMR"], "id": "CMR"},
                            {"name": ["National Protection", "CAR"], "id": "CAR"},
                            {"name": ["National Protection", "DRC"], "id": "DRC"},
                            {"name": ["National Protection", "EQG"], "id": "EQG"},
                            {"name": ["National Protection", "GAB"], "id": "GAB"},
                             {"name": ["National Protection", "ROC"], "id": "ROC"},
                            {"name": ["Int'l Proetection", "CITES"], "id": "humidity"}
                        ],
                                data=df_geo_count.to_dict('records'),
                                style_table={'maxHeight':'330px', 'overflowY':'scroll','border':'0'},
                                page_size=10000,
                                merge_duplicate_headers=True)),
                

                html.Div(
                    html.H2("Protections by Species",style={"width":'378px',"height":"35px","margin-bottom":"4px",'margin-left':'80px','margin-top':'50px'})
                ),
                html.Div(
                    style={'width':'1264px','margin-left':'35px'},
                    children=
                        dash_table.DataTable( #3.22
                        id='table_geography',
                        columns=[
                            {"name": ["Species Information", "Scientific"], "id": "scientific_name_CM_final"},
                            {"name": ["National Protection", "CMR"], "id": "classification"},
                            {"name": ["National Protection", "CAR"], "id": "class_CD"},
                            {"name": ["National Protection", "DRC"], "id": "class_CF"},
                            {"name": ["National Protection", "EQG"], "id": "class_CG"},
                            {"name": ["National Protection", "GAB"], "id": "class_GA"},
                            {"name": ["Int'l Proetection", "CITES"], "id": "humidity"}
                        ],
                                data=df_geography.to_dict('records'),
                                style_data_conditional=[ 
                                    
                                    {'if':{'column_id':'scientific_name_CM_final'},
                                     'background':' var(--background-light-gray-b, #E1E2E3)',
                                        'border':'none'
                                    },
                                    {
                                        'if': {'column_id': 'classification'},
                                        'backgroundColor': 'grey',
                                        'border':'none',
                                    },
                                    {
                                        'if': {'column_id': 'class_CD'},
                                        'backgroundColor': 'grey',
                                        'border':'none'
                                    },
                                    {
                                        'if': {'column_id': 'class_CF'},
                                        'backgroundColor': 'grey',
                                        'border':'none'
                                    },
                                    {
                                        'if': {'column_id': 'class_CG'},
                                        'backgroundColor': 'grey',
                                        'border':'none'
                                    },
                                    {
                                        'if': {'column_id': 'class_GA'},
                                        'backgroundColor': 'grey',
                                        'border':'none'
                                    },
                                    {
                                        'if': {
                                           'column_id':'humidity'
                                        },
                                        'background':' var(--background-light-gray-b, #E1E2E3)',
                                        'border':'none'
                                    },
                                ],
                            style_table={'maxHeight':'365px', 'overflowY':'scroll','border':'0'},
                                page_size=10000,
                                merge_duplicate_headers=True))
                    ])]
            )]
                
)















'''
layout_geography=dbc.Container([
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id="geography_count",
                columns=[
                    {"name": ["Conservation Status", ""], "id": "Header"},
        {"name": ["National Protection", "Region"], "id": "Region"},
        {"name": ["National Protection", "CMR"], "id": "CMR"},
        {"name": ["National Protection", "CAR"], "id": "CAR"},
        {"name": ["National Protection", "DRC"], "id": "DRC"},
        {"name": ["National Protection", "EQG"], "id": "EQG"},
        {"name": ["National Protection", "GAB"], "id": "GAB"},
        {"name": ["Int'l Proetection", "INT'L"], "id": "humidity"}
                ],
                data = df_geo_count.to_dict('records'),
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='table_geography',
                columns=[
        {"name": ["Species Information", "Scientific"], "id": "scientific_name_CM_final"},
        {"name": ["National Protection", "CMR"], "id": "classification"},
        {"name": ["National Protection", "CAR"], "id": "class_CD"},
        {"name": ["National Protection", "DRC"], "id": "class_CF"},
        {"name": ["National Protection", "EQG"], "id": "class_CG"},
        {"name": ["National Protection", "GAB"], "id": "class_GA"},
        {"name": ["Int'l Proetection", "CITES"], "id": "humidity"}
    ],
                data=df_geography.to_dict('records'),
                page_size=10000,
                 merge_duplicate_headers=True)
        ])
    ])
])
'''
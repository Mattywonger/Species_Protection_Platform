from dash import Dash, html, dcc, callback, Output, Input, dash_table, State
import dash_bootstrap_components as dbc
from pages import data_helper
import pandas as pd
import dash_daq as daq

df_count_CM,df_GA,df_CD,df_CM,df_GQ,df_CF,df_CG,df_master = data_helper.csv_reading()
df_geography=pd.read_csv("NSL_master.csv")
df_geo_count=pd.read_csv("Geography_count_master.csv")

def complete_table():
    return html.Div(
        style={'display':'flex', 'flexDirection':'column'},
        children=[
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
                                style_data_conditional=style_conditional(),
                                style_table={'maxHeight':'365px', 'overflowY':'scroll','border':'0'},
                                page_size=10000,
                                merge_duplicate_headers=True))
                    ])

def style_conditional():
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
                                ]
    return style_data_conditional

def country_sentence():
    return html.Div(id='country-sentence',style={'display':'flex','width': '1352px','height': '28px','margin-bottom':'46px','margin-top':'49px','margin-left':'46px','font-size':'32px'},children=[])

def top_banner():
    return html.Div(style={'display': 'flex', 'width': '1728px', 'height': '111px', 'padding': '26px 709px 27px 104px', 'align-items': 'center', 'flex-shrink': 0, 'background': 'black'},
                    children=[
                    html.Img(src='assets/Tree.png', style={
                             'width': '54.908px', 'height': '48.004px', 'flex-shrink': 0, 'display': 'inline-block'}),
                    html.Img(src='assets/Project.png', style={
                             'width': '140.438px', 'height': '42.499px', 'flex-shrink': 0, 'display': 'inline-block'}),
                    html.Img(src='assets/six_buttons.png',
                             style={'width': '12px', 'height': '21px', 'flex-shrink': 0}),
                    html.Img(src='assets/Canopy.png', style={
                             'width': '127.164px', 'height': '42.499px', 'flex-shrink': 0, 'fill': 'rgba(215, 216, 219, 0.80)'}),
                    ]
                    )


def landing_page_paragraph1():
    return html.Div(
        style={'margin-top': '150px',
               'margin-left': '104px', 'margin-right': '709px'},
        children=[
            html.Div(
                "At Project Canopy, we mine, synthesize, and translate the data so that you can \n maximize your effort conserving the Congo Basin.")
        ]
    )


def landing_page_paragraph2():
    return html.Div(
        style={'margin-top': '54px', 'margin-left': '104px',
               'margin-right': '709px'},
        children=[
            html.Div(
                "Simply adapt the statement on the next page to arrive at the actionable data you need.")
        ]
    )


def proceed_button():
    return html.Div(
        style={'margin-left': '104px',
               'margin-top': '103px', 'margin-right': '1466px'},
        children=[dbc.Button(
            'Proceed', id='proceed-button', href="/statement")]
    )


def question_dropdown(category):
    if (category == "time"):
        return html.Div(
            style={'display': 'flex', 'flexDirection': 'column',
                   'margin-left': '12px'},
            children=[

                html.Button("Select Time", id='collapse-button-Time', style={'border': 'none', 'text-decoration': 'underline', 'background-color': 'transparent',
                            'font-size': '20px', 'font-family': 'IBM Plex Sans Regular', 'font-weight': '300', 'line-height': '150%'}),
                html.Div(id='collapsible-section-Time', children=[
                    dcc.Checklist(
                        ['Current', 'Historic'],
                        ['Current'],
                        id='checkboxes-Time',
                        labelStyle={'display': 'block'}
                    )
                ])
            ])
    elif (category == "conservation"):
        return html.Div(
            style={'display': 'flex', 'flexDirection': 'column',
                   'margin-left': '12px'},
            children=[
                html.Button("Select Conservation", id='collapse-button-Conservation', style={'border': 'none', 'text-decoration': 'underline',
                            'background-color': 'transparent', 'font-size': '20px', 'font-family': 'IBM Plex Sans Regular', 'font-weight': '300', 'line-height': '150%'}),
                html.Div(id='collapsible-section-Conservation', children=[
                    dcc.Checklist(
                        ['Conservation', 'National Protections',
                         'Int Protections (CITES)'],
                        ['Conservation'],
                        id='checkboxes-Conservation',
                    )
                ])
            ],)
    

    elif (category == "species"):
        return html.Div(
            style={'display': 'flex', 'flexDirection': 'column',
                   'margin-left': '12px'},
            children=[
                html.Button("Select Species", id='collapse-button-Species', style={'border': 'none', 'text-decoration': 'underline',
                            'background-color': 'transparent', 'font-size': '20px', 'font-family': 'IBM Plex Sans Regular', 'font-weight': '300', 'line-height': '150%'}),
                html.Div(id='collapsible-section-Species', children=[
                    dcc.Checklist(
                            ['Amphibians', 'Reptiles', 'Birds', 'Mammals'],
                            ['Amphibians'],
                            id='checkboxes-Species',
                            labelStyle={'display': 'block'}
                    )
                ])
            ])
    else:
        return html.Div(
            style={'display': 'flex', 'flexDirection': 'column'},
            children=[
                html.Button("select Country", id='collapse-button-Country', style={'border': 'none', 'text-decoration': 'underline',
                            'background-color': 'transparent', 'font-size': '20px', 'font-family': 'IBM Plex Sans Regular', 'font-weight': '300', 'line-height': '150%'}),
                html.Div(id='collapsible-section-Country', children=[
                    dcc.Checklist(
                            ['Cameroon', 'Central African Republic', 'DRC',
                                'Gabon', 'Equitorial Guinea', 'Republic of Congo'],
                            ['Cameroon'],
                            id='checkboxes-Country',
                            labelStyle={'display': 'block'}
                    )
                ])
            ]
        )


def submit_button():
    return html.Div(
        style={'margin-top': '387px', 'margin-left': '107px',
               'margin-bottom': '135px'},
        children=[
            dbc.Button('Submit', id='submit-button', href="/dashboard",
                       style={'background-color': 'black', 'color': 'white'})
        ]
    )


def left_panel():
    return html.Div(
        style={'display': 'flex', 'flexDirection': 'column','width': '360px', 'height': '1025px', 'margin-left': '46px'},
        className="gradientblue",
        children=[  # children clause for 3.1 exclusively
            html.Div(
                style={'display': 'flex', 'flexDirection': 'row',"height":"64px","width":"360px"},
                className="gradient-black",
                children=[
                    html.Div(style=data_helper.auto_style(36,64,41,0,12,16),
                                children=[html.Img(src='assets/one.png')]
                    ),
                    html.Div('Filters',className='section-titles')
                ]
            ),
            html.Div(
                style={'display': 'flex', 'flexDirection': 'row','margin-top':'124px'},
                children=[
                    html.Img(src='assets/calendar.png',
                             style={'margin-right': '16px'}),
                    html.Div("CHART VIEW",className="whitetext")]),

            html.Div(
                style={'display': 'flex', 'flexDirection': 'row','margin-top':'23px'},
                children=[
                    html.Div("By Species"),
                    html.Div(children=[daq.ToggleSwitch(id="my-toggle",value=False)]),
                    html.Div("By Geography")]),
            html.Div(
                style={'display': 'flex', 'flexDirection': 'row','margin-top':'13px'},
                children=[
                    html.Div("By Counts"),
                    html.Div(className="toggle",children=[daq.ToggleSwitch(id="my-toggle",value=False)]),
                    html.Div("By Percentages")]),

            html.Div(
                style={'margin-top': '52px',
                       'display': 'flex', 'flexDirection': 'row'},
                children=[
                    html.Img(src='assets/filter.png',
                             style={'margin-right': '16px'}),
                    html.Div("Filters",className="whitetext")
                ]
            ),

            html.Div(
                html.Img(src='assets/Vector_line.png',
                         style={'margin-top': '9.5px'})
            ),

            html.Div(
                dcc.Checklist(
                    ['Rainforest Only', 'Endemic Only', 'Exclude Data Deficient'],
                    id='control-dropdown',
                    style={'font-family': 'IBM Plex Sans'}
                )
            ),
            html.Div(
                style={'display': 'flex', 'flexDirection': 'row',
                       'margin-top': '55px'},
                children=[
                    html.Img(src='assets/calendar.png',
                             style={'margin-right': '9px'}),
                    html.Div("Last accessed",className="whitetext")
                ]
            ),
            html.Div(
                html.Img(src='assets/Vector_line.png',
                         style={'margin-top': '11.5px'})
            ),
            html.Div(
                dcc.Checklist(
                    ['10 >',  '10 <'],
                    id='control-dropdown1',
                    style={'display': 'inline-block', 'margin-right': '19px'},
                    className="left-panel-dropdowntext"
                )
            ),
#dividing line
            html.Div(
                style={'display': 'flex', 'flexDirection': 'row',
                       'margin-top': '55px'},
                children=[
                    html.Img(src='assets/settings.png',
                             style={'margin-right': '9px'}),
                    html.Div("PRESETS",className="whitetext")
                ]
            ),
            html.Div(
                html.Img(src='assets/Vector_line.png',
                         style={'margin-top': '11.5px'})
            ),
            html.Div(
                dcc.Checklist(
                    ['Show all species that receive full protection ',  'Show only species that are protected in one country but not others'],
                    id='control-dropdown2',
                    style={'display': 'inline-block', 'margin-right': '19px'},
                    className="left-panel-dropdowntext"
                )
            ),

            html.Div(
                style={'width':'363px','height':'2px','margin-top': '132px'},
                className='vectorline'
            ),
            html.Div(
                style={'display': 'flex', 'flexDirection': 'column','margin-top': '45px', 'paddingRight': '28px'},
                children=[
                    html.Div(
                        style={'display': 'flex', 'flexDirection': 'row'},
                        children=[
                            html.Img(src='assets/printer.png',
                                     style={'margin-right': '8px'}),
                            html.Div('PRINT',className="whitetext")
                        ]
                    )
                ]
            ),
            
            html.Div(
                style={'display': 'flex', 'flexDirection': 'row','margin-top':'40px'},
                children=[
                    html.Img(src='assets/share.png',
                                style={'margin-right': '8px'}),
                    html.Div('SHARE',className="whitetext")
                        ]
                    )
        ]
    )

def two_banner():
    return html.Div(
        style=data_helper.auto_style_flex("row",1365,64,2,0,23,0),
        className='black',
        children=[
            html.Img(src='assets/one.png',style=data_helper.auto_style(36,36,35,0,11,11)),
            html.Div("NATIONAL PROTECTIONS",className="section-titles"),
            html.Div(style={'width':'37px','height':'37px','margin-left':'72px'},className="solidnavyblue"),
            html.Div("Class A",style={'margin-left':'11px'},className="classwords"),
            html.Div(style={'width':'37px','height':'37px','margin-left':'24px'},className="solidmediumblue"),
            html.Div("Class B",style={'margin-left':'11px'},className="classwords"),
            html.Div(style={'width':'37px','height':'37px','margin-left':'24px'},className="solidlightblue"),
            html.Div("Class C",style={'margin-left':'11px'},className="classwords")
        ]
    )
def three_banner():
    return html.Div(
        style=data_helper.auto_style_flex("row",1365,64,2,0,1,0),
        className='black',
        children=[
            html.Img(src='assets/one.png',style=data_helper.auto_style(36,36,35,0,11,11)),
            html.Div("RESULTING SPECIES LIST",className="section-titles"),
        ]
    )

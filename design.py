from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from IPython.display import display
import dash_daq as daq
from pages import data_helper

def table_generation(df):
    table=dash_table.DataTable(
                        id='table',
                        columns=[{"name": i, "id": i} 
                            for i in df.columns],
                        data=df.to_dict('records'),
                        style_header=dict(backgroundColor="paleturquoise"),
                        style_data=dict(backgroundColor="lavender"),
                    # fixed_rows={'headers':True},
                        style_table={'maxHeight':'808px', 'overflowY':'scroll'},
                        style_cell={'minWidth':95,'maxWidth':95,'width':95,'textAlign':'left'},
                        style_data_conditional=[ 
                                            {'if':{ 'filter_query': '{Threat Class} eq "LC"'},
                                            'background':' var(--background-light-gray-b, #E1E2E3)',
                                                'border':'none'
                                            }
                        ],
                        page_size=10000,
            )
    return table
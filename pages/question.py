from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
from pages import geography,dashboard
import dash_bootstrap_components as dbc
from IPython.display import display
from pages import data_helper,design_helper,data_preparation

#CSV--> DF
df_count_CM,df_GA,df_CD,df_CM,df_GQ,df_CF,df_CG,df_master = data_helper.csv_reading()

#Data Preparation:



layout_question = html.Div(
    style={'display':'flex','flexDirection':'column'},
    children=[
        design_helper.top_banner(),
        html.Div(
            style={'height':'69px','margin-left':'108px','flex-shrink': 0,'margin-top':'105px'},
            children=[html.Div("Tell me,",style={'font-family':'IBM Plex Sans Medium','font-size':'35px','font-weight':500,'line-height':'normal'})]
        ),

        html.Div(
        style={'display':'flex','flexDirection':'row','margin-left':'108px'},
        children=[

            html.Div("Which are the",style={'font-size': '20px','font-family':'IBM Plex Sans Light','font-weight':'300', 'line-height':'150%'}),
            design_helper.question_dropdown("time"),
            design_helper.question_dropdown("conservation"),
            design_helper.question_dropdown("species"),
            design_helper.question_dropdown("countries"),
            
        ]
    ),
            html.H1("Testing the new method",className="my-custom-text"),
            design_helper.submit_button()
    ]

)

#COLLAPSE CALLBACK

@callback(
    Output('collapsible-section-Time', 'style'),
    Output('collapse-store-Time', 'data'),
    Output('collapse-button-Time', 'children'),
    Input('collapse-button-Time', 'n_clicks'),
    Input('collapse-store-Time', 'data'),
    Input('checkboxes-Time', 'value'),
    State('collapse-button-Time', 'children')
)
def toggle_collapse(n_clicks, collapse_state,select,button_text):
    if n_clicks is None:
        return {'display': 'none'}, collapse_state, button_text
    
    new_collapse_state = not collapse_state
    new_button_text = data_helper.list_to_string(select,'and')
    display_style = {'display': 'block' if new_collapse_state else 'none'}
    return display_style,new_collapse_state, new_button_text

@callback(
    Output('collapsible-section-Conservation', 'style'),
    Output('collapse-store-Conservation', 'data'),
    Output('collapse-button-Conservation', 'children'),
    Input('collapse-button-Conservation', 'n_clicks'),
    Input('collapse-store-Conservation', 'data'),
    Input('checkboxes-Conservation', 'value'),
    State('collapse-button-Conservation', 'children')
)
def toggle_collapse(n_clicks, collapse_state,select,button_text):
    if n_clicks is None:
        return {'display': 'none'}, collapse_state, button_text
    
    new_collapse_state = not collapse_state
    new_button_text = data_helper.list_to_string(select,'and')
    display_style = {'display': 'block' if new_collapse_state else 'none'}
    return display_style, new_collapse_state, new_button_text

@callback(
    Output('collapsible-section-Species', 'style'),
    Output('collapse-store-Species', 'data'),
    Output('collapse-button-Species', 'children'),
    Input('collapse-button-Species', 'n_clicks'),
    Input('collapse-store-Species', 'data'),
    Input('checkboxes-Species', 'value'),
    State('collapse-button-Species', 'children')
)
def toggle_collapse(n_clicks, collapse_state,select,button_text):
    if n_clicks is None:
        return {'display': 'none'}, collapse_state, button_text
    
    new_collapse_state = not collapse_state
    new_button_text = data_helper.list_to_string(select,'and')
    display_style = {'display': 'block' if new_collapse_state else 'none'}
    return display_style, new_collapse_state, new_button_text

@callback(
    Output('collapsible-section-Country', 'style'),
    Output('collapse-store-Country', 'data'),
    Output('collapse-button-Country', 'children'),
    Input('collapse-button-Country', 'n_clicks'),
    Input('collapse-store-Country', 'data'),
    Input('checkboxes-Country', 'value'),
    State('collapse-button-Country', 'children')
)
def toggle_collapse(n_clicks, collapse_state,select,button_text):
    if n_clicks is None:
        return {'display': 'none'}, collapse_state, button_text
    
    new_collapse_state = not collapse_state
    new_button_text = data_helper.list_to_string(select,'and')
    display_style = {'display': 'block' if new_collapse_state else 'none'}
    return display_style, new_collapse_state, new_button_text

#----------------------------------------------


@callback(
    Output('dashboard_tables','data'),
    Output('storage','data'),
    Input('checkboxes-Time', 'value'),
    Input('checkboxes-Conservation', 'value'),
    Input('checkboxes-Species', 'value'),
    Input('checkboxes-Country', 'value'),
)
def handle_question_py(time,conservation,species,country):
    return df_master.to_dict('records'),df_master.to_dict('records')


@callback(
    Output('submit-button','href'),
    Input('submit-button','n_clicks'),
    Input('conservation-boolean','data')
)

def update_href(clicks,conservation):
    if clicks==0:
        print("not clicked yet")
    else:
        conservation=data_helper.list_to_string(conservation)
        if conservation=='Conservation':
            return '/dashboard'
        else:
            return '/dashboard-geography'



@callback(
    Output('sentence','data'),
    [Input('checkboxes-Time','value'),Input('checkboxes-Conservation','value'),Input('checkboxes-Species','value'),Input('checkboxes-Country','value')])

def store_sentence(time,conservation,species,country):
    query_list=[]
    query_list.append(time)
    query_list.append(conservation)
    query_list.append(species)
    query_list.append(country)

    return query_list




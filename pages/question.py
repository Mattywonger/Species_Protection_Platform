from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
from pages import geography,dashboard
import dash_bootstrap_components as dbc
from IPython.display import display
from pages import data_helper

#CSV--> DF
df_count_CM=pd.read_csv('Species_count_CM.csv')
df_test=pd.read_csv('Species_count_GB.csv')
df_GA=pd.read_csv('data_species_master/species_masterGA.csv')
df_CD=pd.read_csv('data_species_master/Species_masterCD.csv')
df_CM=pd.read_csv('data_species_master/Species_masterCM.csv')
df_GQ=pd.read_csv('data_species_master/Species_masterGQ.csv')
df_CF=pd.read_csv('data_species_master/Species_masterCF.csv')
df_CG=pd.read_csv('data_species_master/Species_masterCG.csv')
df_master=pd.read_csv('Species_count.csv')


layout_question = html.Div(
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
            ]),
        html.Div(
            style={'height':'69px','margin-left':'108px','flex-shrink': 0,'margin-top':'105px'},
            children=[html.Div("Tell me,",style={'font-family':'IBM Plex Sans Medium','font-size':'35px','font-weight':500,'line-height':'normal'})]
        ),

        html.Div(
        style={'display':'flex','flexDirection':'row','margin-left':'108px'},
        children=[

            html.Div("Which are the",style={'font-size': '20px','font-family':'IBM Plex Sans Light','font-weight':'300', 'line-height':'150%'}),
            html.Div(
                style={'display':'flex','flexDirection':'column','margin-left':'12px'},
                children=[
                    
                    html.Button("Select Time", id='collapse-button-Time',style={'border':'none','text-decoration':'underline','background-color':'transparent','font-size': '20px','font-family':'IBM Plex Sans Regular','font-weight':'300', 'line-height':'150%'}),
                    html.Div(id='collapsible-section-Time', children=[
                             dcc.Checklist(
                        ['Current', 'Historic'],
                        ['Current'],
                        id='checkboxes-Time',
                        labelStyle={'display': 'block'}

                                    )    
    ])
                ],),

            html.Div(
                style={'display':'flex','flexDirection':'column','margin-left':'12px'},
                children=[
                    html.Button("Select Conservation", id='collapse-button-Conservation',style={'border':'none','text-decoration':'underline','background-color':'transparent','font-size': '20px','font-family':'IBM Plex Sans Regular','font-weight':'300', 'line-height':'150%'}),
                    html.Div(id='collapsible-section-Conservation', children=[
                             dcc.Checklist(
                        ['Conservation', 'National Protections', 'Int Protections (CITES)'],
                        ['Conservation'],
                        id='checkboxes-Conservation',
                                    )  
    ])
                ],),
            

            html.Div(
                style={'display':'flex','flexDirection':'column','margin-left':'12px'},
                children=[
                    html.Button("Select Species", id='collapse-button-Species',style={'border':'none','text-decoration':'underline','background-color':'transparent','font-size': '20px','font-family':'IBM Plex Sans Regular','font-weight':'300', 'line-height':'150%'}),
                    html.Div(id='collapsible-section-Species', children=[
                            dcc.Checklist(
                        ['Amphibians', 'Reptiles','Birds','Mammals'],
                        ['Amphibians'],
                        id='checkboxes-Species',
                        labelStyle={'display': 'block'}
                                    )
    ])
                ],),
            html.Div(
                style={'display':'flex','flexDirection':'column'},
                children=[
                    html.Button("select Country", id='collapse-button-Country',style={'border':'none','text-decoration':'underline','background-color':'transparent','font-size': '20px','font-family':'IBM Plex Sans Regular','font-weight':'300', 'line-height':'150%'}),
                    html.Div(id='collapsible-section-Country', children=[
                            dcc.Checklist(
                        ['Cameroon','Central African Republic','DRC', 'Gabon', 'Equitorial Guinea','Republic of Congo'],
                        ['Cameroon'],
                        id='checkboxes-Country',
                        labelStyle={'display': 'block'}
                                    )
    ])
                ],
            ),
        ]
    ),
    
        html.Div(
            style={'margin-top':'387px','margin-left':'107px','margin-bottom':'135px'},
            children=[
            dbc.Button('Submit',id='submit-button',href="",style={'background-color':'black','color':'white'})
            ]
        )
        
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
    Output('conservation-boolean','data'),
    Input('checkboxes-Time', 'value'),
    Input('checkboxes-Conservation', 'value'),
    Input('checkboxes-Species', 'value'),
    Input('checkboxes-Country', 'value'),
)

def data_parsing(time,conservation,species,country):
    species_list=['Amphibians','Reptiles','Birds',"Mammals"]
    country=data_helper.list_to_string(country,'and')
    index_list=[]
    conservation_list=[]

    if ((data_helper.list_to_string(conservation))=='Conservation'):
        conservation_list.append('Conservation')
        if not country is None:
            country_strip=country.strip()
            time=data_helper.list_to_string(time)
            if (country_strip=="Cameroon"):
                if time=='Current':
                    print("entered current")
                    filtered_list=data_helper.list_filtering(species,species_list)
                    filtered_list=data_helper.list_transformation(filtered_list)
                    print(filtered_list)
                    for i, row in df_CM.iterrows():
                        for j in range(len(filtered_list)):
                            if (row['Species Class'])==(filtered_list[j]):
                                index_list.append(i)
            df_CM_2=df_CM.drop(index_list,axis=0) 
            return df_CM_2.to_dict('records'),df_count_CM.to_dict('records'),conservation_list
    
    elif ((data_helper.list_to_string(conservation))=='Conservation and National Protections and Int Protections (CITES)'):
        conservation_list.append('all')
        return df_CM.to_dict('records'),df_count_CM.to_dict('records'),conservation_list
    else:
        return df_CM.to_dict('records'),df_count_CM.to_dict('records'),conservation_list



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




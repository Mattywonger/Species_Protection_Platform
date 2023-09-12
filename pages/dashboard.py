from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from IPython.display import display
import dash_daq as daq
from pages import data_helper
import design

df=pd.read_csv('Species_count.csv')
df_1=pd.read_csv("Species_master.csv")

df_img=pd.DataFrame( {'Image': ['assets/red_elipse.png', 'assets/orange_elipse.png', 'assets/yellow_elipse.png', 'assets/brightgreen_elipse.png', 'assets/darkgreen_elipse.png','assets/white_elipse.png']})


layout = html.Div(
        style={'display':'flex', 'flexDirection':'column'},
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
                    html.Img(src='assets/Canopy.png',style={'width': '127.164px','height': '42.499px','flex-shrink': 0,'fill': 'rgba(215, 216, 219, 0.80)'})]),
            html.Div(id='country-sentence',style={'display':'flex','width': '1352px','height': '28px','margin-bottom':'46px','margin-top':'49px','margin-left':'46px','font-size':'32px'},children=[]),
            html.Div(
    style={
        'display': 'flex',
        'flexDirection': 'row'
    },
    children=[ #children clause for 3 in total
        html.Div(
        style={'display': 'flex','flexDirection': 'column', 'background-color':'cadetblue','width':'247px','height':'919px','margin-right':'35px','margin-left':'46px'}, #3.1
        children=[ #children clause for 3.1 exclusively
            html.Div(
                style={'display': 'flex','flexDirection': 'row'},
                children=[ 
                    html.Img(src='assets/settings.png',style={'margin-right':'10px'}),
                    html.Div("Controls")]),
            
            html.Div(
                style={'margin-top':'52px','display': 'flex','flexDirection': 'row'},
                children=[
                    html.Img(src='assets/filter.png',style={'margin-right':'11px'}),
                    html.Div("Filters") 
                ]
            ),

            html.Div(
                html.Img(src='assets/Vector_line.png',style={'margin-top':'9.5px'})
            ),
           
            html.Div(
                dcc.Checklist(
                    ['Rainforest Only', 'Endemic Only', 'Exclude Data Deficient'],
                    id='control-dropdown',
                    style={'display':'inline-block','margin-right':'19px'}
                                            )
                    ),
            html.Div(
                style={'display': 'flex','flexDirection': 'row','margin-top':'55px'},
                children=[
                    html.Img(src='assets/calendar.png',style={'margin-right':'9px'}),
                    html.Div("Recency")
                ]
            ),
            html.Div(
                html.Img(src='assets/Vector_line.png',style={'margin-top':'11.5px'})
            ),
            html.Div(
                dcc.Checklist(
                    ['10 >',  '10 <'],
                    id='control-dropdown1',
                    style={'display':'inline-block','margin-right':'19px'}
                            )
            ),

            html.Div(
                style={'display': 'flex','flexDirection': 'column', 'background-color':'white','width':'247px','height':'160px','margin-top':'132px','paddingRight':'28px'},
                children=[
                    html.Div(
                        style={'display': 'flex','flexDirection': 'row'},
                        children=[
                            html.Img(src='assets/printer.png',style={'margin-right':'8px'}),
                            html.Div('PRINT')
                        ]
                    )
                ]
            ) 
        ]
    ),
         html.Div(
            style={  'display': 'flex',
                     'flexDirection': 'column',
                     'background-color':'#D1D2D3'} , #The style for 3.2
            children=[
                html.Div(
                    "GRAPHIC",style={'margin-top':'10px','margin-left':'57px'}
                ),
                html.Div(
                    style={'display': 'flex',
                            'flexDirection': 'row',
                            'width':'610px',
                            'height':'39px',
                            'background-color':'#D1D2D3'
                            },
                    children=[
                        html.Div(
                            style={'margin-left':'78px'},
                            children=[daq.ToggleSwitch(id="my-toggle",value=False)]
                            ),
                        html.Img(src='assets/Vert_vector.png',style={'margin-left':'30px'}),

                        html.Div(
                            style={'margin-left':'85px'},
                            children=[daq.ToggleSwitch(id="abs_rel_toggle",value=False,label='Absolute',labelPosition='right')
                            ]
                        )
                        ]
                        ),
                    
                html.Div( #3.21
                    style={'margin-left': '15px', 'margin-right':'70px','margin-top':'49px','margin-bottom':'47px','border': '0px solid #424953','box-shadow': '0px 4px 4px 0px rgba(0, 0, 0, 0.25) inset'},
                    children=[html.Div(id="dashboard-graph",children=[])]
                    
                        ),
                html.Div(
                    style={'display': 'flex', 'flexDirection': 'column','background-color':'#FFF'},
                    children=[
                                html.Div("NUMERIC DATA"), #3.22A
                                html.Div( #3.22B1
                                    style={'display': 'flex',
                                    'flexDirection': 'row'},
                                    children=[
                                        html.Div(
                                            style={'border-collapse': 'collapse','height':"738px",'width':'353px','paddingRight':'26px','paddingTop':'12px'},
                                            children=[
                                        html.Table([ #image df
                                            html.Tr([
                                                html.Td(html.Img(src='assets/red_elipse.png', style={'width': '16px','height':'16px'}))
                                            ]),
                                            html.Tr([
                                                html.Td(html.Img(src='assets/orange_elipse.png', style={'width': '16px','height':'16px'}))
                                            ]),
                                            html.Tr([
                                                html.Td(html.Img(src='assets/yellow_elipse.png', style={'width': '16px','height':'16px'}))
                                            ]),
                                            html.Tr([
                                                html.Td(html.Img(src='assets/brightgreen_elipse.png', style={'width': '16px','height':'16px'}))
                                            ]),
                                            html.Tr([
                                                html.Td(html.Img(src='assets/darkgreen_elipse.png', style={'width': '16px','height':'16px'}))
                                            ]),
                                            html.Tr([
                                                html.Td(html.Img(src='assets/white_elipse.png', style={'width': '16px','height':'16px'}))
                                            ])
                                                    ])]),  
                                        html.Div( #Actual data df
                                            style={'margin-right':'38px','margin-top':'40px','width':'400px','height':'353px'},
                                            children=html.Div(id='numeric_count',children=[])
                )])
                            ]
                    ),
            ]),
        html.Div(
            html.Img(src='assets/six_buttons_vert.png',style={'margin-left': '14px', 'margin-right':'12px','margin-top':'375px','margin-bottom':'22px', 'flex-shrink': 0}
        )),
        html.Div( #table on the right
            style={},
            children=html.Div(id='matthew',children=[]))
    ]
)

        ])



@callback(
    Output('numeric_count','children'),
    Input('dashboard_tables','data')
)

def numeric_count(data):
    pd_processed=pd.DataFrame(data)
    numeric_df=data_helper.country_indiv_count(pd_processed)

    table=dash_table.DataTable(
                        id='numeric_count',
                        columns=[
                            {"name": 'Amphibian', "id": "Amphibians"},
                            {"name": 'Bird', "id": "Bird"},
                            {"name": 'Mammal', "id": "Mammals"},
                            {"name": 'Reptile', "id": "Reptiles"},
                        ],
                        data=numeric_df.to_dict('records'),
                        )
    return table

@callback(
    Output('dashboard-graph','children'),
    Input('dashboard_tables','data'),
    Input('my-toggle','value')
)


def display_graph(data,toggle):
    if toggle==True:
        print('TRUE TOGGLE')
    else:
        pd_processed=pd.DataFrame(data)
        pd_processed1=data_helper.country_indiv_count(pd_processed)
        pd_processed2=data_helper.transpose(pd_processed1)
        pd_processed2['Category']=['Bird','Amphibians','Reptiles','Mammals']

        fig=px.bar(pd_processed2, x="Category", y=[0,1,2,3,4,5], title="Species-Protection")
        return dcc.Graph(figure=fig,style={'border': '2px solid #424953','box-shadow': '0px 4px 4px 0px rgba(0, 0, 0, 0.25) inset'})


#Same Logic: Get all the inputs in one big callback function and if any of the control functions is clicked, this function will be triggered and a fresh graph will be generated. However, we don't want reloads

@callback(
    Output('matthew','children'),
    [Input('dashboard_tables','data'),Input('control-dropdown','value')]
)

def display_table(data,value):   
    pd_processed=pd.DataFrame(data)
    index_list=[]
    print('before')
    if not (value is None or len(value)==0):
        print('after')
        if value[0]=='Exclude Data Deficient': 
            print("KD IS UGLY")
            for i in pd_processed.index:
                if (pd_processed['Threat Class'][i])=='DD':
                    index_list.append(i)
            pd_processed_new=pd_processed.drop(index_list,axis=0)
            dt=design.table_generation(pd_processed_new)
            return dt
                    
    else:
        dt=design.table_generation(pd_processed)
        return dt
            

   
    
    
@callback(
    Output('country-sentence','children'),
    Input('sentence','data')
)

def display_sentence(data):
    return html.H6('The '+ str(data[0])+' '+str(data[1])+' of all '+str(data[2])+' in '+str(data[3]))






'''
@callback(
    Output('url','href'),
    Input('my-toggle','value')
)
def switch_geography(boolean):
    if boolean==True:
        return 'dashboard-geography'''
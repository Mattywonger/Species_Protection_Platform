from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from IPython.display import display
import dash_daq as daq
from pages import data_helper,design_helper

df=pd.read_csv('Species_count.csv')
df_1=pd.read_csv("Species_master.csv")

df_img=pd.DataFrame( {'Image': ['assets/red_elipse.png', 'assets/orange_elipse.png', 'assets/yellow_elipse.png', 'assets/brightgreen_elipse.png', 'assets/darkgreen_elipse.png','assets/white_elipse.png']})


layout = html.Div(
        style={'display':'flex', 'flexDirection':'column'},
        children=[
            design_helper.top_banner(),
            design_helper.country_sentence(),
            html.Div(
                style={
                    'display': 'flex',
                    'flexDirection': 'row'
        },
                children=[ #children clause for 3 in total
                    design_helper.left_panel(),
                    html.Div(
                         style={ 'display': 'flex',
                                'flexDirection': 'column'},
                        children=[ 
                            design_helper.two_banner(),
                            html.Div(
                                style={'width':'1368px','height':'501px'},
                                children=[html.Div(id="dashboard-graph",children=[])]
                                    ),
                            design_helper.three_banner(),
                            design_helper.complete_table()   
                        ]
                       )
                    

        ])
        ]
)



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






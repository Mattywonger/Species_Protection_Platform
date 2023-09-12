"""from dash import Dash, html, dcc, callback, Output, Input,dash_table,State
import plotly.express as px
import pandas as pd
from pages import page1,geography,dashboard
import dash_bootstrap_components as dbc
from IPython.display import display
from pages import data_helper



app = Dash(__name__, suppress_callback_exceptions=True,assets_folder='assets', external_stylesheets=[dbc.themes.BOOTSTRAP,'typography.css'],use_pages=True)
server = app.server

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

#print(data_helper.transpose(data_helper.country_indiv_count(df_GA)))

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content'),
    dcc.Store(id='storage',data=[],storage_type='memory'),
    dcc.Store(id='sentence',data=[],storage_type='memory'),
    dcc.Store(id='dashboard_tables',data=[],storage_type='memory')
])

layout_home = dbc.Container([ 
    dbc.Row([
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
            ])
            
    ]),
    dbc.Row([ 
        dbc.Col([html.H3('Tell me,')
        ])
]),
    dbc.Row([
        html.Div(
            children=[html.Div('What is the',style={'color': 'var(--text-black, #1A1D21)',
                                                'width':'107px',
                                                'height':'48px','display': 'inline-block','margin-right':'14px'}
                                                ),
                    dcc.Dropdown({f' {i}': f'{i}' for i in ['Current', 'Historic']},
                                    id='time-frame-dropdown',style={"width":"107px","height":"48px",'display': 'inline-block','margin-right':'12px'}),
                    dcc.Dropdown(
        {f' {i}': f'{i}' for i in ['Conservation', 'National Protections', 'International Protections']},
        id='conservation-dropdown',style={"width":"107px","Height":"48px",'display': 'inline-block','margin-right':'20px'}
    ),
    html.Div("of",style={'display':'inline-block','margin-right':'19px'}),
    dcc.Checklist(
    ['amphibians', 'birds', 'mammals','reptiles'],
    ['birds'],
    id='species-dropdown',
    style={'display':'inline-block','margin-right':'19px'}
),
     dcc.Dropdown(options=
        {f' {i}': f'{i}' for i in ['Cameroon','Central African Republic','DRC', 'Gabon', 'Equitorial Guinea','Republic of Congo']},value='country',
        id='country',style={"width":"107px","Height":"48px",'display': 'inline-block'}
    ),
                    ])

                        ]),
    dbc.Row([
        dbc.Col([ dbc.Button('Submit',id='submit-button',href="/dashboard")],width=3)
    ])
])

@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname=='/dashboard':
        return dashboard.layout
    elif pathname=='/dashboard-geography':
        return geography.layout_geography
    else:
        return layout_home


@callback(
   [Output('dashboard_tables','data'),Output('storage','data')],
    Input('country', 'value'))

def display_value(country):
    if not country is None:
        country_strip=country.strip()
        if (country_strip=="Cameroon"):
            print("entered")
            return df_CM.to_dict('records'),df_count_CM.to_dict('records')
        elif (country_strip=="Gabon"):
            print('lebron,')
            return df_GA.to_dict('records'),df_test.to_dict('records')
        elif (country_strip=="Central African Republic") :
            print("yup")
            return df_CF.to_dict('records'),df_count_CM.to_dict('records')
        elif (country_strip=="Equitorial Guinea"):
            return df_GQ.to_dict('records'),df_count_CM.to_dict('records')
        elif (country_strip=="DRC"):
            return df_CD.to_dict('records'),df_count_CM.to_dict('records')
        elif (country_strip=="Republic of Congo"):
            print('congo')
            return df_CG.to_dict('records'),df_count_CM.to_dict('records')
        else:
            print('entered the else statement')
            return df_CD.to_dict('records'),df_count_CM.to_dict('records')
@callback(
    Output('sentence','data'),
    [Input('time-frame-dropdown','value'),Input('conservation-dropdown','value'),Input('species-dropdown','value'),Input('country','value')])

def store_sentence(time,conservation,species,country):
    query_list=[]
    query_list.append(time)
    query_list.append(conservation)
    query_list.append(species)
    query_list.append(country)

    return query_list




if __name__ == '__main__':             
    app.run_server(debug=True)

    """
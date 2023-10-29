import pandas as pd


def rainforest_boolean(dataframe):
    df_rain=pd.read_csv("rainforest.csv")

    for i in dataframe.index:
        for j in df_rain.index:
            if dataframe['taxonid'][i] == df_rain['id'][j]:
                dataframe['rainforest'] = "True"
            else:
                dataframe['rainforest'] = "False"





    
    
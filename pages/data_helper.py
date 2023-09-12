import pandas as pd
from itertools import filterfalse


'''
    for i in master_list[:]:
        for j in list[:]:
            if i==j:

                print('entered')
                master_list.remove(i)'''

def list_filtering(list,master_list):
    for i in reversed(master_list):
        for j in reversed(list):
            if i==j:
                master_list.remove(i)
 
    
    return master_list

def list_transformation(list):
    for i in range(len(list)):
        if list[i]=='Mammals':
            list[i]='MAMMALIA'
        if list[i]=='Birds':
            list[i]='AVES'
        if list[i]=='Amphibians':
            list[i]='AMPHIBIA'
        if list[i]=='Reptiles':
            list[i]='REPTILIA'
    return list

def list_to_string(list,separator='and'):
    string=''
    for i in range(len(list)):
        if i==(len(list)-1):
            string+=list[i]
        else:   
            string+=list[i]
            string+=' ' + separator + ' '
    return string


def country_indiv_count(df):
     LC_bird=VU_bird=EN_bird=CR_bird=NT_bird=DD_bird=0 #bird
     LC_AM=VU_AM=EN_AM= CR_AM=NT_AM=DD_AM=0 #Amphibians
     LC_RT=VU_RT=EN_RT= CR_RT=NT_RT=DD_RT=0 #Reptiles
     LC_MM=VU_MM=EN_MM= CR_MM=NT_MM=DD_MM=0 #Mammals

     for i in df.index:
        if((df['Threat Class'][i]=='LC') and df['Species Class'][i]=='AVES'):
            LC_bird=LC_bird+1
        if ((df['Threat Class'][i]=='LC') and df['Species Class'][i]=='REPTILIA'):
            LC_RT=LC_RT+1
        if ((df['Threat Class'][i]=='LC') and df['Species Class'][i]=='MAMMALIA'):
            LC_MM=LC_MM+1
        if ((df['Threat Class'][i]=='LC') and df['Species Class'][i]=='AMPHIBIA'):
            LC_AM=LC_AM+1
     for j in df.index:
        if((df['Threat Class'][j]=='VU') and df['Species Class'][j]=='AVES'):
            VU_bird=VU_bird+1
        if((df['Threat Class'][j]=='VU') and df['Species Class'][j]=='REPTILIA'):
            VU_RT=VU_RT+1
        if((df['Threat Class'][j]=='VU') and df['Species Class'][j]=='MAMMALIA'):
            VU_MM=VU_MM+1
        if((df['Threat Class'][j]=='VU') and df['Species Class'][j]=='AMPHIBIA'):
            VU_AM=VU_AM+1
        
     for k in df.index:
        if((df['Threat Class'][k]=='EN') and df['Species Class'][k]=='AVES'):
            EN_bird=EN_bird+1
        if((df['Threat Class'][k]=='EN') and df['Species Class'][k]=='REPTILIA'):
            EN_RT=EN_RT+1
        if((df['Threat Class'][k]=='EN') and df['Species Class'][k]=='MAMMALIA'):
            EN_MM=EN_MM+1
        if((df['Threat Class'][k]=='EN') and df['Species Class'][k]=='AMPHIBIA'):
            EN_AM=EN_AM+1
     for l in df.index:
        if((df['Threat Class'][l]=='CR') and df['Species Class'][l]=='AVES'):
             CR_bird= CR_bird+1
        if((df['Threat Class'][l]=='CR') and df['Species Class'][l]=='REPTILIA'):
             CR_RT= CR_RT+1
        if((df['Threat Class'][l]=='CR') and df['Species Class'][l]=='MAMMALIA'):
             CR_MM= CR_MM+1
        if((df['Threat Class'][l]=='CR') and df['Species Class'][l]=='AMPHIBIA'):
             CR_AM= CR_AM+1
     for m in df.index:
        if((df['Threat Class'][m]=='NT') and df['Species Class'][m]=='AVES'):
            NT_bird=NT_bird+1
        if((df['Threat Class'][m]=='NT') and df['Species Class'][m]=='REPTILIA'):
            NT_RT=NT_RT+1
        if((df['Threat Class'][m]=='NT') and df['Species Class'][m]=='MAMMALIA'):
            NT_MM=NT_MM+1
        if((df['Threat Class'][m]=='NT') and df['Species Class'][m]=='AMPHIBIA'):
            NT_AM=NT_AM+1
     for n in df.index:
        if((df['Threat Class'][n]=='DD') and df['Species Class'][n]=='AVES'):
            DD_bird=DD_bird+1
        if((df['Threat Class'][n]=='DD') and df['Species Class'][n]=='REPTILIA'):
            DD_RT=DD_RT+1
        if((df['Threat Class'][n]=='DD') and df['Species Class'][n]=='MAMMALIA'):
            DD_MM=DD_MM+1
        if((df['Threat Class'][n]=='DD') and df['Species Class'][n]=='AMPHIBIA'):
            DD_AM=DD_AM+1
    
     data={
        'Bird':[LC_bird,VU_bird,EN_bird, CR_bird,NT_bird,DD_bird],
        'Amphibians':[LC_AM,VU_AM,EN_AM,CR_AM,NT_AM,DD_AM],
        'Reptiles':[LC_RT,VU_RT,EN_RT,CR_RT,NT_RT,DD_RT],
        'Mammals':[LC_MM,VU_MM,EN_MM,CR_MM,NT_MM,DD_MM]
     }

     df_numeric=pd.DataFrame(data)

     return df_numeric


def transpose(dataframe):
   dataframe=dataframe.transpose()
   return dataframe
    #dataframe.to_csv('country.csv',index=False)

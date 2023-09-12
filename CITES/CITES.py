import requests
import json
import csv
import fnmatch
import os
import string

import pandas as pd
from functools import reduce

#THESE FUNCTIONS ARE API CALLS -----------------------------------------

def CITES_PULL(STEM, TOKEN, COUNTRIES):
    """TAKES STEM, TOKEN, COUNTRIES LIST AND MAKES SPECIES-BY-COUNTRY JSON, CSV FILES"""
    
    headers = {
    'X-Authentication-Token': 'jYoZy6SdTPuNYp0PaQTMuwtt'
}
  
    filename = 'CITES'
    request = requests.get(STEM + 'taxon_concepts',headers=headers)
    writeJSONFile(filename, request.json())
    print("Function activated")
    print(request.status_code)



#THESE FUNCTIONS ARE UTILITIES -------------------------------------------

def writeJSONFile(filename, response):
    """GENERIC CODE TO WRITE JSON FILE FROM 'response' TO 'data' FOLDER"""
    with open('data_CITES/' + filename + '.json', 'w') as f:
        try:
            json.dump(response, f, ensure_ascii=False, indent=4)
            f.close()
            print('Made', filename + '.json')

        except json.JSONDecodeError as e:
            print("JSON DECODING ERROR:", e)




#THIS IS THE MAIN FUNCTION ---------------------------------------------

def main():
    #CONSTANTS------------------------------------
    STEM = 'https://api.speciesplus.net/api/v1/'

    COUNTRIES = ['CD', 'CG', 'GA', 'CM', 'CF', 'GQ']

    with open('CITES_token.txt', 'r') as t:
        TOKEN = t.read()
        t.close()

    #create 'data' folder
    if not os.path.isdir('data_CITES'):
        os.mkdir('data_CITES')

    print()

    #1) (API) GET ALL SPECIES FOR A LIST OF COUNTRIES
    CITES_PULL(STEM, TOKEN, COUNTRIES)


    #4) (API) GET COUNTRY OF OCCURRENCE FOR ALL UNIQUE SPECIES
    #   THIS API CALL TAKES ~90 MINUTES FOR 8749 SPECIES
    # getCtryOccur(STEM, TOKEN)

    #5) (API) GET HISTORICAL CATEGORIES FOR ALL UNIQUE SPECIES
    #   THIS API CALL TAKES ~60 MINUTES FOR 8749 SPECIES
    # getHistCats(STEM, TOKEN)

    #6) (API) GET THREATS FOR ALL UNIQUE SPECIES
    #   THIS API CALL TAKES ~7 HOURS AND 35 MINUTES FOR 8749 SPECIES
    # getThreats(STEM, TOKEN)

    #7) (API) GET HABITATS FOR ALL UNIQUE SPECIES
    #   THIS API CALL TAKE ~5 HOURS AND 10 MINUTES FOR 8749 SPECIES
    # getHabitats(STEM, TOKEN)

    #8) (API) GET COMMON NAMES FOR ALL UNIQUE SPECIES
    #   THIS API CALL TAKE ~4 HOURS FOR 8749 SPECIES
    # getCommonNames(STEM, TOKEN)


main()
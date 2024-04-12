import pandas as pd
from tools import *

def get_data_db(table:str):
    
    # Connexion à la base de données.
    config_azure = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config_azure)
    
    # Récupération des données.
    query = f"SELECT * FROM {table};"
    data = pd.read_sql(query, engine_azure) 
    engine_azure.close()
    return data
    
    

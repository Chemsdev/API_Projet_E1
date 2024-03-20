import pandas as pd
from tools import *

def get_data_db():
    
    # Connexion à la base de données.
    config_azure = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config_azure)
    
    # Récupération des données.
    query = f"SELECT * FROM raw_data;"
    raw_data = pd.read_sql(query, engine_azure) 
    
    engine_azure.close()
    return raw_data
    
    

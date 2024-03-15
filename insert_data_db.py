from options import *
from tools   import *


# Fonction permettent d'insérer les données saisit dans la table raw_data.
def send_new_data(features:list, new_data=columns_new_data):
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    data = {}
    for column, feature in zip(new_data, features):
        data[column] = feature
    data = pd.DataFrame([data])
    data.to_sql("new_data", index=False, con=engine_azure, if_exists="append")
    engine_azure.close()



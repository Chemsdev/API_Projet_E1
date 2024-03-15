from tools          import *
from options        import *
from sqlalchemy.sql import text


# Fonction permettent d'enregistrer la prédiction.
def save_prediction(prediction):
    
    # connexion à la base de données 
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)

    # Exécution de la requête SQL pour récupérer le dernier ID
    sql_query = text("SELECT MAX(id_new_data) FROM new_data")
    result = engine_azure.execute(sql_query)
    
    # Récupération de l'id
    dernier_id = result.fetchall()[0][0]
    
    # Décodage de la prédiction.
    if 1 in prediction:
        prediction = "Oui"
    else:
        prediction = "Non"
        
    # préparation des données
    data  = {"id_new_data":dernier_id, "prediction":prediction}
    data = pd.DataFrame(data, index=[0])    
    
    # Insertion des données
    data.to_sql("prediction", index=False, con=engine_azure, if_exists="append")
    engine_azure.close()
    

# Fonction permettent d'exécuter le modèle.
def execute_model(data_preprocess, model_pickle):
    
    # Préparation de X pour le modèle.
    X = {new_key: data_preprocess[old_key] for old_key, new_key in zip(data_preprocess.keys(), columns_for_model)}
    X_new = pd.DataFrame([X])
    
    # Exécution du modèle.
    prediction = model_pickle.predict(X_new) 
    
    # Enregistrement des données.
    save_prediction(prediction=prediction)
    
    return prediction
    
    

    

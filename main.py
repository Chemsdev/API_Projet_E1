# FastAPI
from   fastapi import FastAPI, HTTPException
from   fastapi import FastAPI

# Others
from dotenv         import load_dotenv
from features       import *
from tools          import *
import os
import pickle

# CODE END-POINTS
from db_init         import *
from preprocessing   import *
from insert_data_db  import *
from model           import *
from get_data_db     import *


# ==================================================>

# Authentification API.
def Authentification(api_key:str):
    load_dotenv()
    password_api = os.environ.get("API_PASSWORD")
    if api_key == password_api:
        return True
    return False

# ==================================================>

# Ouverture du modèle en pickle
with open("logistic_regression.pickle", 'rb') as file:
    model_pickle = pickle.load(file)

# ==================================================>



app = FastAPI()

# =========================================================================================>

@app.post("/database_init")
async def init(api_key:str):
        
    # Authentification API.
    if not Authentification(api_key=api_key):
        raise HTTPException(status_code=401, detail="Unauthorized")    
    
    # Création des tables si elles n'existent pas.
    if check_if_tables_is_empty(table="raw_data"):
        
        # Insertion des données raw.
        insert_raw_data()
    
    return "Initialisation succès !"

# =========================================================================================>

@app.post("/insert_data_db")
async def insert_data_db(api_key:str, data:dict):
    
    # Authentification API.
    if not Authentification(api_key=api_key):
        raise HTTPException(status_code=401, detail="Unauthorized")    
    
    # Insertion des données.
    data = list(data.values())
    send_new_data(
        features=data, 
        new_data=columns_new_data
    )

    return "Données insérées succès !"

# =========================================================================================>

@app.post("/preprocess")
async def preprocess(api_key:str, data:dict):
    
    # Authentification API.
    if not Authentification(api_key=api_key):
        raise HTTPException(status_code=401, detail="Unauthorized")    
    
    # Preprocessing des données.
    data = [i for i in data.values()]
    data_preprocess=preprocessing(data)
    
    return data_preprocess

# =========================================================================================>

@app.post("/modeling")
async def modeling(api_key:str, data_preprocess:dict):
    
    # Authentification API.
    if not Authentification(api_key=api_key):
        raise HTTPException(status_code=401, detail="Unauthorized")   
    
    # Réalisation des prédictions.
    prediction = execute_model(data_preprocess, model_pickle=model_pickle)
    return {"prediction": prediction.tolist()}

# =========================================================================================>

@app.get("/get_data")
async def get_data(api_key:str):
    
    # Authentification API.
    if not Authentification(api_key=api_key):
        raise HTTPException(status_code=401, detail="Unauthorized") 
    
    # Récupération des données.
    raw_data = get_data_db()
    raw_data = raw_data.to_dict()
    return raw_data 


















    
    # # simulation d'entrer utilisateur.
    # data = [
    #     "Homme",
    #     "Urban",
    #     "Oui",
    #     "Kenya",
    #     "Marié(e)/Vie en couple",
    #     "Travailleur indépendant",
    #     "Conjoint(e)",
    #     "2016",
    #     1,
    #     1,
    #     "Autre/Ne sais pas/Refuse de répondre",
    # ]

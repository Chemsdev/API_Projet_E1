# SQL ALCHEMY
from sqlalchemy import create_engine

# Autres
import os
from dotenv import load_dotenv
import pandas as pd


# AZURE_TRANSDEV.
AZURE_INCLUSION=[
    "DB_HOST",
    "DB_USERNAME",
    "DB_PASSWORD",
    "DB_DATABASE"
]

# ====================================================>

# Fonction configuration ENV.
def set_confg(liste_connexion:list):
    load_dotenv()
    host     = os.environ.get(liste_connexion[0])
    user     = os.environ.get(liste_connexion[1])
    password = os.environ.get(liste_connexion[2])
    database = os.environ.get(liste_connexion[3])
    config = {
        "host"     : host,
        "user"     : user,
        "password" : password,
        "database" : database,
    }  
    
    return config

# ====================================================>

# Fonction connexion SQL.
def connect_mysql(config:dict):
    host     = config.get('host','')
    user     = config.get('user','')
    password = config.get('password','')
    database = config.get('database','')
    engine   = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine.connect()

# ====================================================>

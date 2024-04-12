from tools import *


# table raw_data
raw_data = """
    CREATE TABLE IF NOT EXISTS raw_data (
        id_raw INT AUTO_INCREMENT PRIMARY KEY,
        compte_bancaire VARCHAR(10),
        pays VARCHAR(50),
        annee INT,
        type_de_localisation VARCHAR(50),
        acces_au_telephone VARCHAR(10),
        taille_du_menage INT,
        age INT,
        sexe VARCHAR(10),
        relation_avec_le_chef_de_famille VARCHAR(50),
        etat_civil VARCHAR(50),
        niveau_education VARCHAR(50),
        type_de_job VARCHAR(50)
    )
"""

# table new_data
new_data = """
    CREATE TABLE IF NOT EXISTS new_data (
        id_new_data INT AUTO_INCREMENT PRIMARY KEY,
        sexe VARCHAR(10),
        type_de_localisation VARCHAR(50),
        acces_au_telephone VARCHAR(10),
        pays VARCHAR(50),
        etat_civil VARCHAR(50),
        type_de_job VARCHAR(50),
        relation_avec_le_chef_de_famille VARCHAR(50),
        annee INT,
        taille_du_menage INT,
        age INT,
        niveau_education VARCHAR(50)
    )
"""

# Table prediction
prediction = """
    CREATE TABLE IF NOT EXISTS prediction (
        id_pred INT AUTO_INCREMENT PRIMARY KEY,
        id_new_data INT,
        prediction VARCHAR(50),
        FOREIGN KEY (id_new_data) REFERENCES new_data(id_new_data)
    )
"""

# Table performance
performance = """
    CREATE TABLE IF NOT EXISTS performance (
        id_performance INT AUTO_INCREMENT PRIMARY KEY,
        Model VARCHAR(50),
        Classe VARCHAR(50),
        `precision` FLOAT,
        recall FLOAT,
        f1score FLOAT,
        support FLOAT
    )
"""

# ===================================================================================================>

# Fonction permettent de créer une table
def create_table(query_table:str):
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    with engine_azure.connect() as connection:
        connection.execute(query_table)
    engine_azure.close()

# ===================================================================================================>

# Fonction permettent de créer la base de données. 
def create_database_init():
    tables = [raw_data, new_data, prediction, performance]
    for i in tables:
        create_table(i)

# ===================================================================================================>

# Fonction permettent de vérifier si la table raw_data ou new_data existe.
def check_if_tables_is_empty(table:str):

    # Connexion à la base de données.
    config_azure = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config_azure)
    
    # On vérifie si la table raw_data est vide.
    query = f"SELECT count(*) FROM {table}"
    exe = engine_azure.execute(query) 
    row_count = exe.scalar()
    engine_azure.close()
    
    # Si la table est vide : True, sinon False.
    if row_count == 0:
        return True
    return False

# ===================================================================================================>

# Fonction permettent d'insérer les données initiales dans la base de données.
def insert_raw_data():
    
    # Connexion à la base de données.
    config_azure = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config_azure)
    
    # Traduction des colonnes.
    raw_data = pd.read_csv("data.csv")
    raw_data = raw_data.rename(columns={
        'country': 'pays',
        'year': 'annee',
        'bank_account':'compte_bancaire',
        'location_type': 'type_de_localisation', 
        'cellphone_access': 'acces_au_telephone', 
        'household_size': 'taille_du_menage', 
        'age_of_respondent': 'age',
        'gender_of_respondent': 'sexe',
        'relationship_with_head':'relation_avec_le_chef_de_famille',
        'marital_status':'etat_civil', 
        'education_level':'niveau_education',
        'job_type':'type_de_job', 
    })
    raw_data.drop("uniqueid", axis=1, inplace=True)
    raw_data.to_sql("raw_data", index=False, con=engine_azure, if_exists="append")
    engine_azure.close()
    
# =================================================================================>

# Fonction permettent d'insérer les performances dans la table performance
def insert_performance():
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    scoring_2016 = {
        "model" : "2016",
        "classe": [0.0, 1.0],
        "precision": [0.95, 0.27],
        "recall": [0.75, 0.70],
        "f1score": [0.84, 0.39],
        "support": [1543, 204]
    }
    scoring_2016_2017 = {
        "model" : "2016-2017",
        "classe": [0.0, 1.0],
        "precision": [0.96, 0.27],
        "recall": [0.76, 0.75],
        "f1score": [0.85, 0.40],
        "support": [2743, 328]
    }
    scoring_2016_2017_2018 = {
        "model" : "2016-2017-2018",
        "classe": [0.0, 1.0],
        "precision": [0.94, 0.38],
        "recall": [0.79, 0.73],
        "f1score": [0.86, 0.50],
        "support": [4005, 700]
    }
    # Conversion les dictionnaires en DataFrames
    df_2016           = pd.DataFrame(scoring_2016)
    df_2016_2017      = pd.DataFrame(scoring_2016_2017)
    df_2016_2017_2018 = pd.DataFrame(scoring_2016_2017_2018)
    # Concaténation des DataFrames
    scoring_data = pd.concat([df_2016, df_2016_2017, df_2016_2017_2018], ignore_index=True)
    scoring_data.to_sql("performance", index=False, con=engine_azure, if_exists="append")
    engine_azure.close()


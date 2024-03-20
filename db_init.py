from tools import *




# ===================================================================================================>

# Création de la table raw_data.
def create_table_raw_data():
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    with engine_azure.connect() as connection:
        connection.execute("""
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
        """)
    engine_azure.close()
    # print('Table raw_data créée avec succès !')
    
# ===================================================================================================>

# Création de la table new_data.
def create_table_new_data():
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    with engine_azure.connect() as connection:
        connection.execute("""
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
        """)
    engine_azure.close()
    # print('Table new_data créée avec succès !')

# ===================================================================================================>

# Fonction permettant de créer la table prédiction.
def create_table_prediction():
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    with engine_azure.connect() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS prediction (
                id_pred INT AUTO_INCREMENT PRIMARY KEY,
                id_new_data INT,
                prediction VARCHAR(50),
                FOREIGN KEY (id_new_data) REFERENCES new_data(id_new_data)
            )
        """)
    engine_azure.close()
    # print('Table raw_data créée avec succès !')
    
# ===================================================================================================>


# Fonction permettent de vérifier si la table raw_data ou new_data existe.
def check_if_tables_is_empty(table:str):

    # Connexion à la base de données.
    config_azure = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config_azure)
    
    # On créer les tables si elles n'existent pas.
    create_table_raw_data()
    create_table_new_data()
    create_table_prediction()

    # On vérifie si la table est vide.
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




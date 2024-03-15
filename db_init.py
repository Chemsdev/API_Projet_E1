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
    print('Table raw_data créée avec succès !')
    
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
    print('Table new_data créée avec succès !')

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
    print('Table raw_data créée avec succès !')
    
# ===================================================================================================>





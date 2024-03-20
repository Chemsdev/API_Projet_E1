from   options   import *
from   tools     import *

# ============================================================================================================================================>

# Fonction permettent d'encoder des colonnes (0 ou 1)
def label_encoding(columns:list, values:list):
    data={
        columns[0]:0.0,
        columns[1]:0.0
    }
    if values[0] == "Rural":
        data[columns[0]] = 1.0
        
    if values[1] == "Oui":
        data[columns[1]] = 1.0
    return data

# ============================================================================================================================================>

# Fonction permettent de catégoriser un age.
def group_age(age):
    if age >= 10 and age < 20:
        return "Group_Age_10_20"
    elif age >= 20 and age < 30:
        return "Group_Age_20_30"
    elif age >= 30 and age < 40:
        return "Group_Age_30_40"
    elif age >= 40 and age < 50:
        return "Group_Age_40_50"
    elif age >= 50 and age < 60:
        return "Group_Age_50_60"
    elif age >= 60 and age < 70:
        return "Group_Age_60_70"
    elif age >= 70 and age < 80:
        return "Group_Age_70_80"
    else:
        return "Group_Age_80"

# ============================================================================================================================================>

# Fonction permettent d'encoder des features.
def one_hot_encoding_other_features(value:str, columns_table, inputs):

    # Récupération du numéro d'index de la liste.
    index = inputs.index(value)

    # Insertion de 1 au bon champs
    columns_table = columns_table.copy()
    columns_table[list(columns_table.keys())[index]] = 1.0
    return columns_table

# ============================================================================================================================================>

# Fonction permettent de concaténer tous les dictionnaires contenant les features encoders.
def prepare_data_preprocess(list_encodings):
    
    # Concaténation de tous les dictionnaires
    data_preprocess = {}
    for i in list_encodings:
        data_preprocess.update(i)
    return data_preprocess

# ============================================================================================================================================>

# Fonction permettent d'encoder par importance la feature niveau_education
def order_niveau_education(value, inputs):
    if value == inputs[0]:
        return 0.0
    if value == inputs[1]:
        return 1.0
    if value == inputs[2]:
        return 2.0
    if value == inputs[3]:
        return 3.0 
    if value == inputs[4]:
        return 4.0 
    if value == inputs[5]:
        return 5.0 

# ============================================================================================================================================>

# Fonction permettent de preprocess les données (encodage.)
def preprocessing(features:list):
    
    # Supression de la feature "sexe".
    del features[0]
    
    # Calcul de la catégorie d'age
    cat_age = group_age(age=features[8])
        
    # One Hot Encoding/Ordinal Encoding/Label Encoding.
    encode_access_loc       = label_encoding(columns=["type_de_localisation", "acces_au_telephone"], values=[features[0], features[1]])
    encode_pays             = one_hot_encoding_other_features(value=features[2], inputs=values_pays,             columns_table=columns_pays)
    encode_group_age        = one_hot_encoding_other_features(value=cat_age,     inputs=values_group_age,        columns_table=columns_group_age)
    encode_etat_civil       = one_hot_encoding_other_features(value=features[3], inputs=values_etat_civil,       columns_table=columns_etat_civil)
    encode_type_job         = one_hot_encoding_other_features(value=features[4], inputs=values_type_job,         columns_table=columns_type_de_job)
    encode_relation_famille = one_hot_encoding_other_features(value=features[5], inputs=values_relation_famille, columns_table=columns_relation_chef_famille)
    encode_annee            = one_hot_encoding_other_features(value=features[6], inputs=values_annee,            columns_table=columns_annee)
    taille_du_menage        = {"taille_du_menage"         :features[7]}
    age                     = {"age"                      :features[8]}
    niveau_education_encode = {"niveau_education_encode"  :order_niveau_education(value=features[-1], inputs=values_niveau_education)}
    
    # Concaténation de tous les dictionnaires.
    list_encodings = [
        encode_access_loc, 
        encode_pays, 
        encode_group_age, 
        encode_etat_civil, 
        encode_type_job, 
        encode_relation_famille, 
        encode_annee,
        taille_du_menage,
        age,
        niveau_education_encode
    ]
    
    
    # for i in list_encodings:
    #     print(i)
        
        
    data_preprocess = prepare_data_preprocess(list_encodings=list_encodings)
    
    
    print("here:")
    for key, value in data_preprocess.items():
        print(f"Clé : {key}, Valeur : {value}")

    return data_preprocess
# ============================================================================================================================================>


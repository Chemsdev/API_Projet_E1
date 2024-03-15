import pickle

# Ouverture du modèle en pickle
with open("logistic_regression.pickle", 'rb') as file:
    loaded_model = pickle.load(file)

# Fonction permettent d'éxécuter le modèle
def model(X_new, model_pickle=loaded_model):
    predictions = model_pickle.predict(X_new)
    return predictions
    

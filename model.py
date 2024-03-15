import pickle



# Fonction permettent d'éxécuter le modèle
def model(X_new):
    
    # Ouverture du modèle en pickle
    with open("logistic_regression.pickle", 'rb') as file:
        model_pickle = pickle.load(file)
    
    # Prédicictons...
    predictions = model_pickle.predict(X_new)
    return predictions
    

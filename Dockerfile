# On utilise l'image de base Python
FROM python:3.8-slim-buster

# On spécifie le chemin ou on souhaite copier l'app dans le conteneur.
WORKDIR /app

# Exécution du fichier requirements pour installer tous les dépendances nécéssaire.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le fichier principale d'éxecution du streamlit dans le conteneur.
COPY main.py      .
COPY db_init.py   .
COPY tools.py     .
COPY data.csv     .
COPY features.py  .
COPY options.py   .
COPY model.py     .

# Les fichiers pythons pour les end-points.
COPY database_init.py  .
COPY preprocessing.py  .
COPY insert_data_db.py .

# Copie du modèle pickle.
COPY logistic_regression.pickle .

# COPY .env .

# On spécifie le port.
EXPOSE 8501

# On spécifie la commande à saisir pour exécuter l'app.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


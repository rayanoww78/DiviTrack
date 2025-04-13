# Ce fichier contiendra les fonctions pour interagir avec l'API Budget Insight

import requests

def get_access_token(client_id, client_secret):
    url = "https://api.budget-insight.com/api/v2/auth/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=data)
    return response.json()["access_token"]

# Ajoute ici les autres fonctions : create_user, get_transactions, etc.

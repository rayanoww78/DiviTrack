import requests

BASE_URL = "https://api.budget-insight.com/api/v2"

def get_access_token(client_id, client_secret):
    url = f"{BASE_URL}/auth/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def create_user(access_token):
    url = f"{BASE_URL}/users"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    return response.json()["uuid"]

def get_transactions(user_id, access_token):
    url = f"{BASE_URL}/users/{user_id}/transactions"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def filter_dividends(transactions):
    # Filtre les transactions qui contiennent le mot "dividende" dans le libellé
    return [
        {
            "date": t["date"],
            "label": t["label"],
            "amount": t["value"],
            "currency": t["currency_code"]
        }
        for t in transactions
        if "dividende" in t["label"].lower()
    ]

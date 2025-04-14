
from flask import Flask, redirect, request, session, jsonify, render_template
import requests
import yfinance as yf
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecret")

# === Configuration Powens Sandbox ===
CLIENT_ID = os.getenv("POWENS_CLIENT_ID", "63386072")
CLIENT_SECRET = os.getenv("POWENS_CLIENT_SECRET", "VJdoBxPV0I4o091JChHOlJHY3Nkk1Vso")
BASE_URL = "https://demo.biapi.pro/2.0"

# Exemple ISIN -> ticker (à compléter)
isin_to_ticker = {
    "FR0000120271": "OR.PA",   # L'Oréal
    "US0378331005": "AAPL",    # Apple
    "FR0000131104": "BNP.PA",  # BNP Paribas
}

@app.route("/")
def accueil():
    return '''
        <h2>DiviTrack - Connexion bancaire</h2>
        <a href="https://webview.powens.com/connect?domain=rayanoww-sandbox.biapi.pro&client_id=63386072&redirect_uri=https://divitrack.onrender.com/&max_connections=5" target="_blank">
            🔐 Se connecter à ma banque
        </a>
    '''

@app.route("/redirect")  # Redirection après la Webview
def redirect_from_webview():
    token = request.args.get("access_token")
    if not token:
        return "❌ Token manquant dans l'URL", 400

    session["access_token"] = token
    return redirect("/analyse")

@app.route("/analyse")
def analyse_portefeuille():
    access_token = session.get("access_token")
    if not access_token:
        return "❌ Aucune session utilisateur active", 403

    try:
        headers = {"Authorization": f"Bearer {access_token}"}
        res = requests.get(f"{BASE_URL}/portfolios/positions", headers=headers)
        positions = res.json().get("positions", [])

        enriched = []
        for position in positions:
            isin = position.get("isin")
            quantity = position.get("quantity")
            name = position.get("label", "Inconnu")

            ticker = isin_to_ticker.get(isin)
            if not ticker or not quantity:
                continue

            stock = yf.Ticker(ticker)
            info = stock.info
            eps = info.get("forwardEps")
            dividend = info.get("dividendRate")

            enriched.append({
                "entreprise": name,
                "ticker": ticker,
                "quantite": quantity,
                "eps_estime_par_action": eps,
                "eps_total": round(eps * quantity, 2) if eps else None,
                "dividende_estime_par_action": dividend,
                "dividende_total": round(dividend * quantity, 2) if dividend else None
            })

        return render_template("mon_portfolio.html", portefeuille=enriched)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

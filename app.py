import os

from flask import Flask, jsonify, render_template, request
import yfinance as yf

app = Flask(__name__)

# dictionnaire pour faire correspondre les noms aux tickers
nom_vers_ticker = {
    "l'oréal": "OR.PA", "air liquide": "AI.PA", "lvmh": "MC.PA", "sanofi": "SAN.PA", "danone": "BN.PA",
    "bnp paribas": "BNP.PA", "schneider electric": "SU.PA", "société générale": "GLE.PA", "veolia": "VIE.PA",
    "vinci": "DG.PA", "michelin": "ML.PA", "hermès": "RMS.PA", "pernod ricard": "RI.PA", "engie": "ENGI.PA",
    "carrefour": "CA.PA", "crédit agricole": "ACA.PA", "bouygues": "EN.PA", "stmicroelectronics": "STM.PA",
    "capgemini": "CAP.PA", "total": "TTE", "stellantis": "STLA.PA", "legrand": "LR.PA", "airbus": "AIR.PA",
    "arcelormittal": "MT.AS", "edf": "EDF.PA", "thales": "HO.PA", "kering": "KER.PA", "safran": "SAF.PA",
    "vivendi": "VIV.PA", "worldline": "WLN.PA", "orange": "ORA.PA", "publicis": "PUB.PA", "unibail-rodamco": "URW.AS",
    "alstom": "ALO.PA", "atos": "ATO.PA", "valeo": "FR.PA", "renault": "RNO.PA",
    "apple": "AAPL", "microsoft": "MSFT", "google": "GOOGL", "alphabet": "GOOGL", "amazon": "AMZN",
    "meta": "META", "facebook": "META", "tesla": "TSLA", "nvidia": "NVDA", "berkshire hathaway": "BRK-B",
    "jpmorgan": "JPM", "johnson & johnson": "JNJ", "visa": "V", "mastercard": "MA", "procter & gamble": "PG",
    "home depot": "HD", "disney": "DIS", "exxonmobil": "XOM", "pfizer": "PFE", "coca-cola": "KO", "pepsico": "PEP",
    "intel": "INTC", "netflix": "NFLX", "adobe": "ADBE", "oracle": "ORCL", "qualcomm": "QCOM",
    "ibm": "IBM", "salesforce": "CRM", "boeing": "BA", "mcdonald's": "MCD", "walmart": "WMT",
    "chevron": "CVX", "cisco": "CSCO", "abbvie": "ABBV", "costco": "COST", "goldman sachs": "GS",
    "3m": "MMM", "paypal": "PYPL", "starbucks": "SBUX", "ford": "F", "general motors": "GM", "Klépierre" : "LI.PA", "Axa" : "CS.PA","Veralia" : "VRLA.PA"
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/forecast-live')
def forecast_live():
    nom = request.args.get("entreprise", "").strip().lower()

    ticker = nom_vers_ticker.get(nom)
    if not ticker:
        return jsonify({"error": "Entreprise inconnue"}), 404

    stock = yf.Ticker(ticker)
    info = stock.info

    eps = info.get("forwardEps")
    dpa = info.get("dividendRate")

    return jsonify({
        "entreprise": nom.title(),
        "ticker": ticker,
        "annee": 2025,
        "eps_estime": f"{eps:.2f} $" if eps else "Non disponible",
        "dividende_estime": f"{dpa:.2f} $" if dpa else "Non disponible"
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render fournit un PORT dans ses variables d'environnement
    app.run(host='0.0.0.0', port=port)


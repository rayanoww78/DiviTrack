import requests


def get_divi(ticker):
    url = f"https://finnhub.io/api/v1/stock/metric?symbol={ticker}&metric=all&token=cvtto79r01qjg1369uggcvtto79r01qjg1369uh0"
    r = requests.get(url)
    data = r.json()

    # Extraire uniquement ce qui t'intéresse (exemple)
    return {"ticker": ticker,"eps_2025": data["metric"].get("epsForward"),"dividend_2025": data["metric"].get("dividendPerShareForward")}

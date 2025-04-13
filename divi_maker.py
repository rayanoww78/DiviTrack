import yfinance as yf

def get_yahoo_forecast(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    eps_estimate = info.get("forwardEps")
    dividend_estimate = info.get("dividendRate")

    return {
        "ticker": ticker,
        "eps_2025": eps_estimate,
        "dividend_2025": dividend_estimate
    }

# Exemples d'utilisation
tickers = ["TTE", "AAPL", "MSFT", "DG.PA", "AI.PA"]  # TotalEnergies, Apple, Microsoft, Vinci, Air Liquide

for t in tickers:
    data = get_yahoo_forecast(t)
    print(data)

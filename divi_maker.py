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


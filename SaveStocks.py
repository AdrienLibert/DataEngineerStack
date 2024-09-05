import yfinance as yf
import pandas as pd

tickers = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "TSLA", "BRK-B", "NVDA", "TSM", "V", 
    "JNJ", "WMT", "META", "PG", "UNH", "LVMUY", "MA", "XOM", "HD", "CVX",
    "BABA", "LLY", "KO", "MRK", "PEP", "ABBV", "NVO", "ASML", "AZN", "SHEL", 
    "COST", "ORCL", "MCD", "AVGO", "ADBE", "CSCO", "NKE", "ACN", "TM", 
    "TMUS", "NEE", "TXN", "SAP", "UL", "LIN", "DHR", "NFLX", "ABT", "AMD",
    "PFE", "DIS", "UPS", "PM", "TMO", "BHP", "MS", "BMY", "UNP", "RTX", 
    "SCHW", "VZ", "HON", "AMT", "RY", "AMGN", "BAC", "INTC", "GS", 
    "HSBC", "WFC", "QCOM", "SBUX", "COP", "EL", "CAT", "BLK", "BDX",
    "CVS", "AXP", "SPGI", "IBM", "DE", "C", "ISRG", "NOW", "MDT",
    "ADP", "TTE", "LOW", "T", "ZTS", "GILD", "SONY", "MO", "PLD", 
    "CSX", "MMC", "TJX", "MUFG", "BP", "GE", "BA"
]

# Créer un DataFrame pour stocker les données
data = []

# Récupérer la capitalisation boursière pour chaque ticker
for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info
    
    if "marketCap" in info:
        data.append({
            "Ticker": ticker,
            "Name": info.get("longName", ""),
            "Market Cap": info["marketCap"],
            "Revenue": info.get("totalRevenue", "N/A"),
            "Country": info.get("country", "N/A"),
            "Sector": info.get("sector", "N/A")
        })


# Convertir en DataFrame
df = pd.DataFrame(data)

# Trier par capitalisation boursière décroissante
df_sorted = df.sort_values(by="Market Cap", ascending=False)

# Sélectionner les 1000 plus grandes
top_1000 = df_sorted.head(1000)

# Afficher les 1000 premières entreprises
print(top_1000)

# Sauvegarder dans un fichier CSV si besoin
top_1000.to_csv("stocks.csv", index=False)


import yfinance as yf
import pandas as pd

data = pd.DataFrame(
    {"Category": ["LG", "LV", "MG", "MV", "SG", "SV", "Intl" , "EM", "Core Bond" "Non-Core Bond", "Alt 1"]
     "Fund": ["MFEIX" , "GCVTX", "JEMWX", "MCVCX", "NEJYX", "FCGIX", "GSINX", "FKMKX", "PTTPX", "IISIX", "MLPOX"]})

sleeves = {"US Equity": ["LG", "LV", "MG", "MV", "SG", "SV"],
           "Intl Equity": ["Intl", "EM"],
           "Fixed Income": ["Core Bond", "Non-Core Bond"],
           "Alternatives": ["Alt 1"]}

data["Sleeves"] = data["Category".map(
    lambda x: next((sleeve for sleeve, categories in sleeves.items() if x in categories), None))]

def generate_portfolio(data, stock_bond_mix):
    stock_mix, bond_mix = stock_bond_mix
    data["Allocation"] = 0.0

    stock_allocation = stock_mix / 100
    bond_allocation = bond_mix / 100

    for sleeve, allo


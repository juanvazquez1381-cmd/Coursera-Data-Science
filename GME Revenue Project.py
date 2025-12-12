import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf


gme_data = yf.Ticker("GME")
gme_data = gme_data.history(period = 'max') 
gme_data = pd.DataFrame(data = gme_data)
gme_data.reset_index(inplace= True)

link = ' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

fill = []

html_data = requests.get(link).text
soup = BeautifulSoup(html_data, 'html.parser')

for row in soup.find_all('tbody')[1].find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 1:
        date = cols[0].text
        revenue = cols[1].text

    fill.append({'Date': date, 'Revenue': revenue})


gme_revenue = pd.DataFrame(fill)


gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r',|\$', "", regex=True)

gme_revenue.dropna(inplace=True)

gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

print(gme_revenue)

import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

make_graph(gme_data, gme_revenue, 'GameStop')

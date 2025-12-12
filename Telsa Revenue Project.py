import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf


tesla_data = yf.Ticker("TSLA")
tesla_data = tesla_data.history(period = 'max') 
tesla_data = pd.DataFrame(data = tesla_data)
tesla_data.reset_index(inplace= True)


link = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
fill = []

html_data = requests.get(link).text
soup = BeautifulSoup(html_data, 'html.parser')

for row in soup.find_all('tbody')[1].find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 1:
        date = cols[0].text
        revenue = cols[1].text

    fill.append({'Date': date, 'Revenue': revenue})


tesla_revenue = pd.DataFrame(fill)


tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$', "", regex=True)

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]







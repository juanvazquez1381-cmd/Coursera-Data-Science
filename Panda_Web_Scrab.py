import pandas as pd
import requests
URL_1 = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
URL_2 = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}

def frame_builder(URL, headers, pos):
    

    try:
        # 1. Use requests.get with the headers
        response = requests.get(URL, headers=headers)
        response.raise_for_status() # Raises an HTTPError for bad responses (4XX or 5XX)

        # 2. Pass the raw text content to pandas.read_html
        # Specify the parser 'lxml' for reliability
        tables = pd.read_html(response.text, flavor='lxml')
        df = tables[pos]
        return df

        # The result 'tables' will be a list of DataFrames
        print(f"Successfully scraped {len(tables)} table(s).")
        # print(tables[0].head()) # Example: print the first few rows of the first table

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


banks = frame_builder(URL_1, headers, 0)

print(banks)






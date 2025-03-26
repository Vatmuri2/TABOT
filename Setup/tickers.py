import requests
from bs4 import BeautifulSoup

# Get S&P 500 tickers from Wikipedia
def get_sp500_wiki_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve S&P 500 data. HTTP Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    tickers = []
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')[1:]  # Skip the header row

    for row in rows:
        ticker = row.find_all('td')[0].text.strip()
        tickers.append(ticker)

    return tickers

# Get NASDAQ 100 tickers from Wikipedia
def get_nasdaq100_wiki_tickers():
    url = 'https://en.wikipedia.org/wiki/NASDAQ-100'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve NASDAQ 100 data. HTTP Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    tickers = []
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')[1:]  # Skip the header row

    for row in rows:
        ticker = row.find_all('td')[1].text.strip()  # Tickers are in the second column
        tickers.append(ticker)

    return tickers

# Get Russell 2000 tickers from a different reliable source
def get_russell2000_wiki_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_Russell_2000_companies'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve Russell 2000 data. HTTP Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    tickers = []
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')[1:]  # Skip the header row

    for row in rows:
        ticker = row.find_all('td')[0].text.strip()
        tickers.append(ticker)

    return tickers

# Save tickers to a file
def save_tickers_to_file(tickers, filename='tickers.txt'):
    with open(filename, 'w') as file:
        for ticker in tickers:
            file.write(f"{ticker}\n")

# Fetch and save tickers
def fetch_and_save_tickers():
    sp500_tickers = get_sp500_wiki_tickers()
    nasdaq100_tickers = get_nasdaq100_wiki_tickers()

    # Combine only S&P 500 and NASDAQ 100 tickers
    all_tickers = sp500_tickers + nasdaq100_tickers
    unique_tickers = list(set(all_tickers))  # Remove duplicates if any

    if unique_tickers:
        save_tickers_to_file(unique_tickers)
        print(f"Saved {len(unique_tickers)} unique tickers to tickers.txt")
    else:
        print("No tickers found.")

# Run the function
fetch_and_save_tickers()
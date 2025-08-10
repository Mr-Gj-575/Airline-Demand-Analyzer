from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_airline_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    data = []

    # Example scraping logic (this will need to be customized based on the actual website structure)
    for flight in soup.find_all('div', class_='flight-info'):
        flight_data = {
            'airline': flight.find('span', class_='airline-name').text,
            'price': flight.find('span', class_='flight-price').text,
            'departure': flight.find('span', class_='departure-time').text,
            'arrival': flight.find('span', class_='arrival-time').text,
        }
        data.append(flight_data)

    return pd.DataFrame(data)

def save_data_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
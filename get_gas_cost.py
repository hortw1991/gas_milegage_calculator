"""
Fetches the premium gas price from the Marathon website.
"""
import requests
from bs4 import BeautifulSoup

def get_gas_cost():
    # Look for status code 200 to show the page downloaded successfully
    url = requests.get('http://mymarathonstation.com/StoreHome/173385')
    if url.status_code != 200:
        print("Error loading page.")

    soup = BeautifulSoup(url.content, 'html.parser')

    # GasPrice 3 corresponds to premium.  (1 is regular, 2 is midrange).  This is split into 2 parts, the main cost
    # and the fractions of a cent cost.
    big_cost = soup.find('b', id='GasPriceBoldTag_3')
    big_cost = float(big_cost.get_text())

    # Split fraction
    little_frac = soup.find('span', id='GasPriceCentsSpan_3')  
    little_frac = little_frac.get_text()
    little_cost = fract_to_float(little_frac)

    # Combine fraction
    return big_cost + little_cost

def fract_to_float(little_frac):
    """ Splits the value of the fraction cents into a float value. """
    num, denom = little_frac.split('/')
    return float(num) / float(denom)
    


if __name__ == "__main__":
    gas_price_tester()

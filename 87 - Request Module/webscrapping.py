# ----------------------------------------------
# 🕷️ Simple Web Scraping with BeautifulSoup
# ----------------------------------------------

import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com"

# Send a GET request to the website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote elements on the page
    quotes = soup.find_all("span", class_="text")

    print("📜 Quotes from the website:\n")
    # Loop through and print each quote
    for quote in quotes:
        print(quote.get_text())
else:
    print("❌ Failed to fetch the page. Status code:", response.status_code)

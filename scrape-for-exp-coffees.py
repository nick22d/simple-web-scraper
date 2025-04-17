import requests
from bs4 import BeautifulSoup
import re

# URL of the coffee shop page
URL = "http://192.168.56.10:80/index.html"

# Load the page content
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    products = soup.find_all("a", class_="product")

    for product in products:
        name = product.find("div", class_="caption").text.strip()

        # Try to extract price (e.g., "$4.99") from the product block
        price_text = product.get_text()
        price_match = re.search(r'\$\s*(\d+(\.\d{1,2})?)', price_text)
        
        if price_match:
            price = float(price_match.group(1))
            if price > 4.0:
                print(f"{name} - ${price:.2f}")
else:
    print(f"Failed to fetch page: {response.status_code}")

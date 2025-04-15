import requests
from bs4 import BeautifulSoup

# URL of the mock coffee shop page (update with actual URL if hosted online)
URL = "http://192.168.56.101:80/index.html"  # Change this to an actual URL or local file path

# Load the page content
response = requests.get(URL)

if response.status_code == 200:  # Ensure request was successful
    soup = BeautifulSoup(response.text, "html.parser")
    
    products = soup.find_all("div", class_="product")

    for product in products:
        name = product.find("div", class_="caption").text.strip()
        print(name)
else:
    print(f"Failed to fetch page: {response.status_code}")


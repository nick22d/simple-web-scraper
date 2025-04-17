import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

# URL of the mock coffee shop page (update with actual URL if hosted online)
URL = "http://192.168.56.10:80/index.html"  # Change this to an actual URL or local file path

# Parse the robots.txt to check allowed paths
parsed_url = urlparse(URL)
robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

# Initialize RobotFileParser and read the robots.txt
rp = RobotFileParser()
rp.set_url(robots_url)
rp.read()

# Check if scraping is allowed for the given URL path
if rp.can_fetch("*", URL):
    # Load the page content
    response = requests.get(URL)

    if response.status_code == 200:  # Ensure request was successful
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("a", class_="product")

        for product in products:
            name = product.find("div", class_="caption").text.strip()
            print(name)
    else:
        print(f"Failed to fetch page: {response.status_code}")
else:
    print(f"Scraping is not allowed for this page according to robots.txt: {URL}")

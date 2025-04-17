import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse, urljoin

# Base URL of the site
BASE_URL = "http://192.168.56.10:80"
INDEX_URL = f"{BASE_URL}/index.html"

# Load and parse robots.txt
robots_url = f"{BASE_URL}/robots.txt"
rp = RobotFileParser()
rp.set_url(robots_url)
rp.read()

# Request the homepage
if rp.can_fetch("*", INDEX_URL):
    response = requests.get(INDEX_URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("a", class_="product")

        for product in products:
            href = product.get("href")
            full_url = urljoin(BASE_URL, href)

            # Respect robots.txt for each product page
            if rp.can_fetch("*", full_url):
                caption = product.find("div", class_="caption")
                if caption:
                    print(caption.text.strip())
            else:
                print(f"Skipping (disallowed by robots.txt): {full_url}")
    else:
        print(f"Failed to fetch page: {response.status_code}")
else:
    print(f"Scraping is not allowed for: {INDEX_URL}")

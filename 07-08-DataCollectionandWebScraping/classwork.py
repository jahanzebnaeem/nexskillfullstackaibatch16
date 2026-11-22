import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=15)
response.raise_for_status()  # Check if the request was successful

soup = BeautifulSoup(response.content, "html.parser")

for book in soup.find_all("h3"):
    title = book.find("a")["title"]
    #price = book.select_one(".price_color").get_text(strip=True)
    price = book.find_next("p", class_="price_color").get_text(strip=True)
    #availability = book.select_one(".availability").get_text(" ", strip=True)
    availability = book.find_next("p", class_="instock availability").get_text(" ", strip=True)
    #print(title, price, availability)
    #if "In stock" in availability:
    if availability.strip() == "In stock":
        print(title, price, availability)
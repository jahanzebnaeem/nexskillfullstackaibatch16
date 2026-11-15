import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=15)
response.raise_for_status()  # Check if the request was successful

soup = BeautifulSoup(response.content, "html.parser")

for book in soup.find_all("h3"):
    title = book.find("a")["title"]
    print(title)